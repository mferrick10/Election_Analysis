# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of all canidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote


import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Intitalize a total vote counter.
total_votes = 0
# Candidates options
candidate_options = []
# Candidate name and total votes
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.

        # Read the file object witht the reader function.
        file_reader = csv.reader(election_data)

        # Print the header row.
        headers = next(file_reader)

        # Print each row in the CSV file.
        for row in file_reader:
            # Add to the total vote count.
            total_votes += 1
            # Print candidates names
            candidate_name = row[2]

            if candidate_name not in candidate_options:

                candidate_options.append(candidate_name)
        
                candidate_votes[candidate_name] = 0

            candidate_votes[candidate_name] += 1

# Determines the percentage of votes for each candidate by looping through the counts.
for candidate in candidate_votes:

    votes = candidate_votes[candidate]

    votes_percentage = float(votes) / float(total_votes) * 100
    
    if (votes > winning_count) and (votes_percentage > winning_percentage):
        
        winning_count = votes

        winning_percentage = votes_percentage

        winning_candidate = candidate

    print(f'{candidate}: {votes_percentage:.1f}% ({votes:,})\n')

winning_candidate_summary = (f'--------------------\n'f'Winner: {winning_candidate}\n'f'Winning Vote Count: {winning_count:,}\n'f'Winning Percentage: {winning_percentage:.1f}%\n'f'-------------------\n')
print(winning_candidate_summary)



