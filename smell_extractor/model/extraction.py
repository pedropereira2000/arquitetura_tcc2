"""
Index to keep when the last data extraction was performed
"""
from elasticsearch.exceptions import NotFoundError
from elasticsearch_dsl import Date, Document


class Extraction(Document):
    timestamp = Date(default_timezone='Brazil/East')

    def last_extraction_date(self):
        try:
            for hit in self.search().sort({"timestamp": {"order": "desc"}}):
                return hit['timestamp']

            return None
        except NotFoundError:
            return None

    class Index:
        name = 'index-extraction'
        settings = {
            "number_of_shards": 1
        }