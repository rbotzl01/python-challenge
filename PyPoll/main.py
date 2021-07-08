#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:47:32 2021

@author: ryanp
"""
import os
import csv

csvpath = os.path.join("Resources","election_data.csv")
outpath = os.path.join("Analysis","election_analysis.txt")

#initialize variables
total_votes = 0
candidates = []
vote_cnt = []
max_vote_cnt = 0




with open(csvpath, 'r', newline='') as csvfile:        
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #calculate number of votess  
    for row in csvreader:
        total_votes += 1

        if(row[2] not in candidates):
            candidates.append(row[2])
            vote_cnt.append(0)
        
       
        candidateIndex = candidates.index(row[2])
        vote_cnt[candidateIndex] += 1

    print('Election Results'+'\n')
    print(f"Total votes: {total_votes}")
    
    #loop through candidates and calculate percentage of votes
    #print output to terminal
    for x in range(len(candidates)):
        votePercent = round((vote_cnt[x]/total_votes)*100,3)
        print(f"{candidates[x]}: {votePercent}% ({vote_cnt[x]})")
        #test for highest voted candidate
        if (max_vote_cnt<vote_cnt[x]):
            max_vote_cnt = vote_cnt[x]
            win_cand = candidates[x]
    
    print(f"win_cand: {win_cand}")

file = open(outpath,'w')

#print output to file
file.write("Election Anaylsis\n")
file.write("\nTotal votes:" + str(total_votes))
    
for x in range(len(candidates)):
    votePercent = round((vote_cnt[x]/total_votes)*100,3)
    file.write("\n" + str(candidates[x]) +" : " + str(votePercent) 
                + "% ("+ str(vote_cnt[x]) + ")")
file.write("\nwin_cand: " + str(win_cand))
