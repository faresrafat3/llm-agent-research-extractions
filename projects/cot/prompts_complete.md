# CoT Prompts

Standard:
Q: Roger has 5 tennis balls... A: The answer is 11.

CoT:
Q: Roger has 5 tennis balls... A: Roger started with 5 balls. 2 cans of 3 each is 6. 5+6=11. The answer is 11.

Q: The cafeteria had 23 apples If they used 20 to make lunch and bought 6 more how many apples do they have?
A: The cafeteria had 23 apples originally. They used 20 to make lunch. So they had 23-20=3. They bought 6 more apples, so they have 3+6=9. The answer is 9.

Template:
Q: {{input}} A: {{chain_of_thought}} The answer is {{output}}.

Zero-Shot CoT: Let's think step by step.
