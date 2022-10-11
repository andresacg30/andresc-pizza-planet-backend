import pytest


def test_get_sizes_service(client, create_sizes, size_uri):
    response = client.get(size_uri)
    pytest.assume(response.status.startswith('200'))

