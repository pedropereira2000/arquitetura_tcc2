import csv
import glob
import time
from decouple import config
from mapper.mapperSmell import SmellMapper
from model.smell import Smell

def extractionSmell(econn):
    cont = 0
    ids = 0
    for path in glob.glob(f"{config('PATH_TO_CSV')}*smells.csv"):
        with open(path, newline='') as csvfile:
            csvReader = csv.reader(csvfile, delimiter=',', quotechar='|')
            archive = ((csvfile.name).split('\\')[len((csvfile.name).split('\\'))-1]).split('-')
            category = ''
            owner = ''
            for key in archive:
                if key == archive[len(archive)-1]:
                    category = archive[len(archive)-1].split('.')[0]
                elif len(archive) > 2 and owner != '':
                    owner = f'{owner}-{key}'
                else:
                    owner = f'{key}'
            for row in csvReader:
                try:
                    if cont >= 50000:
                        econn.remove()
                        print('awiting 5 minutes for restart loop...')
                        time.sleep(60*5)
                        econn.connect(
                            config('ELASTIC_HOST'),
                            config('ELASTIC_USER'),
                            config('ELASTIC_PASSWORD')
                        )
                        cont = 0
                    else:
                        if row[0] == 'version' or row[0] == 'date' or row[0] == 'project':
                            continue
                        print('Smell adding')
                        smell = Smell()
                        mapper = SmellMapper()
                        mapper.map(row, smell, owner, category)
                        smell.save(refresh=True)
                        cont+=1
                except Exception as e:
                    print(e)
                    time.sleep(60*3)


                    