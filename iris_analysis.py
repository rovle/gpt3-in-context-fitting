import json

engines = ['ada', 'babbage', 'curie', 'davinci']
for engine in engines:
    with open('iris_results.json', 'r') as file:
        results = json.loads(file.read())

    accurate = [1 if x==y else 0
            for x, y in zip(results[engine]['gpt_classification'],
                            results['labels'])]

    report = f'{engine} had {100*sum(accurate)/len(accurate)}% accuracy.\n'
    print(report)

    with open('iris_results.txt', 'a') as file:
        file.write(report)


# Also try out KNN and LR

# KNN with k=1, 2, 3, 5, 7

kvals = {1, 3, 5, 7}

for k in kvals:
    pass