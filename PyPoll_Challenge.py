# Add dependicies
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
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0
# County Votes/ Largest County Turnout
county_votes = {}
county_options = []
largest_county = ''
largest_county_count = 0
largest_county_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:

        # Read the file object witht the reader function.
        file_reader = csv.reader(election_data)

        # Reads and excludes the header row from next loop.
        headers = next(file_reader)

        # Loops through each row in the csv file minus the header row
        for row in file_reader:
            # Add to the total vote count.
            total_votes += 1
            # Candidates names from csv file
            candidate_name = row[2]
            # County name from csv file
            county_name = row[1]
            # Creates dictionary of candidates names and their total votes
            if candidate_name not in candidate_options:

                candidate_options.append(candidate_name)
        
                candidate_votes[candidate_name] = 0

            candidate_votes[candidate_name] += 1
            # Creates dictionary of county names and their total votes
            if county_name not in county_options:

                county_options.append(county_name)
                county_votes[county_name] = 0

            county_votes[county_name] += 1
            

with open(file_to_save, "w") as txt_file:
    #Prints the header Election Results and total votes overall
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f'County Votes:\n'
        f'')
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    # Determines the percentage of votes for each county 
    for county in county_votes:

        votes = county_votes[county]
        county_vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > largest_county_count) and (county_vote_percentage > largest_county_percentage):

            largest_county_count = votes
            largest_county_percentage = county_vote_percentage
            largest_county = county

        county_results = (f'{county}: {county_vote_percentage:.1f}% ({votes:,})\n')

        print(county_results)

        txt_file.write(county_results)

    largest_county_summary = (
        f'\n'
        f'-------------------------\n'
        f'Largest County Turnout: {largest_county}\n'
        f'-------------------------\n')
    print(largest_county_summary)

    txt_file.write(largest_county_summary)


    # Determines the percentage of votes for each candidate by looping through the counts.
    for candidate in candidate_votes:

        votes = candidate_votes[candidate]

        votes_percentage = float(votes) / float(total_votes) * 100
        
        if (votes > winning_count) and (votes_percentage > winning_percentage):
            
            winning_count = votes

            winning_percentage = votes_percentage

            winning_candidate = candidate

        candidate_results = (f'{candidate}: {votes_percentage:.1f}% ({votes:,})\n')

        print(candidate_results)

        txt_file.write(candidate_results)

    winning_candidate_summary = (
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'-------------------------\n')
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)