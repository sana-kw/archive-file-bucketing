Archival File Bucketing with Python

Overview
This project demonstrates a Python workflow for generating synthetic archival folder identifiers, creating JPEG filenames, and grouping files by their corresponding folder identifiers. 

It was developed as a programming exercise related to archival metadata organisation.

Objectives
	• Generate 500 unique folder identifiers.
	• Generate 50,000 synthetic JPEG filenames.
	• Group filenames into folders using Python dictionaries.
	• Display a sample of the structured output.

Tools Used
	• Python 3
	• collections.defaultdict

How It Works
	• Generate synthetic folder identifiers.	
	• Create 100 JPEG filenames for each folder.	
	• Extract the folder identifier from each filename.	
	• Store filenames in the corresponding folder bucket.	
	• Print a sample of the results.	

How to Run
Ensure Python 3 is installed, then run:
archive_file_bucketing.py

Scope and Limitations
This project uses synthetic test data. It does not modify an archival database or validate real archival records. Further development could include filename validation, duplicate detection, unmatched-file reporting, and checks against an authorised metadata export.

