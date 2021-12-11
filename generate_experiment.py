from io import TextIOBase
import json
from inspect import getsource
from json.decoder import JSONDecodeError
import os
from scipy.stats import norm
import random
import numpy as np


with open('experiments_log.json', 'r+') as file:
    file_contents = file.read()
    if len(file_contents) == 0:
        experiments = dict()
    else:
        experiments = json.loads(file_contents)


def textify_numbers(nums):
    if hasattr(nums, '__iter__'):
        input = ', '.join(map(str, nums))
    else:
        input = str(nums)
    return nums

def generate_regression_experiment(name, preamble, function,
                                    input_train, input_test):
    """
    Generate data for a regression experiment.

    ----------

    Parameters:

    
    """
    if name in experiments.keys():
        raise Exception("An experiment with that name already exists!")
    
    outputs = [function(*point) if hasattr(point, '__iter__')
                else function(point)
                for point in input_train]

    input_text = preamble
    for x, y in zip(input_train, outputs):
        x = textify_numbers(x)
        y = textify_numbers(y)
        input_text += f"Input = {x}, output = {y}\n"
    
    experiments[name] = {"input_train" : input_train,
                        "output_train" : outputs,
                        "input_text" : input_text,
                        "function" : getsource(function),
                        "input_test" : input_test
                        }
    
    with open('experiments_log.json', 'w') as file:
        json.dump(experiments, file)

def generate_classification_experiment(name, premable, class_generators)


if __name__=='__main__':
    name = 'sine_input_30'
    preamble = ('This is a sequence of inputs and outputs of a function'
                ' which takes an integer as an argument and returns an'
                ' integer.\n')
    input_train = random.sample(range(30, 70+1), k=30)
    def function(x):
        x = 2*x + 50*np.sin(x/3) + norm.rvs(loc=0, scale=15,
                                        size=1, random_state=None)[0]
        x = round(x)
        return x
    input_test = random.sample([x for x in range(1, 99+1)
                                if x not in input_train], k=40)
    generate_regression_experiment(name=name,
                        function=function,
                        preamble=preamble,
                        input_train=input_train,
                        input_test=input_test)