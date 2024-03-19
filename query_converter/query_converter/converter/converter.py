def convert_query_to_es_format(query: str) -> dict:
    field, dummy, value = query.partition("=")
    field = field.strip()
    value = value.strip()
    if value.endswith("*"):
        return {
            "wildcard": {
                field: value,
            },
        }
    return {
        "match": {
            field: value,
        },
    }
