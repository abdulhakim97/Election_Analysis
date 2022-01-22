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

# Initialize a total vote counter.
total_votes = 0

# Initialize a candidates list
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Winning candidate and winning count tracker.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To read and analyze the data here.
    file_reader = csv.reader(election_data)
    # read and print the header row
    headers = next(file_reader)
    # Print each row from csv file.
    for row in file_reader:
        # Add to the total vote count. 
        total_votes = total_votes + 1

        # Print the candidates name from each row.
        candidate_name = row[2]

        # if the candidate does not match in any existing name.
        if candidate_name not in candidate_options:

            #add the candidates name to the List.
            candidate_options.append(candidate_name)

            # Begin tracking the votes
            candidate_votes[candidate_name] = 0

         # Add a vote to that candidates count.
        candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    # Iterate through candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print to the terminal.
        candidate_results= (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine the winning vote count.
        # Determine if the votes is greater than the winning count.
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)