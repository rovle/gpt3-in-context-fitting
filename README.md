# GPT-3 In-context numerical model fitting experiments

This is repository for my experiments on GPT-3's ability to fit numerical models in-context. See the associated [Lesswrong post](https://www.lesswrong.com/posts/c2RzFadrxkzyRAFXa/who-models-the-models-that-model-models-an-exploration-of).

Short descriptions of files in this repository:

|  Notebooks |   |
|---|---|
| classification_playground.ipynb | Classification scenario plotting & Calculating accuracy |
| iris_analysis.ipynb | Calculating accuracy of GPT-3 and kNN/log. reg. on Iris dataset |

|  Python scripts |   |
|---|---|
| generators.py | Functions for generating classification/regression experiments |
| generate_experiment.py | Script in which I called aforementioned functions |
| run_all_experiments.py | Runs all not-yet-run experiments, saves their results |
| iris_test.py | Performes test on the Iris dataset and saves results |
| number_sense_test.py | Experiment in which letters replace numbers |
| number_sense_test_spaced.py  | Same as above, only with spaces between letters |
| text_freq_classifier.py | Tests a hand-coded text frequency classifier |
| even_odd_test.py | Test whether GPT-3 can learn that the second digit is even |
| utils.py | Just a single utility function |

|  R script |   |
|---|---|
| visualizations.R | Visualize stuff in results/ in ggplot2 |

|  Json |   |
|---|---|
| experiments_log.json | Metadata, raw results of all experiments |
