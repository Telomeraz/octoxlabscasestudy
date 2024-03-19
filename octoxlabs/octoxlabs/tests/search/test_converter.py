from search.converter import convert_query


def test_convert_query() -> None:
    query = "hostname = octo*"
    converted_query = convert_query(query)

    assert converted_query == {
        "wildcard": {
            "hostname": "octo*",
        },
    }


def test_convert_query_if_query_is_exact_match() -> None:
    query = "hostname = octoxlabs"
    converted_query = convert_query(query)

    assert converted_query == {
        "match": {
            "hostname": "octoxlabs",
        },
    }
