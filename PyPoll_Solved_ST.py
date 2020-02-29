import os
import csv
import numpy as np #import this module to compute differential 

#Import raw data
data_csv = os.path.join("Resources", "election_data.csv")

# Counter for total number of votes
total_votes = 0
# Lists to store county, candidate information for each vote
county = []
candidate = []

candidate_list = [] # to compile a list of unique candidate
candidate_votes_list = {} # list of votes by candidates
# class candidate_votes_list:
#     def __init__(candidate, name, age):
#         candidate.name = name
#         candidate.votes = votes

# Open and read csv
with open(data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csvreader:
        #print(row)
        total_votes = total_votes + 1 # Update total votes
        county=row[1]
        candidate=row[2]
        # Add candidate name to unique candidates list if seen for first time
        if candidate not in candidate_list: 
            candidate_list.append(candidate)
            candidate_votes_list[candidate] = 1 #start vote count for candidate
        else:
            candidate_votes_list[candidate] = candidate_votes_list[candidate] + 1 #update vote count for candidate


textfile = open('PyPoll-Results.txt', 'w') #declare output text file and open for editing

print("Here is the list of candidates:"), textfile.write("Here is the list of candidates:\n")
print("-------------------------------"), textfile.write("-------------------------------\n")
for x in candidate_list:
    print(x), textfile.write("%s\n" % x)

# Print Results to screen
print("--------Election Results--------"), textfile.write("--------Election Results--------\n")
print("--------------------------------"), textfile.write("--------------------------------\n")
print(f"Total Votes: {total_votes}"), textfile.write("Total Votes: %d\n" % total_votes)
print("--------------------------------"), textfile.write("--------------------------------\n")

#To compute the breakdown by Candidates and print in descending order

#candidate_votes_list_index = [candidate_votes_list.index(x) for x in sorted(candidate_votes_list)]

# Determine the winner by looping through the counts
candidate_votes_list_sorted = sorted(candidate_votes_list, reverse=True)

print("-------Breakdown of Votes-------"), textfile.write("-------Breakdown of Votes-------\n") 
print("--------------------------------"), textfile.write("--------------------------------\n")
winning_count = 0 #initialize winning number of votes
for candidate in candidate_votes_list:
    # call number of votes and compute % of total votes
    candidate_votes = candidate_votes_list.get(candidate)
    candidate_votes_percentage = float(candidate_votes) / float(total_votes) * 100

    # Determine winning vote count and candidate
    if (candidate_votes > winning_count):
        winning_count = candidate_votes #update winning number of votes
        winning_candidate = candidate #update winning candidate
        winning_candidate_percentage = candidate_votes_percentage #update winning candidate % of votes

    # Print each candidate's voter count and percentage (to terminal)
    # voter_output = f"{candidate}: {vote_percentage:.1f}% ({votes})\n"
    print(f"{candidate}: {candidate_votes_percentage:.2f}% ({candidate_votes})")
    #textfile.write("%s: %.2f%20 (%d)\n" %(candidate,candidate_votes_percentage,candidate_votes))
    textfile.write("%s: %.0f percent of votes (%d)\n" % (candidate,candidate_votes_percentage,candidate_votes))

print("--------------------------------"), textfile.write("--------------------------------\n")
print(f"Winner:{winning_candidate} with {winning_candidate_percentage:.0f}% of votes"), 
textfile.write("Winner:%s with %.0f percent of votes\n" % (winning_candidate,winning_candidate_percentage))
print("--------------------------------"), textfile.write("--------------------------------\n")