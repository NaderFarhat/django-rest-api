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

with open(CSV_PATH, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    print('Loading...')
    for row in spamreader:
        Noc.objects.create(noc=row[0], region=row[1], notes=row[2])
        contSuccess_noc += 1
    print(f'{str(contSuccess_noc)} inserted successfully (NOC)! ')


