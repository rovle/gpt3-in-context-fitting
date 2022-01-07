from utils import textify_numbers
import json
import random
from inspect import getsource

def generate_regression_experiment(experiments_dict, name, preamble,
                                function, input_train, input_test):
    """
    Generate data for a regression experiment.

    ----------

    Parameters:

    
    """
    if name in experiments_dict.keys():
        raise Exception("An experiment with that name already exists!")
    
    outputs = [function(*point) if hasattr(point, '__iter__')
                else function(point)
                for point in input_train]

    input_text = preamble
    for x, y in zip(input_train, outputs):
        x = textify_numbers(x)
        y = textify_numbers(y)
        input_text += f"Input = {x}, output = {y}\n"
    
    experiments_dict[name] = {
                        "input_train" : input_train,
                        "output_train" : outputs,
                        "input_text" : input_text,
                        "function" : getsource(function),
                        "input_test" : input_test
                        }
    
    with open('experiments_log.json', 'w') as file:
        json.dump(experiments_dict, file)


def generate_classification_experiment(experiments_dict, name, preamble,
                                        sampling_fn, num_train, num_test,
                                        classes):
    """
    Supports only binary & balanced dataset classification.
    """
    num_classes = len(classes)
    if (num_train % num_classes != 0) or (num_test % num_classes != 0):
        raise Exception("Number of classes has to divide train/test sizes.")

    train_class_size = num_train // num_classes
    test_class_size = num_test // num_classes

    x_train = []
    y_train = []
    x_test = []
    y_test = []
    for class_ in classes:        
        x_train += sampling_fn(class_num=class_, size=train_class_size)
        y_train += [class_]*train_class_size

        x_test += (sampling_fn(class_num=class_, size=test_class_size))
        y_test += [class_]*test_class_size

    train = list(zip(x_train, y_train))
    test = list(zip(x_test, y_test))

    random.shuffle(train)
    random.shuffle(test)

    x_train, y_train = zip(*train)
    x_test, y_test = zip(*test)


    input_text = preamble
    for x, y in zip(x_train, y_train):
        x = textify_numbers(x)
        y = textify_numbers(y)
        input_text += f"Input = {x}, output = {y}\n"

    experiments_dict[name] = {
                        "input_train" : x_train,
                        "output_train" : y_train,
                        "input_text" : input_text,
                        "function" : getsource(sampling_fn),
                        "input_test" : x_test,
                        "output_test" : y_test
    }
    with open('experiments_log.json', 'w') as file:
        json.dump(experiments_dict, file)

