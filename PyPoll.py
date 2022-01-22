# The data we need to retrieve.
# The total number of votes cast.
# A complete list of candidates who received votes.
# The percentage of votes each candidate won.
# The total number of votes each candidate won.
# The winner of the election based on popular vote.

import csv
import os

# Assign a variable to the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_results.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To read and analyze the data here.
    file_reader = csv.reader(election_data)
    # read and print the header row
    headers = next(file_reader)
    # Print each row from csv file.
    for row in file_reader:
        print(row)

    

