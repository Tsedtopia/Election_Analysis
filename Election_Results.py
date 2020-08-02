#!/usr/bin/env python
# coding: utf-8

# In[11]:


# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("./election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("election_analysis.txt")


# In[14]:


# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# Open file
with open(file_to_load) as election_results:
    file_reader=csv.reader(election_results)
    
    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in CSV file.
    for row in file_reader:
        #2. Add to the total vote count.
        total_votes += 1
        
        # Print the candidate name from each row.
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
        
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
        
# Print the candidate list And vote dictionary.
print(candidate_options)
        
#3. Print the total votes.
print(total_votes)
print(candidate_votes)


# Initialize a total county counter
total_county = 0

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

# Open file 
with open(file_to_load) as election_results:
    file_reader=csv.reader(election_results)
    
    # Read the header row
    headers = next(file_reader)
    
    #Print each row in csv file.
    for row in file_reader:
        #2. Add to the total counties list AND counties votes
        total_county +=1
        
        # Print the counties name from each row.
        county_name = row [1]
        
        
        if county_name not in county_options:
            
            # Add the counties name to the list.
            county_options.append(county_name)
            
# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# In[40]:


# 2: Track the largest county and county voter turnout.
county_options = []
county_name ={}


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_results:
    reader = csv.reader(election_results)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:
        # Add to the county voter turnout
        total_votes = total_votes + 1

        # Get the county name from each row.
        county_name = row[1]
        
        # 3: Extract the county name from each row.
        for county_dict in voting_data:
                print(county_dict['county'])

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if county_name not in county_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[county_name] = 0

        # List votes by county name
        county_name[county_votes]+=1

        # 4a: Write a decision statement that checks the largest county turnout 
        
        
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_vote.append(count_name)

            # 4c: Begin tracking the county's vote count.
            county_vote[county_name]=0

        # 5: Add a vote to that county's vote count.
            county_vote[county_name]+=1

# Print the largest county and country voter turnout
print(county_vote)


# In[36]:


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

  

    # 6a: Write a repetition statement to get the county from the county dictionary.

        # 6b: Retrieve the county vote count.
        votes = county_votes.get(county_name)
        vote_percentage = float(county_votes) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # 6c: Calculate the percent of total votes for the county.


         # 6d: Print the county results to the terminal.
            print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write a decision statement to determine the winning county and get its vote count.
            if(total votes >)
                county_name = votes
                total_votes = Election_results
                county_votes = Election_results

    # 7: Print the county with the largest turnout to the terminal.
    

    # 8: Save the county with the largest turnout to a text file.
    
  # Print the final vote count by county (to terminal)
    election_results = (
        f"-------------------------\n"
        f"County Votes:{county_votes}\n")
        f"Total Votes: {total_votes:,}\n"
         f"\nElection Results percentage: {election_percentage} %\n"
        f"-------------------------\n\n"
    print(election_results, end="")

    txt_file.write(election_results)
    

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)


# In[ ]:




