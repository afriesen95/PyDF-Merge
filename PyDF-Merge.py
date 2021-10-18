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

# Define output folder name and build output folder path
output_folder_name = "PyDF-Merge"
output_folder_path = f"{os.path.dirname(__file__)}\\{output_folder_name}\\"

# Define output file name and build output file path
output_file_name = args.output
output_file_path = f"{output_folder_path}\\{output_file_name}.pdf"

# Create PDF Merger object
merger = PdfFileMerger()

# Append each file
try:
    for x in args.input:
        merger.append(x)
except FileNotFoundError:
    print(
        f'ERROR: \"{x}\" could not be found, double-check the file name and try again.')
    sys.exit()

# Write the finished PDF to a file
merger.write(output_folder_path)
