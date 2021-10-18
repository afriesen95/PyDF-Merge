#######################################################
# PyDF-Merge
# Author: Alexander Friesen
# Created: October 18th, 2021
# Description: CLI tool for merging PDF files.
#######################################################

import argparse
import os
import sys
from PyPDF2 import PdfFileMerger

# Define output folder name and build output folder path
output_folder_name = "output"
output_folder_path = f"{os.path.dirname(__file__)}\\{output_folder_name}\\"

# Define output file name and build output file path
output_file_name = "result.pdf"
output_file_path = f"{output_folder_path}\\{output_file_name}"

# Create Argument Parser object
parser = argparse.ArgumentParser(
    description="Merge two or more PDF files into one.")

# Create PDF Merger object
merger = PdfFileMerger()

# Write the finished PDF to a file
merger.write(output_folder_path)
