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

    name = f'2d_class_type_2_rstate_93'
    preamble = ""
    classes = [0, 1]
    def sampling_fn(class_num, size):
        if class_num == 0:
            sample = multivariate_normal.rvs(mean=[40, 50],
                                            cov=[[80, 0], [0, 160]], 
                                            size=size,
                                            random_state=93)
            round_vec = np.vectorize(round)
            sample = round_vec(sample)
            return [x.tolist() for x in sample]
    
        if class_num == 1:
            sample = multivariate_normal.rvs(mean=[60, 50],
                                            cov=[[160, 0], [0, 80]],
                                            size=size,
                                            random_state=94)
            round_vec = np.vectorize(round)
            sample = round_vec(sample)
            return [x.tolist() for x in sample]
    
    generate_classification_experiment(
                                    experiments_dict=experiments,
                                    name=name,
                                    preamble=preamble,
                                    sampling_fn=sampling_fn,
                                    num_train=50,
                                    num_test=30,
                                    classes=[0,1]
                                    )