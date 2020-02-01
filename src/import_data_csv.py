"""
    1) manage.py shell
    2) exec(open('import_data_csv.py').read())
"""

import csv
from events.models import Comitees, Event

CSV_PATH = '../noc_regions.csv' 
CSV_PATH_EVENT = '../athlete_events.csv' 

contSuccess_noc = 0
contSuccess_evt = 0

Comitees.objects.all().delete()
Event.objects.all().delete()

with open(CSV_PATH, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    print('Loading...')
    for row in spamreader:
        if row:
            if row[0] == 'NOC':
                pass
            else:
                print(row[0])
                Comitees.objects.create(
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
            filterNoc = Comitees.objects.filter(noc=row[7]).values('noc', 'region', 'notes').first()
            if filterNoc is None:
                filterNoc = {'noc': ' ', 'region': ' ', 'notes': ' '}
            if row[0] == 'ID':
                pass
            else:
                Event.objects.create(
                    identification=row[0],
                    name=row[1],
                    sex=row[2],
                    age=row[3],
                    height=row[4],
                    weight=row[5],
                    team=row[6],
                    noc=Comitees.objects.create(noc=filterNoc['noc'], region=filterNoc['region'], notes=['notes']),
                    games=row[8],
                    year=row[9],
                    season=row[10],
                    city=row[11],
                    sport=row[12],
                    event=row[13],
                    medal=row[14]
                )
                contSuccess_evt += 1
    print(f'{str(contSuccess_evt)} inserted successfully (EVT)! ')


