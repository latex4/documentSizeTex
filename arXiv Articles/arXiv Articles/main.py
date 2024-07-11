from dir_findTEX import find_tex_file
from Vspace_delete import *
import os
from addRows import *
import shutil
import time
import func_timeout
import sys
from multiprocessing import Process
sys.path.append(r'code\\greedy_from_machine')

from Last_2_pages_rows_extract import check_invalid_chars


def create(sub_path, destination_path):
    create_new_pdf(sub_path)
    move_changed_pdfs(sub_path, destination_path)
    

def create_wrapper(subdirectory_path, destination_path, timeout, process_id):
    try:
        func_timeout.func_timeout(timeout=timeout, func=create, args=[subdirectory_path, destination_path])
    except func_timeout.exceptions.FunctionTimedOut:
        print(f"Timeout occurred for process {process_id}. Terminating...")
        os.system("TASKKILL /F /PID {pid} /T".format(pid=os.getpid())) 
        shutil.move(subdirectory_path, "new_papers_creation/failed_directories")# Terminate the process
    except Exception as e:
        print(f"An error occurred: {e}, the directory: {subdirectory_path} was not created")
        shutil.move(subdirectory_path, "new_papers_creation/failed_directories")
    finally:
        print(f"Processing for directory {subdirectory_path} completed.")


def loop_through_directories(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for directory in dirs:
            subdirectory_path = os.path.join(root, directory)
            print("now in directory: --------------------------------: ", subdirectory_path)
            
            # Use multiprocessing to run create function in a separate process
            process = Process(target=create_wrapper, args=[subdirectory_path, "new_papers_creation/results", 120, os.getpid()])
            process.start()
            process.join()  # Wait for the process to complete or timeout
            if process.is_alive():
                print(f"Process {process.pid} exceeded the timeout. Terminating...")
                process.terminate()
                process.join()  # Ensure the process is terminated before continuing
 

def create_new_pdf(directory_path):
    tex_file_path = find_tex_file(directory_path)
    if tex_file_path != None :
        if has_aaai_format(tex_file_path):
            # create a new file with the same name as the original file, but with the suffix '_changed' and the same content as the original file.
            new_file_name = os.path.splitext(os.path.basename(tex_file_path))[0] + "_changed.tex"
            new_file_path = os.path.join(directory_path, new_file_name)
            check_invalid_chars(tex_file_path)
            with open(tex_file_path, 'r', encoding="utf-8") as original_file:
                content = original_file.read()
            with open(new_file_path, 'w', encoding="utf-8") as new_file:
                new_file.write(content)        
            # comment the vspace lines (delete the vspace command and add a comment sign before it)
            remove_pdfinfo_commands(new_file_path)
            comment_vspace_lines(new_file_path)
            remove_new_page_command(new_file_path)
            # remove_small_command(new_file_path)
            # add 3 lines to the last page
            create_extra_line_page(new_file_path)

            
            # comment_vspace_lines(tex_file_path)

        else:
            print("No aaai format found in the .tex file")
            # raise Exception("No aaai format found in the .tex file")
            raise Exception("No aaai format found in the .tex file")
    else:
        print("No .tex file found")
        raise Exception("No .tex file found")

def move_changed_pdfs(directory_path, destination_path):
    # move directory to destination path
    shutil.move(directory_path, destination_path)


import os
import tarfile
import shutil
import glob


def extract_tar(tar_file, extract_path):
    with tarfile.open(tar_file, 'r:gz') as tar:
        tar.extractall(extract_path)


def process_tar_files(input_directory, output_directory):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Get a list of all files with the pattern "title.tar.gz" in the input directory
    tar_files = glob.glob(os.path.join(input_directory, '*.tar.gz'))
    index=0
    for tar_file in tar_files:
        try:
            if index==200:
                break
            # Create a directory with a unique name based on the tar file's base name
            base_name, _ = os.path.splitext(os.path.splitext(os.path.basename(tar_file))[0])
            extract_path = os.path.join(output_directory, base_name)
            os.makedirs(extract_path, exist_ok=True)

            # Extract tar.gz file into the created directory
            extract_tar(tar_file, extract_path)

            # Delete the tar.gz file after extraction
            os.remove(tar_file)
            index+=1
        except Exception as e:
            os.remove(tar_file)
            print(f"Error: {e}")
            continue

    # Now you can perform any additional processing on the extracted directories


if __name__ == "__main__":
    # List of gzipped tar files
    
    input_directory = "new_papers_creation\\tar_files"
    # Output directory where all the extracted directories will be placed
    output_directory = "new_papers_creation\\All_Directories"
    # Process the tar files and run the custom function
    #process_tar_files(input_directory, output_directory)
    loop_through_directories(output_directory)



