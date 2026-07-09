# Visual Self-Refine GPT-4V Notebook Prompt / Logic Audit

Source: `colabs/Visual-Self-Refine-GPT4V.ipynb`

This notebook is not part of the core Python `src/` package, but it contains valuable Self-Refine logic and prompts for visual/TikZ refinement using GPT-4 and GPT-4V. It was added after review.

---

## Cell 0 — markdown

```markdown
<a href="https://colab.research.google.com/github/madaan/self-refine/blob/main/colabs/Visual-Self-Refine-GPT4V.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
```

---

## Cell 2 — code

```python
!pip install folium==0.2.1 --quiet
!pip install pdflatex --quiet
!apt-get install texlive-latex-recommended
!apt install texlive-latex-extra
!apt install dvipng
!apt-get install imagemagick
!apt-get install ghostscript
!pip install openai --quiet
```

---

## Cell 4 — markdown

```markdown
## Tikz to JPEG Utilities
```

---

## Cell 5 — code

```python
import subprocess
import base64
import os
from tempfile import NamedTemporaryFile
from IPython.display import display, Image
import base64


# Function to display the image
def display_base64_image(base64_str):
    display(Image(data=base64.b64decode(base64_str)))

def remove_if_exists(filename):
    if os.path.exists(filename):
        os.remove(filename)

def latex_to_base64_jpeg(latex_code, patience: int = 5):
    # Create a temporary file for the LaTeX code
    with NamedTemporaryFile(suffix=".tex", delete=False) as tex_file:
        tex_filename = tex_file.name
        tex_file.write(latex_code.encode('utf-8'))
        tex_file.flush()

        # Compile the LaTeX file into a PDF
        result = subprocess.run(['pdflatex', '-output-directory', os.path.dirname(tex_filename), tex_filename], capture_output=True)
        if result.returncode != 0:
            print(f"pdflatex failed with exit code: {result.returncode}, patience {patience}")
            output = result.stdout.decode()
            error = result.stderr.decode()
            if patience > 0:
              print(f"Attempting to fix!")
              fixed_latex = fix_latex(latex_code, error_message=output + "\n\n" + error)
              return latex_to_base64_jpeg(fixed_latex, patience - 1)

            return None

        # Convert the produced PDF to a JPEG image
        pdf_filename = tex_filename.replace('.tex', '.pdf')
        if not os.path.exists(pdf_filename):
            print("PDF file was not created.")
            remove_if_exists(tex_filename)
            return None

        jpeg_filename = tex_filename.replace('.tex', '.jpeg')
        # result = subprocess.run(['convert', '-density', '300', pdf_filename, '-quality', '90', jpeg_filename], capture_output=True)
        result = subprocess.run([
            'gs',
            '-sDEVICE=jpeg',
            '-dPDFFitPage',
            '-g512x512',
            '-o', jpeg_filename,
            '-r300',
            pdf_filename
        ], capture_output=True)

        if result.returncode != 0:
            print("convert failed with exit code:", result.returncode)
            output = result.stdout.decode()
            error = result.stderr.decode()
            if patience > 0:
              print(f"Attempting to fix!")
              fixed_latex = fix_latex(latex_code, error_message=output + "\n\n" + error)
              return latex_to_base64_jpeg(fixed_latex, patience - 1)

            return None

        if not os.path.exists(jpeg_filename):
            print("JPEG file was not created.")
            remove_if_exists(tex_filename)
            remove_if_exists(pdf_filename)
            return None

        # Encode the JPEG image to base64
        with open(jpeg_filename, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

        remove_if_exists(tex_filename)
        remove_if_exists(pdf_filename)
        remove_if_exists(jpeg_filename)

        return encoded_string

```

---

## Cell 7 — markdown

```markdown
## Self-Refine Loop
```

---

## Cell 8 — markdown

```markdown
### Initialize

* Note: the initial tikz is written by GPT-4, which the GPT-4V improves upon. GPT-4 is not used after the initial call, and the entire feedback -> refine process is handled by GPT4-V
```

---

## Cell 9 — code

```python
import base64
import requests
import re
import openai
from openai import OpenAI
from tqdm import tqdm



def get_initial_latex(object_name, model="gpt-4-0613"):
    client = OpenAI(api_key=os.environ["OPEN_API_KEY"])

    # The "simple" here is intentional: I tried multiple variants: awesome, nice, cool.
    # but starting with simple and refining leads to the lower error rates.
    prompt = f"""Generate LaTeX code that draws a simple {object_name} using Tikz.
Please make sure that the latex code is self-contained (no fancy packages except Tikz-related imports). Please don't forget to include \\usepackage{{tikz}} and \\usetikzlibrary{{shapes.geometric}}! Please use colors.
I know it's a difficult task, try your best! Return your result in a  ```latex block"""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant who can write Tikz code."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.0
    )
    return response


def fix_latex(latex_code, error_message, model="gpt-4-0613"):

    client = OpenAI(api_key=os.environ["OPEN_API_KEY"])
    prompt = f"""Error log:\n\n{error_message}


Buggy code:

```latex
{latex_code}
```
Please fix the bug and return the fixed code in a latex block ```latex."""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant who can write Tikz code."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.0
    )
    return extract_latex_from_response(response)



def extract_latex_from_response(response):
    # Check if the response is a dictionary and has the 'choices' key
    if isinstance(response, openai.types.chat.chat_completion.ChatCompletion):
      content = response.choices[0].message.content
    elif isinstance(response, dict) and 'choices' in response:
      content = response['choices'][0]['message']['content']
    elif isinstance(response, str) and isinstance(json.loads(response), dict) and 'choices' in json.loads(response):
      content = json.loads(response)['choices'][0]['message']['content']
    else:
      print("Invalid response format.")
      return None

    # Define the regex pattern for LaTeX code block
    latex_pattern = r"```(?:latex|tex)\n([\s\S]*?)\n```"


    # Search for LaTeX code block
    matches = re.search(latex_pattern, content)

    # If a match is found, return the LaTeX code
    if matches:
        return matches.group(1)
    else:
        print("No LaTeX code block found.")
        return content

```

---

## Cell 10 — markdown

```markdown
### Feedback and Refine
```

---

## Cell 11 — code

```python
def get_refinement_prompt(object_name):
  return f"""This is the Tikz/Latex code for {object_name} shown in the picture. Can you improve it?

First, understand the current picture.

Then, think about how can it be improved.

Then, rewrite the Tikz code to improve the image.

Please make sure that the latex code is self-contained (no fancy packages except Tikz-related imports). Please don't forget to include \\usepackage{{tikz}} and \\usetikzlibrary{{shapes.geometric}}!

Return your result in a  ```latex block"""



def vlm_call(base64_image, latex_code, text_prompt, api_key):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    },
                    {
                        "type": "text",
                        "text": f"```latex\n\n{latex_code}\n\n```{text_prompt}"
                    },

                ]
            }
        ],
        "max_tokens": 3000,
        "temperature": 0.0
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    # print(response.json()['choices'][0]['message']['content'])
    return response



```

---

## Cell 13 — markdown

```markdown
### Self-Refine Loop
```

---

## Cell 15 — code

```python
# Pick the object to draw
object_name = "sphere" #@param {type:"string"}
n_refine_loop = 5 #@param {type:"slider", min:2, max:10, step:1}
```

---

## Cell 17 — code

```python
init_response = get_initial_latex(object_name)
init_code = extract_latex_from_response(init_response)
base64_image = latex_to_base64_jpeg(init_code)
# Store the initial result
results = [(init_code, init_response)]

# Iteratively refine the LaTeX code
num_exceptions_ok = 2
for i in tqdm(range(n_refine_loop), desc=f"Drawing {object_name}"):
  try:
    base64_image = latex_to_base64_jpeg(init_code) or base64_image
    if base64_image is None:
      print(f"Error in turn {i+1}")
      break
    response = vlm_call(latex_code=init_code, base64_image=base64_image,
                        text_prompt=get_refinement_prompt(object_name), api_key=os.environ["OPEN_API_KEY"])
    refined_code = extract_latex_from_response(response.json())

    results.append((refined_code, response))
    init_code = refined_code or init_code
  except Exception as e:
    if num_exceptions_ok > 0:
      num_exceptions_ok -= 1
      continue
    else:
      break
    print(f"Error in turn {i+1}")





```

---

## Cell 21 — code

```python
import base64
from PIL import Image, ImageDraw, ImageFont, ImageOps
from io import BytesIO
import imageio.v2 as imageio  # Use imageio version 2

!rm *.png
!rm *.gif

import re

def to_safe_filename(s):
    s = re.sub(r'\W|^(?=\d)', '_', s)

    if s[0].isdigit():
        s = '_' + s

    return s.lower()[:25]

object_name = to_safe_filename(object_name)
gif_file_name = f"{object_name}.gif"
latex_codes_file_name = f"{object_name}.json"

def base64_to_image(base64_string):
    img_data = base64.b64decode(base64_string)
    return Image.open(BytesIO(img_data))



def save_annotated_images_from_latex(latex_codes, font_path='/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf', font_size=50):
    for i, latex_code in enumerate(latex_codes):
      try:
        image = base64_to_image(latex_to_base64_jpeg(latex_code, patience=2))

        # Annotating the image with a larger font
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(font_path, font_size)
        text = f"Step {i}"
        textwidth, textheight = draw.textbbox((0, 0), text, font=font)[2:]  # Get text size
        x, y = image.width - textwidth - 10, image.height - textheight - 10
        draw.text((x, y), text, font=font, fill="black")

        image.save(f"annotated_{object_name}_{i+1}.png")
      except Exception as e:
        print(f"Error in saving image {i+1}")


def create_gif(image_count, fps=1, loop=0):
    images = []
    for i in range(image_count):
        # check if image exists
        if not os.path.exists(f"annotated_{object_name}_{i+1}.png"):
            print(f"Image {i+1} does not exist.")
            continue
        images.append(imageio.imread(f"annotated_{object_name}_{i+1}.png"))
    imageio.mimsave(gif_file_name, images, fps=fps, loop=loop)


```

---

## Cell 22 — code

```python
# Extracting LaTeX codes from the results
latex_codes = [latex_code for latex_code, _ in results]

# Save annotated images
save_annotated_images_from_latex(latex_codes)

# Create and display GIF
create_gif(len(latex_codes), fps=1, loop=0)  # Adjust fps as needed

# Display the GIF in Colab
from IPython.display import Image
Image(open(gif_file_name,'rb').read())


```

---

## Cell 23 — code

```python
from google.colab import files
files.download(gif_file_name)
tikz_code = [results[0] for results in results]
with open(latex_codes_file_name, "w") as f:
  for i in range(len(tikz_code)):
    tmp = {"object": object_name, "step": i+1, "code": tikz_code[i]}
    f.write(json.dumps(tmp) + "\n")
files.download(latex_codes_file_name)
```


## Extracted notebook flow

1. User chooses `object_name` and `n_refine_loop`.
2. `get_initial_latex(object_name)` calls GPT-4 with a system prompt: `You are a helpful assistant who can write Tikz code.`
3. The user prompt asks for self-contained TikZ/LaTeX code for a simple object, with colors, `\usepackage{tikz}`, and a fenced `latex` block.
4. `latex_to_base64_jpeg` compiles/renders the current TikZ code into an image.
5. `get_refinement_prompt(object_name)` asks GPT-4V to inspect the image, understand it, identify improvements, and rewrite the TikZ code.
6. `vlm_call` sends both the rendered image and current LaTeX code to GPT-4V.
7. Loop: `for i in range(n_refine_loop)`; update `init_code` with refined code.
8. Stop early if no image is available or if more than `num_exceptions_ok` exceptions occur.
9. `fix_latex` is available as a repair path when LaTeX compilation errors occur.
