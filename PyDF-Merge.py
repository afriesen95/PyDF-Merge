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

# Create argument parser object
parser = argparse.ArgumentParser(
    description="Merge PDF files into one.")

# Add arguments to the parser
parser.add_argument('output', metavar="resultFileName",
                    help="name of resulting pdf file")
parser.add_argument('input', metavar="pdfToMerge",
                    nargs="+", help="pdf file to merge")

# Parse the arguments
args = parser.parse_args()

# Create PDF Merger object
# merger = PdfFileMerger()

# Write the finished PDF to a file
# merger.write(output_folder_path)
