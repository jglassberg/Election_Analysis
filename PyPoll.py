#Retrieve data
#Review data
#Write down all the names of the candidates
#Add a vote count for each candidate
#Get the total votes for each candidate
#Get the total votes for the election


# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")

# 1. Initialize a otal vote counter.
total_votes=0

# Candidate options
candidate_options = []

#Create dictionary
candidate_votes={}

# Winning candidate & winning count.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file. 
with open(file_to_load) as election_data:
    
    #To do: read and analyze the data here. 
    print(election_data)
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data) 
    
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        total_votes +=1
        # Print candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Track vote count
            candidate_votes[candidate_name]=0
        
        # Add a vote that candidate's count.
        candidate_votes[candidate_name]+=1

    #3. Print the candidate list.
    print(candidate_votes)    

    #4. Vote percentage
    for candidate_name in candidate_votes:
        votes=candidate_votes[candidate_name]
        vote_percentage=float(votes)/float(total_votes)*100
        #print(f"{candidate_name}:received {vote_percentage:.1f}% of the vote.")

        print(f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")
        # Detmine winning vote count and candidate
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count=votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary) 




















# Assign a variable to save the file to a path.
file_to_save=os.path.join("analysis","election_analysis.txt")
with open(file_to_save,"w") as txt_file:
    txt_file.write("Counties in the Election\n-------------------\nArapahoe\nDenver\nJefferson") 















