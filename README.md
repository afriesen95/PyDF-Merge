# PyDF-Merge
CLI tool for merging PDF files written in Python.

## Installation
1. Download the latest release.
2. Unzip the release, open your terminal of choice in the folder and run ```pip install -r requirements.txt```
3. Move the folder to the root of your drive (it can exist anywhere, so long as you do not move it after it adding to your PATH.)
4. Add the folder to your PATH.

You may need to restart your device at this point.

## Usage
1. Open your terminal of choice to the location of the PDF files to be merged.
2. Use PyDF-Merge as such: ```pdfm [-h] resultFileName pdfToMerge [pdfToMerge ...]```
3. The resulting PDF file will be in ```./PyDF-Merge/<resultFileName>.pdf```
