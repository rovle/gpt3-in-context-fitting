from utils import textify_numbers
import json
import random
from inspect import getsource

def generate_regression_experiment(experiments_dict, name, preamble,
                                function, input_train, input_test):
    """
    Generate data for a regression experiment.

    Takes a dictionary in which to store a regression experiment;
    its name, preamble (text before the input vectors), regression
    function, train and test set (just the "x"s, "y"s are generated
    by the function).

    Note that I was calling this function with the full dictionary
    of previous experiments as the first argument.
    USING THIS FUNCTION IN A 'NAIVE' WAY MIGHT CAUSE LOSS OF DATA.
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
    Generate data for a classification experiment.

    Takes a dictionary in which to store a classification
    experiment; its name, preamble (text before the input
    vectors), sampling function, number of samples in train
    and test dataset, as well as a list of classes.

    Note that I was calling this function with the full dictionary
    of previous experiments as the first argument.
    USING THIS FUNCTION IN A 'NAIVE' WAY MIGHT CAUSE LOSS OF DATA.
    """
    num_classes = len(classes)
    if (num_train % num_classes != 0) or (num_test % num_classes != 0):
        raise Exception("Number of classes has to divide train/test sizes.")

    classes_cardinality = (num_train + num_test) // num_classes
    x = []
    y = []
    for class_ in classes:
        x += sampling_fn(class_num=class_,
                        size=classes_cardinality)
        y += [class_]*(classes_cardinality)

    xy = list(zip(x, y))
    random.shuffle(xy)
    x, y = zip(*xy)

    x_train, y_train = x[:num_train], y[:num_train]
    x_test, y_test = x[num_train:], y[num_train:]


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
    
    #print(experiments_dict[name])
    with open('experiments_log.json', 'w') as file:
       json.dump(experiments_dict, file)

