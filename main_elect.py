#import
import csv 
from pathlib import Path

#set path to csv
electcsv = Path('../Resources/election_data.csv')
# total votes cast count
tvote = 0
#complete list of canadates
clist = []
#total votes per candidate 
tvotepcan = {}
#winner
winner = ''
wvote = 0
wper = 0
#write results in txt file 
analysis = Path('../Resources/analysis/analysisele.txt')
with open(analysis,'w') as file: 
    file.write('Election Results\n') 
    file.write('-------------------------\n')
#open csv
    with open(electcsv,newline='') as elect:
        csvreader = csv.reader(elect,delimiter=',')
        header = next(csvreader)
        #count votes
        for row in csvreader:
            tvote = tvote + 1
            name = row[2]
            if name not in clist: 
                clist.append(name)
                tvotepcan[name] = 0
            tvotepcan[name] += 1

    #print results in terminal and txt 
    print('Election Results')
    print('-------------------------\n')
    print('Total Votes:' + str(tvote))
    file.write(f'Total Votes:' + str(tvote))
    file.write('\n-------------------------\n')
    print('\n-------------------------\n')
    #printing results and generating percentages
    for name in tvotepcan:
        vote = tvotepcan[name]
        per = (float(vote)/(tvote))*100
        result = (
            f'{name}: {per:.3f}% ({vote:})\n')
        print(result)
        file.write(result)
    # pulling max value from tvotepcan and assigning as winner
    winner = max(tvotepcan, key=tvotepcan.get)
    print('-------------------------\n')
    print(f'Winner: {winner}\n')
    print('-------------------------\n')
    file.write('-------------------------\n')
    file.write(f'Winner: {winner}\n')







