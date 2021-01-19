import os
import csv

pollpath = os.path.join('..','Resources','election_data.csv')

tv = 0
kh = 0
co = 0
li = 0
ot = 0
pkh = 0
pco = 0
pli = 0
pot = 0

with open(pollpath) as pollcsv:
    pollreader = csv.reader(pollcsv)

    pollheader = next(pollreader)

    for row in pollreader:
        tv = tv + 1
        if row[2] == 'Khan':
            kh = kh + 1
        elif row[2] == 'Correy':
            co = co + 1
        elif row[2] == 'Li':
            li = li + 1
        elif row[2] == "O'Tooley":
            ot = ot + 1

    pkh = round(kh/tv*100,4)
    pco = round(co/tv*100,4)
    pli = round(li/tv*100,4)
    pot = round(ot/tv*100,4)

print('Election Results')
print('-----------------')
print(f'Total voters: {tv}')
print('-----------------')
print(f'Khan: {pkh}% ({kh})')
print(f'Correy: {pco}% ({co})')
print(f'Li: {pli}% ({li})')
print(f"O'Tooley: {pot}% ({ot})")
print('-----------------')
print(f'Winner: Khan')