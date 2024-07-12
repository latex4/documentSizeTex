# LaTeX-Paper-Reduction

This repository contains the main folders:
1. documents_generations - contains the files used for generating our 300000+ documents
2. operators - contains the files used for performing operators on our generated documents
3. modelling - contains the files we used to create the tests we showed in our paper
4. second_experiment_ - contains the files used to create the 2nd test in our paper
5. arXiv Articles- contains the script files to download the real papers from arXiv, process them to be ready for our testset, and a directory of the actual arXiv articles after this process, we used in our testset.
6. greedy - The code we used for the paper reduction, contains the process of feature extraction, activating operators, and the algorithms we used in order to reduce the paper length.
7. Article Reduction Outcomes - The results of the shortened papers for each algorithm, contains the files of the pdf after using each operator, and also the csv results for each algorithm and statistics. 

here is the list of python libraries we used in order to generate the documents, perform the operators and perform the tests on different models and architectures:
1. to compile the generated latex code we used **tectonic** which uses the latex compiler **XeLaTeX**
2. to analyze the generated pdfs from our generated latex code we used **pdfminer** and **pdfplumber**, we also used these libraries to map objects from pdf files to their corresponding latex files.
3. to create 300000 random unique latex files we used the libraries **essential_generators** (this libarary helps us create random texts) and **Random** and **Itertools**
4. we used **Numpy** and **pandas** for Dataframes and arrays
5. we used **scikit-learn** for the models we tested and we separated our dataset into train and test using **scikit-learn** too

