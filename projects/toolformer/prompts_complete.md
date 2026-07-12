# Toolformer Prompts

API call representation e(c)=<API> ac(ic) </API> e(c,r)=<API> ac(ic) ->r </API>

Example: [QA("Where was Joe Biden born?")] etc
Filtering Li(z) L+ L- keep if L- - L+ >= tauf
Model Finetuning merge remaining API calls interleave x* = x1:i-1, e(ci,ri), xi:n
Inference regular decoding until -> token interrupt call API get response
