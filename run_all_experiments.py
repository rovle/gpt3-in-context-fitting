import json
import openai
import re
import os


with open('experiments_log.json', 'r') as file:
    experiments = json.loads(file.read())

openai.api_key = os.getenv("OPENAI_API_KEY")

for experiment_name in experiments.keys():
    if 'output_test_raw' in experiments[experiment_name].keys():
        print(f"Have already performed {experiment_name}, skipping it now.")
        continue
    print(f"Running experiment {experiment_name}")    
    experiment = experiments[experiment_name]
    experiment['response'] = []
    experiment['output_test_raw'] = []
    experiment['output_test_cleaned'] = []
    for point in experiment['input_test']:
        if hasattr(point, '__iter__'):
            pass
        else:
            prompt_text = (experiment['input_text']
                            + f'Input = {point}, output =')
        response = openai.Completion.create(engine="davinci",
                        prompt=prompt_text, max_tokens=6,
                        temperature=0, top_p=0)
        experiment['response'].append(response)
        response_text = response['choices'][0]['text']
        experiment['output_test_raw'].append(response_text)
        experiment['output_test_cleaned'].append(
            int(
                re.findall('-?\d+',response_text
                        )[0]
                )
            )
        experiments[experiment_name] = experiment

with open('experiments_log.json', 'w') as file:
    json.dump(experiments, file, indent=4)
