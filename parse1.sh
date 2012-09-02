#!/bin/sh
# Convert all pdfs in the current directory to text.

# Doesn't work on files with spaces
for file in *.PDF;
  do
  pdftotext $file
done
