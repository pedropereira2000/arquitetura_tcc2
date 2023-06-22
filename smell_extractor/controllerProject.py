import csv
import glob
from decouple import config
from mapper.mapperProject import ProjectMapper
from model.project import Project

def extractionProject(econn):
    for path in glob.glob(f"{config('PATH_TO_CSV')}*projects.csv"):
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
                if row[0] == 'version' or row[0] == 'date' or row[0] == 'project':
                    continue
                proj = Project()
                print('project adding')
                mapper = ProjectMapper()
                mapper.map(row, proj, owner, category)
                proj.save(refresh=True)

