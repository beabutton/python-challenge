#import
import csv, statistics 
from pathlib import Path

#set path to csv
budgetcsv = Path('../Resources/budget_data.csv')
## make empty lists for storing data 
# total months
tmonth = []
#total profit/losses
tprofit = []
#greatest increase in profit
giprofit = []
#greatest decrease in profit
gdprofit = []
#month change
monchange = []
#mon-mon change
mmc = []

#open csv reader
with open(budgetcsv,newline='') as budget:
    #sets deliniter to seperate data
    csvreader = csv.reader(budget,delimiter=',')
    #start past header
    header = next(csvreader)
    #interates rows after header
    for row in csvreader:
        # append total month and profit to empty lists declared above
        tmonth.append(row[0])
        tprofit.append(int(row[1]))
    #monthly changes
    for i in range(len(tprofit) - 1):
        monchange = (tprofit[i + 1] - tprofit[i])
        mmc.append(monchange)
    avc = statistics.mean(mmc)

#generate min and max for greatest increase and decrease
giprofitv = max(mmc)
gdprofitv = min(mmc)

#add min and max to corresponding month
giprofit = mmc.index(max(mmc)) + 1
gdprofit = mmc.index(min(mmc)) + 1

#print in terminal results
print('Financial Analysis')
print('-------------------------')
print(f'Total Months: {len(tmonth)}')
print(f'Total: ${sum(tprofit)}')
print(f'Average Change: $' + str(round(avc, 2)))
print(f'Greatest Increase in profits: {tmonth[giprofit]} (${str(giprofitv)})')
print(f'Greatest Decrease in profits: {tmonth[gdprofit]} (${str(gdprofitv)})')

#print in txt file results stored in folder within resources
analysis = Path('../Resources/analysis/analysis.txt')
with open(analysis,'w') as file: 
    file.write('Financial Analysis\n') 
    file.write('-------------------------\n')
    file.write(f'Total Months: {len(tmonth)}\n')
    file.write(f'Total: ${sum(tprofit)}\n')
    file.write(f'Average Change: $' + str(round(avc, 2)))
    file.write(f'Greatest Increase in profits: {tmonth[giprofit]} (${str(giprofitv)})\n')
    file.write(f'Greatest Decrease in profits: {tmonth[gdprofit]} (${str(gdprofitv)})\n')

