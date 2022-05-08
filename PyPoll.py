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
# Open the election results and read the file. 
with open(file_to_load) as election_data:
    #To do: read and analyze the data here. 
    print(election_data)
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data) 
    # Print the header row.
    headers = next(file_reader)
    print(headers)
    




















# Assign a variable to save the file to a path.
file_to_save=os.path.join("analysis","election_analysis.txt")
with open(file_to_save,"w") as txt_file:
    txt_file.write("Counties in the Election\n-------------------\nArapahoe\nDenver\nJefferson") 















