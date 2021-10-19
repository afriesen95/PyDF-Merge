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
    description="PyDF-Merge: CLI tool for merging PDF files.")

# Add arguments to the parser
parser.add_argument('output', metavar="resultFileName",
                    help="name of resulting PDF file")
parser.add_argument('input', metavar="pdfToMerge",
                    nargs="+", help="PDF files to merge")

# Parse the arguments
args = parser.parse_args()

# Define output folder name and build output folder path
output_folder_name = "PyDF-Merge"
output_folder_path = f"{os.getcwd()}\\{output_folder_name}"

# Create the output directory
os.makedirs(output_folder_path, exist_ok=True)

# Define output file name and build output file path
output_file_name = args.output if args.output.endswith(
    ".pdf") else args.output + ".pdf"
output_file_path = f"{output_folder_path}\\{output_file_name}"

# Create PDF Merger object
merger = PdfFileMerger()

# Append each file
try:
    for x in args.input:
        pdf = x
        if (not pdf.endswith(".pdf")):
            pdf += ".pdf"

        merger.append(pdf)

# If, for example, a .txt file has been passed in as an argument, it would become "a.txt.pdf" so it is okay to catch it here
except FileNotFoundError:
    print(f"ERROR: \"{x}\" does not exist, is corrupt, or is not a PDF file.")
    sys.exit()

# If the input file was not a PDF file...
except OSError as e:
    if (e.args[0] == 22):
        print(f"ERROR: \"{x}\" is not a valid PDF file.")

# If anything else went wrong...
except Exception:
    print(f"ERROR: an unknown error has occurred, please try again.")
    sys.exit()

# Write the finished PDF to a file
merger.write(output_file_path)
print(f"SUCCESS: {len(args.input)} files were merged to {output_file_path}")
