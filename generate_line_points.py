import random
import os
import openai
from typing import DefaultDict
from scipy.stats import norm

def linear_function(x, a, b):
    return a*x + b

random.seed(1)

line_coefficients = []
num_of_lines = 5
for _ in range(num_of_lines):
    line_coefficients.append( (random.randint(-30, 30+1),
                                random.randint(-100, 100+1)) )

k_vals = [5, 15, 50]
chosen_points = DefaultDict()

print(line_coefficients)
for k in k_vals:
    chosen_points[k] = random.sample(range(1, 99+1), k=k)
print(chosen_points)

for model_num, (a, b) in enumerate(line_coefficients):
    with open(os.path.join('models_info', f'model_{model_num+1}.txt'), 'w') as file:
        file.write(f"Coefficients are a = {a}, b = {b}, where the function is f(x) = ax + b. ")
        file.write("(With an added random error drawn from the normal distribution with mean 0 and st. dev. 10 if applicable.)")

    for k in k_vals:
        with open(os.path.join(f'inputs_k_{k}_nonrandom', f'model_{model_num+1}_input.txt'), 'w') as file:
            for x in chosen_points[k]:
                file.write(f"Input = {x}, output = {linear_function(x, a, b,)}\n")

    for k in k_vals:
        with open(os.path.join(f'inputs_k_{k}_random', f'model_{model_num+1}_input.txt'), 'w') as file:
            for x in chosen_points[k]:
                normal = norm.rvs(loc=0, scale=50, size=1, random_state=None)[0]
                print(normal)
                file.write(f"Input = {x}, output = {round(normal + linear_function(x, a, b,))}\n")

all_chosen = chosen_points[3] + chosen_points[15] + chosen_points[50]
sample_to_predict = random.sample([x for x in range(1, 99+1) if x not in all_chosen], k=20)

openai.api_key = "totally_my_key"


"""
for model_num, it in enumerate(line_coefficients):
    for k in k_vals:
        print(f"Querying the API for the model number {model_num+1} and for {k} examples . . .")
        with open(os.path.join(f'inputs_k_{k}_nonrandom', f'model_{model_num+1}_input.txt'), 'r') as file:
            input_text = file.read()
        with open(os.path.join(f'outputs_k_{k}_nonrandom', f'model_{model_num+1}_outputs.txt'), 'w') as file:
            for x in sample_to_predict:
                input_text_appended = input_text + f"Input = {x}, output ="
                response = openai.Completion.create(engine="davinci",
                        prompt=input_text_appended, max_tokens=4,
                        temperature=0, top_p=0)
                response_num = response['choices'][0]['text']
                file.write(f"Input = {x}, output = {response_num}\n")
                """
