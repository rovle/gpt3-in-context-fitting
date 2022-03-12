"""
Just a small script which takes the usual classification task of 2d points,
but replaces labels with 1 if the first coordinate is even, 0 otherwise.

No models find to "spot the pattern" here (see classification_playground.ipynb),
and so they have random classifier's accuracy, 50%.
"""


import json

with open('experiments_log.json', 'r') as file:
    experiments = json.loads(file.read())

for rs in [42, 55, 93]:
    experiment = experiments[f'2d_class_type_1_rstate_{rs}']

    new_experiment = dict()
    train_labels = []
    for point in experiment['input_train']:
        x, y = point
        if x % 2 == 0:
            train_labels.append(1)
        else:
            train_labels.append(0)

    test_labels = []
    for point in experiment['input_test']:
        x, y = point
        if x % 2 == 0:
            test_labels.append(1)
        else:
            test_labels.append(0)


    new_experiment['input_train'] = experiment['input_train']
    new_experiment['output_train'] = train_labels
    new_experiment['input_test'] = experiment['input_test']
    new_experiment['output_test'] = test_labels
    new_experiment['function'] = "1 if the first coordinate is even, 0 else"

    new_input_text = ''
    for ix, line in enumerate(experiment['input_text'].split('\n')):
        if line != '':
            new_input_text += (line[:-1] + str(train_labels[ix]) + '\n')

    new_experiment['input_text'] = new_input_text

    experiments[f'2d_class_type_1_evenodd_rstate_{rs}'] = new_experiment

with open('experiments_log.json', 'w') as file:
    json.dump(experiments, file)
