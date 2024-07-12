## Script: run

### Description

This is the main script that sets up the necessary directories and runs the `new_experiment.py` script multiple times with different parameters.

## Script: new_experiment.py
### Parameters
* x: Determines which greedy algorithm to run.
* pdf_tex_files_dir: Directory containing the necessary input files.
* dir_to_results: Directory where the results will be stored.
### Algorithm Types
* 0 -> simple greedy algorithm
* 1 -> heuristic greedy algorithm
* 3 -> classification model greedy algorithm
* 5 -> regression model greedy algorithm
* 7 -> classification and regression model greedy algorithm
### Functionality
Depending on the value of x, a different greedy algorithm experiment is run. The following code snippet from new_experiment.py explains the mapping of x values to the corresponding experiments:
