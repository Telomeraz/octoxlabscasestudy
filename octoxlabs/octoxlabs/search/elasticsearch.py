from elasticsearch import Elasticsearch

from django.conf import settings


def query_elasticsearch(query: str) -> list:
    es = Elasticsearch(settings.ELASTICSEARCH_HOST)

    response = es.search(index="hosts_v1", body={"query": query})
    hits = response["hits"]["hits"]

    results = [hit["_source"] for hit in hits]
    return results
