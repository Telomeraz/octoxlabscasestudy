from faker import Faker

from search.serializers import QuerySerializer

fake = Faker()


class TestQuerySerializer:
    def test_data(self) -> None:
        query = fake.text()
        data = {
            "query": query,
        }
        serializer = QuerySerializer(data=data)

        assert serializer.is_valid()
        assert serializer.validated_data["query"] == query
