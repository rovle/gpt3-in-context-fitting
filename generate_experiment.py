import json
from scipy.stats import norm, multivariate_normal
import random
import numpy as np
from generators import (
    generate_regression_experiment,
    generate_classification_experiment
)

with open('experiments_log.json', 'r+') as file:
    file_contents = file.read()
    if len(file_contents) == 0:
        experiments = dict()
    else:
        experiments = json.loads(file_contents)


if __name__=='__main__':

    name = 'simple_linearly_separable_2d_classification'
    preamble = ""
    classes = [0, 1]
    def sampling_fn(class_num, size):
        if class_num == 0:
            return multivariate_normal.rvs(mean=[50, 40],
                                            cov=[[160, 0], [0, 80]], 
                                            size=size)
        if class_num == 1:
            return multivariate_normal.rvs(mean=[50, 60],
                                            cov=[[80, 0], [0, 160]], 
                                            size=size)

    generate_classification_experiment(name=name,
                                    preamble=preamble,
                                    sampling_fn=sampling_fn,
                                    num_train=50,
                                    num_test=30,
                                    classes=[0,1])
           
