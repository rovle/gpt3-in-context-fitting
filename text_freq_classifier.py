import json
from collections import defaultdict
from statistics import mean
experiment_names = [f'2d_class_type_{x}_rstate_' for x in range(1,10)]

results = dict()

rstates = ['42', '55', '93']
with open('experiments_log.json', 'r') as file:
    experiments = json.loads(file.read())


ukupno = 0

accuracies2 = []
for name in experiment_names:
    accuracies = []
    for rstate in rstates:
        experiment = experiments[name + rstate]
        train = experiment['input_train']
        labels = experiment['output_train']
        train_reduced = []
        for it in train:
            x, y = it
            x, y = x // 10, y // 10
            train_reduced.append([x,y])
        
        test_reduced = []
        test = experiment['input_test']
        for it in test:
            x, y = it
            x, y = x // 10, y // 10
            test_reduced.append([x,y])

        predictions = []
        for it in test_reduced:
            class_ = defaultdict(int)
            x, y = it
            for ix, itt in enumerate(train_reduced):
                xx, yy = itt
                if xx == x:
                    class_[labels[ix]] += 1
                if yy == y:
                    class_[labels[ix]] +=1
            if class_[0] > class_[1]:
                predictions.append(0)
            else:
                predictions.append(1)
        accurate = [1 if x==y else 0
                    for x, y in zip(predictions, experiment['output_test'])]
        accuracies.append(sum(accurate)/len(accurate))
    print(name, mean(accuracies))
    accuracies2.append(mean(accuracies))

print(mean(accuracies2))