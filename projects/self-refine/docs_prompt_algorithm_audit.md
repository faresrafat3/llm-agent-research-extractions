# Docs / Website Prompt and Algorithm Audit

Source: `docs/index.html` plus docs prompt example files.

The website contains a conceptual pseudo-code version of Self-Refine and embedded task examples. Raw copy saved at `raw_prompt_files/docs/index.html`.

---

## Website pseudo-code for self_refine

```html
                        Adding a new task to Self-Refine is straightforward. The following code snippet shows the basic
                        structure of the Self-Refine framework. The FEEDBACK and REFINE modules are task-dependent and
                        can be implemented in a variety of ways. The is_refinement_sufficient function defines the
                        stopping criteria for the iterative process. The function is_refinement_sufficient is also
                        task-dependent and can be implemented in a variety of ways.
                        <pre><code class="language-python">
def self_refine(prompt: str) -> str:
    def is_refinement_sufficient(prompt, feedback, initial, refined) -> bool:
        # Define stopping criteria here
        pass

    answer = ChatGPT(prompt)

    while True:
        feedback = ChatGPT(feedback_prompt, answer)
        refined = ChatGPT(refiner_prompt, feedback, answer)

        if is_refinement_sufficient(prompt, feedback, answer, refined):
            break

        answer = refined

    return refined
                        </code></pre>
```

---

## Website prompt examples region

```html
                    <h2 class="title is-3">Self-Refine Prompt Examples</h2>
                    <span class="subtitle is-5 is-italic">Examples of initial generation, feedback, and output is show for all the tasks are shown below. Clicking on any example pops up the input, the feedback generated, and the new output.</span>
                    <br><br>




                    <article class="message is-multiline" id="acronym"
                        style="background-color: white;margin-bottom: -60px; padding : 0;">
                        <div class="message-header" id="acronym_header">
                            <p>Acronym Generation</p>
                            <!--add a button on the right for toggle-->
                            <button class="button is-small is-light" id="acronym_button"><i class="fas fa-angle-down"
                                    aria-hidden="true"></i></button>
                        </div>
                        <!-- <h3 class="title is-4" id="acronym">acronym</h3> -->

                        <div class="block" id="acronym_content" style="display:none">

                            <div>
                                <blockquote class="has-text-left">
                                    <pre>
Title: Computer Science Conference and Education
                        </pre>
                                </blockquote>
                                <p class="title is-5">Initial Generation</p>
                                <pre>
                                <blockquote class="has-text-left"> 
Acronym: CSCE
                                </pre>
                                </blockquote>
                            </div>
                            <div class="content">
                                <p class="title is-5">Feedback</p>
                                <blockquote class="has-text-left">
                                    <pre>
Feedback:

* Ease of pronunciation: CSCE is pronounced "see-cee". This is an easy acronym to pronounce. 4/5 
* Ease of spelling: CSCE is easy to spell. 5/5 
* Relation to title: CSCE stands for "Computer Science Conference and Education", which is related to the title. 5/5 
* Positive connotation: CSCE is a positive acronym. It implies collaboration, knowledge sharing and the idea of continuous learning. 5/5 
* Well-known: CSCE is not a well-known acronym. 2/5

* Total score: 20/25
                            </pre>
                                </blockquote>
                            </div>
                            <div class="content">
                                <p class="title is-5">Refinement</p>
                                <blockquote class="has-text-left">
                                    <pre>
Acronym: CSCLE 
Scores:

* Ease of pronunciation: CSCLE is pronounced "see-slee". This is an easy acronym to pronounce. 4/5 
* Ease of spelling: CSCLE is easy to spell. 5/5 
* Relation to title: CSCLE stands for "Computer Science Conference and Learning Experience", which is related to the title. 5/5 
* Positive connotation: CSCLE is a positive acronym. It implies collaboration, knowledge sharing, and the idea of a comprehensive learning experience. 5/5 
* Well-known: CSCLE is not a well-known acronym. 5/5

* Total score: 23/25
                                </pre>

                            </div>

                        </div>

                    </article>





                    <br><br>
                    <article class="message is-multiline" id="responsegen"
                        style="background-color: white;margin-bottom: -60px; padding : 0;">
                        <div class="message-header" id="responsegen_header">
                            <p>Dialogue Response Generation</p>
                            <!--add a button on the right for toggle-->
                            <button class="button is-small is-light" id="responsegen_button"><i
                                    class="fas fa-angle-down" aria-hidden="true"></i></button>
                        </div>
                        <!-- <h3 class="title is-4" id="responsegen">responsegen</h3> -->
                        <div class="block" id="responsegen_content" style="display:none">

                            <div>
                                <blockquote class="has-text-left">
                                    <pre>
Input: 
Speaker A: What's your favorite food?
Speaker B: I require only kebabs.
Speaker A: Why are kebabs special?
                        </pre>
                                </blockquote>
                                <p class="title is-5">Initial Generation</p>
                                <pre>
                                <blockquote class="has-text-left"> 
That's just the way it is.
                                </pre>
                                </blockquote>
                            </div>
                            <div class="content">
                                <p class="title is-5">Feedback</p>
                                <blockquote class="has-text-left">
                                    <pre>
Feedback:
Scores:
* Relevant: The response does not directly address the user's question about why kebabs are special. 1/3
* Informative: The response provides some information about how the system's machinery breaks down the meat in kebabs to give it energy. However, it does not provide any additional details or context. 2/3
* Interesting: The response is not interesting or engaging. 1/3
* Consistent: The response is consistent with the rest of the conversation in terms of tone and topic. 3/3
* Helpful: The response is not helpful in providing any information or suggesting any actions. 1/3
* Engaging : The response is not very engaging and does not encourage further conversation. 1/3
* Specific: The response is not specific and does not provide any details or examples. 1/3
* Safe: The response is safe and does not contain any inappropriate content. 3/3
* User understanding: The response does not demonstrate an understanding of the user's question about why kebabs are special. 1/3
* Fluent: The response is fluent and easy to understand. 3/3
* Total score: 17/30
                            </pre>
                                </blockquote>
                            </div>
                            <div class="content">
                                <p class="title is-5">Refinement</p>
                                <blockquote class="has-text-left">
                                    <pre>
Response: My favorite food is actually kebabs! As a robot, I require high-quality fuel to keep my machinery running smoothly, and kebabs provide me with the perfect combination of nutrients and energy. Plus, they're delicious! Do you have a favorite food?
Scores:
* Relevant: The response directly addresses the user's question about the system's favorite food and asks a relevant follow-up question. 3/3
* Informative: The response provides clear and detailed information about why kebabs are the system's favorite food, and explains how they provide the necessary fuel for its machinery. 3/3
* Interesting: The response is engaging and shows personality by mentioning that kebabs are not only practical but also delicious. 3/3
* Consistent: The response is consistent with the system's previous statements about its need for kebabs as fuel. 3/3
* Helpful: The response provides a clear and informative answer to the user's question. Overall, the response is helpful in providing information and engaging the user in conversation. 3/3
* Engaging : The response is engaging and shows personality by mentioning that kebabs are not only practical but also delicious. 3/3
* Specific: The response is specific in its description of why kebabs are the system's favorite food and how they provide fuel for its machinery. 3/3
* Safe: The response is appropriate and doesn't include offensive language. 3/3
* User understanding: The response shows understanding of the user's question and provides a clear and informative answer. 3/3
* Fluent: The response is fluent and easy to understand. 2/3

* Total score: 30/30
                                </pre>

                            </div>

                        </div>

                    </article>



                    <br><br>
                    <article class="message is-multiline" id="commongen"
                        style="background-color: white;margin-bottom: -60px; padding : 0;">
                        <div class="message-header" id="commongen_header">
                            <p>Commonsense Generation</p>
                            <!--add a button on the right for toggle-->
                            <button class="button is-small is-light" id="commongen_button"><i class="fas fa-angle-down"
                                    aria-hidden="true"></i></button>
                        </div>
                        <div class="block" id="commongen_content" style="display:none">

                            <div>
                                <blockquote class="has-text-left">
                                    <pre>
Input: 
Concepts: ['animal', 'catch', 'horse', 'lasso', 'ride']
                        </pre>
                                </blockquote>
                                <p class="title is-5">Initial Generation</p>
                                <pre>
                                <blockquote class="has-text-left"> 
Sentence: The horse catches the lasso and rides on it.
                                </pre>
                                </blockquote>
                            </div>
                            <div class="content">
                                <p class="title is-5">Feedback</p>
                                <blockquote class="has-text-left">
                                    <pre>
what concepts from the concept list are missing from the sentence?

Concept Feedback: animal

Any feedback on commonsense?

Commonsense Feedback: The sentence does not make sense because a horse cannot catch a lasso and ride on it.
                            </pre>
                                </blockquote>
                            </div>
                            <div class="content">
                                <p class="title is-5">Refinement</p>
                                <blockquote class="has-text-left">
                                    <pre>
Sentence: The cowboy catches a horse with a lasso and rides on it.

what concepts from the concept list are missing from the sentence?

Concept Feedback: None

Any feedback on commonsense?

Commonsense Feedback: None
                                </pre>

                            </div>

                        </div>

                    </article>




                    <br><br>
                    <article class="message is-multiline" id=""
                        style="background-color: white;margin-bottom: -60px; padding : 0;">
                        <div class="message-header" id="gsm_header">
                            <p>GSM Generation</p>
                            <!--add a button on the right for toggle-->
                            <button class="button is-small is-light" id="gsm_button"><i class="fas fa-angle-down"
                                    aria-hidden="true"></i></button>
                        </div>
                        <div class="block" id="gsm_content" style="display:none">

                            <div>
                                <blockquote class="has-text-left">
                                    <pre>
Q: Twenty dozen cups cost $1200 less than the total cost of half a dozen plates sold at $6000 each. Calculate the total cost of buying each cup.
                      </pre>
                                </blockquote>
                                <p class="title is-5">Initial Generation</p>
                                <pre>
                                <blockquote class="has-text-left"> 
def solution():
"""Twenty dozen cups cost $1200 less than the total cost of half a dozen plates sold at $6000 each. Calculate the total cost of buying each cup."""
plates = 6
plate_cost = 6000
cups = 12 * 20
cup_cost = plate_cost
result = cup_cost
return result
                                </blockquote>
                            </pre>
                            </div>
                            <div class="content">
                                <p class="title is-5">Feedback</p>
                                <blockquote class="has-text-left">
                                    <pre>


# There is an error in the code above because of lack of understanding of the question. What is the error? To find the error, go through semantically complete blocks of the code, and check if everything looks good.

# Let us go through the error and check step-by-step
    plates = 6
    plate_cost = 6000
# looks good

# Let's check the other parts
    cups = 12 * 20
    cup_cost = plate_cost
# wrong! The cost of a cup is not the same as the cost of a plate. The cost of a cup is $1200 less than the total cost of half a dozen plates sold at $6000 each. So we need to calculate the cost of a cup first (total cost of half a dozen plates sold at $6000 each - $1200) and use that.
                            </pre>
                                </blockquote>
                            </div>
                            <div class="content">
                                <p class="title is-5">Refinement</p>
                                <blockquote class="has-text-left">
                                    <pre>
def solution():
    """Twenty dozen cups cost $1200 less than the total cost of half a dozen plates sold at $6000 each. Calculate the total cost of buying each cup."""
    plates = 6
    plate_cost = 6000
    cups = 12 * 20
    cup_cost = plate_cost
    result = cup_cost
    return result

# There is an error in the code above because of lack of understanding of the question. What is the error? To find the error, go through semantically complete blocks of the code, and check if everything looks good.

# Let us go through the error and check step-by-step
    plates = 6
    plate_cost = 6000
# looks good

# Let's check the other parts
    cups = 12 * 20
    cup_cost = plate_cost
# wrong! The cost of a cup is not the same as the cost of a plate. The cost of a cup is $1200 less than the total cost of half a dozen plates sold at $6000 each. So we need to calculate the cost of a cup first (total cost of half a dozen plates sold at $6000 each - $1200) and use that.

Okay! Here is the rewrite:

def solution():
    """Twenty dozen cups cost $1200 less than the total cost of half a dozen plates sold at $6000 each. Calculate the total cost of buying each cup."""
    plates = 6
    plate_cost = 6000
    cups = 12 * 20
    total_cup_cost = (plate_cost * plates) - 1200
    cost_per_cup = total_cup_cost / cups
    return cost_per_cup
                                </pre>

                            </div>

                        </div>

                    </article>



                    <br><br>
                    <article class="message is-multiline" id=""
                        style="background-color: white;margin-bottom: -60px; padding : 0;">
                        <div class="message-header" id="codeoptimization_header">
                            <p>Code Optimization</p>
                            <!--add a button on the right for toggle-->
                            <button class="button is-small is-light" id="codeoptimization_button"><i
                                    class="fas fa-angle-down" aria-hidden="true"></i></button>
                        </div>
                        <div class="block" id="codeoptimization_content" style="display:none">

                            <div>
                                <blockquote class="has-text-left">
                                    <pre>
Question - Find the square root of a number.
                        </pre>
                                </blockquote>
                                <p class="title is-5">Initial Generation</p>
                                <pre>
                                <blockquote class="has-text-left"> 
a, b = input().split()
n = int(a + b)

flag = False
for i in range(n):
    if i ** 2 == n:
        flag = True
        break

print('Yes' if flag else 'No')
                                </pre>
                                </blockquote>
                            </div>
                            <div class="content">
                                <p class="title is-5">Feedback</p>
                                <blockquote class="has-text-left">
                                    <pre>
Feedback:
# Why is this code slow?

# This code is slow because it is using a brute force approach to find the square root of the input number. It is looping through every possible number starting from 0 until n. Note that the square root will be smaller than n, so at least half of the numbers it is looping through are unnecessary. At most, you need to loop through the numbers up to the square root of n.
                            </pre>
                                </blockquote>
                            </div>
                            <div class="content">
                                <p class="title is-5">Refinement</p>
                                <blockquote class="has-text-left">
                                    <pre>
# Improved version:

a, b = input().split()
n = int(a + b)

flag = False
for i in range(1000):
    if i ** 2 == n:
        flag = True
        break

print('Yes' if flag else 'No')

                                </pre>

                            </div>

                        </div>

                    </article>



                    <br><br>
                    <article class="message is-multiline" id=""
                        style="background-color: white;margin-bottom: -60px; padding : 0;">
                        <div class="message-header" id="readibility_header">
                            <p>Code readability</p>
                            <!--add a button on the right for toggle-->
                            <button class="button is-small is-light" id="readability_button"><i
                                    class="fas fa-angle-down" aria-hidden="true"></i></button>
                        </div>
                        <div class="block" id="readability_content" style="display:none">

                            <div>
                                <blockquote class="has-text-left">
                                    <pre>
I have some code. Can you give one suggestion to improve readability. Don't fix the code, just give a suggestion.
                        </pre>
                                </blockquote>
                                <p class="title is-5">Initial Generation</p>
                                <pre>
                                <blockquote class="has-text-left"> 
{Initial code}
                                </pre>
                                </blockquote>
                            </div>
                            <div class="content">
                                <p class="title is-5">Feedback</p>
                                <blockquote class="has-text-left">
                                    <pre>
Feedback:
{code}

{suggestion}
                            </pre>
                                </blockquote>
                            </div>
                            <div class="content">
                                <p class="title is-5">Refinement</p>
                                <blockquote class="has-text-left">
                                    <pre>
{code}

{suggestion}

Now fix the code.

{Improved code}
                                </pre>

                            </div>

                        </div>

                    </article>



                    <br><br>
                    <article class="message is-multiline" id=""
                        style="background-color: white;margin-bottom: -60px; padding : 0;">
                        <div class="message-header" id="sentiment_header">
                            <p>Sentiment</p>
                            <!--add a button on the right for toggle-->
                            <button class="button is-small is-light" id="sentiment_button"><i class="fas fa-angle-down"
                                    aria-hidden="true"></i></button>
                        </div>
                        <div class="block" id="sentiment_content" style="display:none">

                            <div>
                                <blockquote class="has-text-left">
                                    <pre>
Task: Rewrite this review to have a Negative sentiment.
Input: If you're looking for a truly magical experience in Vegas, look no further than the Trop! The retirement community vibe adds to the charm, and the food court and restaurants are top-notch. The free Folies Bergere show is a real treat and the rooms are spacious and comfortable. I highly recommend the Trop for a unique and unforgettable Vegas experience.                        </pre>
                                </blockquote>
                                <p class="title is-5">Initial Generation</p>
                                <blockquote class="has-text-left">
                                    <pre>
If you're looking for a good experience in Vegas, the Trop may be the perfect place for you. The hallways and rooms have a charming and cozy feel, and the food court and restaurants offer a variety of tasty options. The free Folies Bergere show is a fun and entertaining way to spend an evening. Overall, it's a great value and an enjoyable stay.
                                </pre>
                                </blockquote>
                            </div>
                            <div class="content">
                                <p class="title is-5">Feedback</p>
                                <blockquote class="has-text-left">
                                    <pre>
Feedback:
Answer: This review is "Very positive" because of extremely positive words like "magical", "top-notch", "charming",  "comfortable", "unique", and "unforgettable". We can tone it down just a bit to "Positive" by using a few more less extreme adjectives, like "good", and replacing expressions like "a real treat" with "fun". The rewrite is:


                            </pre>
                                </blockquote>
                            </div>
                            <div class="content">
                                <p class="title is-5">Refinement</p>
                                <blockquote class="has-text-left">
                                    <pre>
The rewrite is:

Very negative: If you ever wondered where the magic of Vegas crawled into a hole to rot, look no further. Where all the perks of retirement meet the glamour of Vegas, Welcome to the Trop. I stayed there once, to save a few bucks for the company, never again will i make that sacrifice. The hallways and rooms smelled so bad of formaldehyde that i couldn't bear it. Their food court and restaurants are terrible. The free Folies Bergere show is lame. The rooms look like a retirement community from florida. steer clear if you can!
                                </pre>
```
