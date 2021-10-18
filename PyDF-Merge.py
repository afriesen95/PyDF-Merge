#######################################################
# PyDF-Merge
# Author: Alexander Friesen
# Created: October 18th, 2021
# Description: CLI tool for merging PDF files.
#######################################################

import os
from PyPDF2 import PdfFileMerger

output_folder_name = "output"
output_folder_path = f'{os.path.dirname(__file__)}\\{output_folder_name}\\'

print(output_folder_path)
