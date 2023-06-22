from elasticsearch_dsl import Document, Date, Keyword, Integer, Boolean, Q
from elasticsearch.exceptions import NotFoundError

class Project(Document):
    timestamp = Date(default_timezone='Brazil/East')
    owner = Keyword()
    date = Date(default_timezone='Brazil/East') 
    number_projects = Integer()
    number_test_cases = Integer()
    number_keywords = Integer()
    number_variables = Integer()
    number_lines = Integer()
    
    class Index:
        name = 'index-project'
        settings = {
            "number_of_shards": 1
        }


