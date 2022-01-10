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
    rstate = 240
    name = f'2d_class_type_7_small_train_rstate_{rstate}'
    preamble = ""
    classes = [0, 1]
    def sampling_fn(class_num, size):
        var = 200
        rstate = 240
        if class_num == 0:
            mixture1 = np.concatenate((
                                        multivariate_normal.rvs([25, 25], [[var, 0], [0, var]], size=size, random_state=rstate),
                                        multivariate_normal.rvs([75, 75], [[var, 0], [0, var]], size=size, random_state=rstate+1),
                                    ))

            indices = np.random.choice(mixture1.shape[0], 25, replace=False)
            mixture_sample1 = mixture1[indices]
            round_vec = np.vectorize(round)
            sample = round_vec(mixture_sample1)
            return [x.tolist() for x in sample]

    
        if class_num == 1:
            mixture2 = np.concatenate((
                                        multivariate_normal.rvs([75, 25], [[var, 0], [0, var]], size=size, random_state=rstate+2),
                                        multivariate_normal.rvs([25, 75], [[var, 0], [0, var]], size=size, random_state=rstate+3),
                                    ))

            indices = np.random.choice(mixture2.shape[0], 25, replace=False)
            mixture_sample2 = mixture2[indices]
            round_vec = np.vectorize(round)
            sample = round_vec(mixture_sample2)
            return [x.tolist() for x in sample]
    
    generate_classification_experiment(
                                    experiments_dict=experiments,
                                    name=name,
                                    preamble=preamble,
                                    sampling_fn=sampling_fn,
                                    num_train=16,
                                    num_test=32,
                                    classes=[0,1]
                                    )