import csv 
from pathlib import Path

electcsv = Path('../Resources/election_data.csv')
# total votes cast count
tvote = 0
#votes
vote = []
#complete list of canadates
clist = []
#total votes/candidate 
tvotepcan = {}
#% votes won/candidate 
per = []
#winner/pop
winner = ''
wvote = 0
wper = 0


with open(electcsv,newline='') as elect:
    csvreader = csv.reader(elect,delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        tvote = tvote + 1
        name = row[2]
        if name not in clist: 
            clist.append(name)
            tvotepcan[name] = 0
        tvotepcan[name] += 1

    # for name in tvotepcan:
    #     vote = tvotepcan.get(name)
    #     per = (float(vote)/float (tvote))*100
    #     result = (
    #         f'{name}: {per:.3f}% ({vote:})\n')


print('Election Results')
print('-------------------------')
for name in tvotepcan:
    vote = tvotepcan.get(name)
    per = (float(vote)/float (tvote))*100
    result = (
        f'{name}: {per:.3f}% ({vote:})\n')
    print(result)
    if (vote > wvote) and (per > wper):
        winner = name
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

# analysis = Path('../Resources/analysis/analysis.txt')
# with open(analysis,'w') as file: 
#     file.write('Financial Analysis\n') 
#     file.write('-------------------------\n')
#     file.write(f'Total Months: {len(tmonth)}\n')
#     file.write(f'Total: ${sum(tprofit)}\n')
#     file.write(f'Average Change: ${round(sum(cprofit)/len(cprofit),2)}\n')
#     file.write(f'Greatest Increase in profits: {tmonth[giprofit]} (${str(giprofitv)})\n')
#     file.write(f'Greatest Decrease in profits: {tmonth[gdprofit]} (${str(gdprofitv)})\n')

