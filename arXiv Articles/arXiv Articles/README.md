# arXiv Articles

This directory contains a collection of scripts for downloading, processing, and modifying LaTeX files from arXiv, specifically those related to AAAI conference papers. It also contains the papers we used for the testset (arxiv_testset) after downloading it from arxiv.org and have the process of modify the paper to be ready for our algorithms.





## Scripts and Usage
### 1. Download Papers from arXiv-Script: download_papers.py

This script searches for the most recent articles related to the keyword "AAAI" on arXiv and downloads them.

### 2. addRows : 
Our goal is to modify the paper to have 3 lines on the last page on the left column.

    1. we add \clearpage to the latex file right before the \bibliography using "add_clearpage_before_bibliography"
    
    2. we compile the latex file with the clear page using "compile_latex_to_pdf"
    
    3. while the number of lines is not 3 we:
    
       1. find the page number that is right before the bibliography using "find_page_number_before_bibliography" (IMPORTANT: the page
       number starts from 0)
       
       2. we count the lines in the page (IMPORTANT: use pdfplumber and not fitz) using "count_lines_in_page"
       
       3. according to number of lines we will add or remove lines
       
          1. if the number is 3 exit
          
          2. if we have more than 66 lines then the right column has text and we would like to add until we have 3 lines in a new page,
          in order to compile as less as possible we will add lines132-number of lines because 132 is the number of lines
          in a full pdf page
          
          3. if we have less than 3 lines we need to add one line 
          
          4. if we have less than 66 than we need to remove the number of lines -3 
          
       4. compile again to check changes 
   
### 3. Script: main.py

This script extracts tar.gz files, processes LaTeX files to remove certain commands, and adds extra lines to the last page of the document. It then moves the processed directories to the results directory.

### 4. Additional Scripts
* dir_findTEX.py: Finds the main .tex file in a given directory.
* extract_2_last_pages.py: Extracts the last two pages from a PDF and the preamble from a .tex file.
* Vspace_delete.py: Modifies LaTeX commands by commenting out \vspace, \pdfinfo, and \newpage commands.


### 5. arxiv_testset
The arxiv_testset directory contains all the downloaded and processed papers from arXiv. Each paper has its own directory with the following structure:

* <paper_directory>/
* main_changed.tex: The modified LaTeX file after processing, which includes the removal and commenting out of certain LaTeX commands and 3 lines.
* main_changed.pdf: The PDF file of the paper after modified.

# Example Workflow
## Download Papers:
 First, run the download_papers.py script to download relevant papers from arXiv.
## Process Papers:
 Next, run the main.py script to extract and process the downloaded papers.
