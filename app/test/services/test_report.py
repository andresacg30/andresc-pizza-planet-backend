import pytest


def test_get_report_service(client, report_uri, create_orders):
    response = client.get(report_uri)
    report = response.json

    pytest.assume(response.status.startswith('200'))
    pytest.assume(report['most_requested_ingredient'])
    pytest.assume(report['month_with_most_revenue'])
    pytest.assume(report['top_clients'])
