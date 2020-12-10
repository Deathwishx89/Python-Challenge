#imports
import os
import csv


#make a path that goes to the Data
csvpath = os.path.join('/Users/villa/Desktop/Python-Challenge/PyPoll/Resources/election_data.csv')
                       
#using the csv module open the data files
with open(csvpath) as csv_file:
    election_data = csv.reader(csv_file, delimiter=',')

#now lets set up the names for the colums and rows
    header_row = next(election_data)
#lets make some lists to evaluate the values x
    all_rows = list(election_data)
    lists = list(zip(*all_rows))
    voter_ids = lists[0]
    counties = lists[1]
    candidates = lists[2]

#we should now make a value name to represent the total number of votes
    total_votes = len(voter_ids)
               
#seperate the different candidates 
    unique_candidates = list(set(candidates))
                       
#code that counts each vote and shows us the results for every different candidiate
    def tally_totals(total_votes):
        vote_tally = 0
        for unique_candidate in unique_candidates:
            for candidate in candidates:
                if candidate == unique_candidate:
                    vote_tally += 1
            vote_percentage = vote_tally / total_votes
            print(unique_candidate + ': {:.1%}'.format(vote_percentage) + ' -{:,}'.format(vote_tally))
            vote_tally = 0
#
#calulates and shows the winner!!!!
    def declare_winner():
        highest_votes = 0
        winner = 0
        vote_tally = 0
        for unique_candidate in unique_candidates:
            for candidate in candidates:
                if candidate == unique_candidate:
                    vote_tally += 1
                    if vote_tally > highest_votes: 
                        highest_votes = vote_tally
                        if highest_votes == vote_tally:
                            winner = unique_candidate
            vote_tally = 0
        print(f'Winner:{winner}')
#the summary of the election
    dash_line = '_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ '
    
    print(f'{dash_line}') 
    print(f'Election Results')
    print(f'{dash_line}')
    print('Total Votes:{:,}'.format(total_votes))   
    print(f'{dash_line}')
    tally_totals(total_votes)
    print(f'{dash_line}')   
    declare_winner()
    print(f'{dash_line}')  
    
          
#now lets make a fie that contains the summary for the election in the same folder
    print(f'{dash_line}', file=open("election_summary.txt","w"))
    print(f'Election Results',file=open("election_summary.txt","a"))
    print(f'{dash_line}', file=open("election_summary.txt","a"))
    print('Total Votes:{:,}'.format(total_votes), file=open("election_summary.txt","a"))
    print(f'{dash_line}', file=open("election_summary.txt","a"))        
    print(f'{dash_line}', file=open("election_summary.txt","a"))        
          
          