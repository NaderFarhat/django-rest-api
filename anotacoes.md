"""
    Script to import book data from .csv file to Model Database DJango
    To execute this script run: 
                                1) manage.py shell
                                2) exec(open('import_data_csv.py').read())
"""

import csv
from events.models import Noc, Events

CSV_PATH = '../noc_regions.csv'      # Csv file path 
CSV_PATH_EVENT = '../athlete_events.csv'      # Csv file path   

contSuccess_noc = 0
contSuccess_athletes = 0
# Remove all data from Table
Noc.objects.all().delete()
Events.objects.all().delete()

with open(CSV_PATH, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    print('Loading...')
    for row in spamreader:
        Noc.objects.create(
            noc=row[0],
            region=row[1],
            notes=row[2]
        )
        contSuccess_noc += 1
    print(f'{str(contSuccess_noc)} inserted successfully (NOC)! ')

with open(CSV_PATH_EVENT, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    print('Loading...')
    for row in spamreader:
        #filterNoc = Noc.objects.filter(noc=row[7]).values('noc', 'region', 'notes').first()
        #N = Noc.objects.create(noc=filterNoc['noc'], region=filterNoc['region'], notes=['notes'])
        #print(N)


"""     Events.objects.create(
            identification=row[0],
            name=row[1],
            sex=row[2],
            age=row[3],
            height=row[4],
            weight=row[5],
            team=row[6],
            noc=n,
            games=row[8],
            year=row[9],
            season=row[10],
            city=row[11],
            sport=row[12],
            event=row[13],
            medal=row[14]
        )
        contSuccess_athletes += 1
    print(f'{str(contSuccess_athletes)} inserted successfully (Athletes)! ') """