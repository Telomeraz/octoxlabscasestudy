from converter.converter import convert_query_to_es_format


def test_convert_query_to_es_format() -> None:
    query = "hostname = octo*"
    converted_query = convert_query_to_es_format(query)

    assert converted_query == {
        "wildcard": {
            "hostname": "octo*",
        },
    }


def test_convert_query_to_es_format_if_query_is_exact_match() -> None:
    query = "hostname = octoxlabs"
    converted_query = convert_query_to_es_format(query)

    assert converted_query == {
        "match": {
            "hostname": "octoxlabs",
        },
    }
