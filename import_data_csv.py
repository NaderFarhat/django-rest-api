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
# Remove all data from Table
Noc.objects.all().delete()
Events.objects.all().delete()

with open(CSV_PATH, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    print('Loading...')
    Noc.objects.create(
        noc=row[0],
        region=row[1],
        notes=row[2]
    )
        contSuccess_noc += 1
    print(f'{str(contSuccess_noc)} inserted successfully (NOC)! ')

with open(CSV_PATH_EVENT, newline='') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    print('Loading...')
    for row in reader:
        if row:
            filterNoc = Noc.objects.filter(noc=row[7]).values('noc', 'region', 'notes').first()
            #N = Noc.objects.create(noc=filterNoc['noc'], region=filterNoc['region'], notes=['notes'])
            if row[0] == 'ID':
                pass
            else:
                print(row[0])
                print(row[1])
                print(row[2])
                print(row[3])
                print(row[4])
                print(row[5])
                print(row[6])
                print(row[7])
                print(row[8])
                print(row[9])
                print(row[10])
                print(row[11])
                print(row[12])
                print(row[13])
                print(row[14])
                Events.objects.create(
                    identification=row[0],
                    name=row[1],
                    sex=row[2],
                    age=row[3],
                    height=row[4],
                    weight=row[5],
                    team=row[6],
                    noc=Noc.objects.create(noc=filterNoc['noc'], region=filterNoc['region'], notes=['notes']),
                    games=row[8],
                    year=row[9],
                    season=row[10],
                    city=row[11],
                    sport=row[12],
                    event=row[13],
                    medal=row[14]
                )



