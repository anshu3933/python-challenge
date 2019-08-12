import os
import csv
import pandas as pd
import numpy

votes = -1
candidates = []
winner = ' '
votes_khan = 0
votes_li = 0
votes_correy = 0
votes_otooley = 0

csvpath = os.path.join('election_data.csv')
with open(csvpath, newline = '') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ',')
    for row in csvreader:
        votes = votes + 1
        candidates.append(row[2])
        if row[2] == 'Khan':
            votes_khan = votes_khan + 1
        elif row[2] == 'Correy':
            votes_correy = votes_correy + 1
        elif row[2] == 'Li':
            votes_li = votes_li + 1
        elif row[2] == "O'Tooley":
            votes_otooley = votes_otooley + 1
print('Total votes cast: %d' % votes)
unique_candidates = []
for i in candidates:
    if i not in unique_candidates:
        unique_candidates.append(i)
#print(unique_candidates)
print('Khan received: %d votes' % votes_khan)
print('Correy received %d votes' % votes_correy)
print('Li received %d votes' % votes_li)
print('O Tooley received %d votes' % votes_otooley)
votes_percent = [votes_khan/votes * 100, votes_correy/votes * 100, votes_li/votes * 100, votes_otooley/votes * 100]
print('Candidate percentages:', votes_percent)

with open("results.txt", "w") as f:
   f.write('Election results' + '\n' + '-------------------' + '\n' + 'Total Votes: %d' % votes + '\n' + 'Khan: %d percent : %d' % (votes_percent[0], votes_khan) + '\n' + 'Correy: %d percent : %d' % (votes_percent[1], votes_correy) + '\n' + 'Li: %d percent : %d' % (votes_percent[2], votes_li) + '\n' + "O'Tooley: %d percent : %d" % (votes_percent[3], votes_otooley) + '\n' + 'The winner is Khan' )
   f.close()

