import pytest


def test_get_report_service(client, report_uri, create_orders):
    response = client.get(report_uri)
    report = response.json

    pytest.assume(response.status.startswith('200'))
