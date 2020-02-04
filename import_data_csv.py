"""
    manage.py shell
    exec(open('import_data_csv.py').read())
"""

import csv
from events.models import Comitees, Event, Athlete, Game

CSV_PATH = 'noc_regions.csv' 
CSV_PATH_EVENT = 'athlete_events.csv' 

contSuccess_noc = 0
contSuccess_evt = 0
contSuccess_ath = 0

Comitees.objects.all().delete()
Event.objects.all().delete()
Athlete.objects.all().delete()
Game.objects.all().delete()


with open(CSV_PATH, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    print('Loading...')
    com_list = []
    for row in spamreader:
        if row:
            if row[0] == 'NOC':
                pass
            else:
                print(row[0])
                com = Comitees(
                    noc=row[0],
                    region=row[1],
                    notes=row[2]
                )
                contSuccess_noc += 1
                com_list.append(com)
    Comitees.objects.bulk_create(com_list)
    print(f'{str(contSuccess_noc)} inserted successfully (NOC)! ')

with open(CSV_PATH_EVENT, newline='') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    print('Loading...')
    evt_list = []
    for row in reader:
        if row:
            filterNoc = Comitees.objects.filter(noc=row[7]).values('noc', 'region', 'notes').first()
            Comitees.objects.filter(noc=row[7]).delete()
            if filterNoc is None:
                filterNoc = {'noc': ' ', 'region': ' ', 'notes': ' '}
            if row[0] == 'ID':
                pass
            else:
                print(row[1])
                game = Game(
                    sport=row[12],
                    event=row[13],
                    medal=row[14]
                )
                game.save()
                evt = Event(
                   games=row[8],
                   year=row[9],
                   season=row[10],
                   city = row[11]
                )
                evt.save()
                ath = Athlete(
                    name=row[1],
                    sex =row[2],
                    age=row[3] ,
                    height=row[4],
                    weight=row[5],
                    noc=Comitees.objects.create(noc=filterNoc['noc'], region=filterNoc['region'], notes=['notes']),
                    event=evt,
                    game=game
                )

                ath.save()
                contSuccess_ath += 1
    print(f'{str(contSuccess_ath)} inserted successfully (EVT)! ')


