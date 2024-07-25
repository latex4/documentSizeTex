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
### Usage example
* how to use the run file?

      files_dir="code/greedy_from_machine/files"
      results_dir="code/~/results"
      x = 0 # the simple algorithm
      # Run experiments with different algorithm variants
      python -u code/greedy_from_machine/new_experiment.py $x $files_dir $results_dir
