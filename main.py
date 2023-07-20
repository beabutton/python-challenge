import csv 
from pathlib import Path

budgetcsv = Path('../Resources/budget_data.csv')
# total months
tmonth = []
#total profit/losses
tprofit = []
#changes in profit.losses
cprofit = []
#greatest increase in profit
giprofit = []
#greatest decrease in profit
gdprofit = []


with open(budgetcsv,newline='') as budget:
    csvreader = csv.reader(budget,delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        tmonth.append(row[0])
        tprofit.append(int(row[1]))
    for i in range(len(tprofit)-1):
        cprofit.append(tprofit[i+1]-tprofit[i]) 

giprofitv = max(cprofit)
gdprofitv = min(cprofit)

giprofit = cprofit.index(max(cprofit))+1
gdprofit = cprofit.index(min(cprofit))+1

print('Financial Analysis')
print('-------------------------')
print(f'Total Months: {len(tmonth)}')
print(f'Total: ${sum(tprofit)}')
print(f'Average Change: ${round(sum(cprofit)/len(cprofit),2)}')
print(f'Greatest Increase in profits: {tmonth[giprofit]} (${str(giprofitv)})')
print(f'Greatest Decrease in profits: {tmonth[gdprofit]} (${str(gdprofitv)})')

analysis = Path('../Resources/analysis/analysis.txt')
with open(analysis,'w') as file: 
    file.write('Financial Analysis\n') 
    file.write('-------------------------\n')
    file.write(f'Total Months: {len(tmonth)}\n')
    file.write(f'Total: ${sum(tprofit)}\n')
    file.write(f'Average Change: ${round(sum(cprofit)/len(cprofit),2)}\n')
    file.write(f'Greatest Increase in profits: {tmonth[giprofit]} (${str(giprofitv)})\n')
    file.write(f'Greatest Decrease in profits: {tmonth[gdprofit]} (${str(gdprofitv)})\n')

