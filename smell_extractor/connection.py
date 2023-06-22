'''
Establish a connection to an Elastic instance
'''
import time

from decouple import config
from elasticsearch_dsl import connections

class ElasticConnection:
    def connect(self, host, user, password):
        self.connection = connections.create_connection(
            hosts=[host],
            http_auth=f'{user}:{password}'
        )
    
    def remove(self):
        self.connection = connections.remove_connection(
            "default"
        )

    def index_configuration(issue_object, issue_name):
        issue_object._index._name = f"index-{issue_name}"