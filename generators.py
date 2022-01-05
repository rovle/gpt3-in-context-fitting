from utils import textify_numbers
import json
from inspect import getsource

def generate_regression_experiment(experiments_dict, name, preamble, function,
                                    input_train, input_test):
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
    
    experiments_dict[name] = {"input_train" : input_train,
                        "output_train" : outputs,
                        "input_text" : input_text,
                        "function" : getsource(function),
                        "input_test" : input_test
                        }
    
    with open('experiments_log.json', 'w') as file:
        json.dump(experiments_dict, file)


def generate_classification_experiment(name, premable, sampling_fn,
                                        num_train, num_test, classes):
    """
    Supports only binary & balanced dataset classification.
    """
    
    pass

