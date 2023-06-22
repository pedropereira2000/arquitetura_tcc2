from decouple import config
from connection import ElasticConnection
from controllerSmell import extractionSmell
from controllerProject import extractionProject
from model import (smell, project)

econn = ElasticConnection()
econn.connect(
    config('ELASTIC_HOST'),
    config('ELASTIC_USER'),
    config('ELASTIC_PASSWORD')
)

print('Coletando Projects...')
project.Project._index._name = f"index-stag-projects"
extractionProject()

print(f'Coletando Smells...')
smell.Smell._index._name = f"index-stag-smells"
extractionSmell(econn)

