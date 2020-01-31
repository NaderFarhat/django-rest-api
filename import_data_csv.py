#!/usr/bin/env python

"""
    Script to import book data from .csv file to Model Database DJango
    To execute this script run: 
                                1) manage.py shell
                                2) exec(open('import_data_csv.py').read())
"""

import csv
from events.models import Noc

def run():
    fhand = open('../noc_regions')
    reader = csv.reader(fhand)

    Noc.objects.all().delete()

    for row in reader:
        print(row)

        #p, created = Noc.objects.get_or_create(NOC=row[0])

