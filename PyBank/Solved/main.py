import os
import csv

bank_path = os.path.join('..','Resources','budget_data.csv')

mnth = []
pl = []
chng = []
cmnth = 0
spl = 0
avg = 0
maxmonth = ''
minmonth = ''

with open(bank_path,newline='') as bankcsv:
    bankreader = csv.reader(bankcsv)

    bankheader = next(bankreader)

    n = 867884

    for row in bankreader:
        mnth.append(row[0])
        pl.append(row[1])
        change = int(row[1]) - n
        chng.append(change)
        n = int(row[1])

data = zip(mnth,pl,chng)

newbank = os.path.join('..','Resources','new_bank_data.csv')

with open(newbank,'w',newline='') as nbankcsv:
    writer = csv.writer(nbankcsv)

    writer.writerow(['Date','Profit/Losses','Change'])

    writer.writerows(data)

with open(newbank) as rbankcsv:
    reader = csv.reader(rbankcsv)

    header = next(reader)

    average = 0

    for row in reader:
        cmnth = cmnth + 1
        spl = spl + int(row[1])
        average = average + int(row[2])
        if row[2] == max(chng):
            print(row[0])
        elif row[2] == min(chng):
            print(row[0])
    avg = average/(cmnth - 1)

print('Financial Analysis')
print('-------------------')
print(f'Total Months: {cmnth}')
print(f'Total: ${spl}')
print(f'Average Change: ${avg}')
print(f'Gratest increase in Profits: {maxmonth} (${max(chng)})')
print(f'Gratest decrease in Profits: {minmonth} (${min(chng)})')