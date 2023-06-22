from elasticsearch_dsl import Document, Date, Keyword, Integer, Boolean, Q, Float
from elasticsearch.exceptions import NotFoundError

class Smell(Document):
    timestamp = Date(default_timezone='Brazil/East')
    owner = Keyword()
    category = Keyword()
    project_name = Keyword()
    version = Date(default_timezone='Brazil/East')
    test_case_name = Keyword()
    test_case_size = Integer()
    test_case_sequence = Integer()
    test_case_level = Integer()
    smell_name = Keyword()
    smell_raw_value = Float()
    smell_normalized_value = Float()
    fixes = Integer()

    class Index:
        name = 'index-smells'
        settings = {
            "number_of_shards": 1
        }




