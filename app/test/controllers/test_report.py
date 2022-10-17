import pytest


def test_report_gets_the_most_requested_ingredient(app):
    most_requested_ingredient = ReportController.get_most_requested_ingredient()
    pytest.assume(most_requested_ingredient is not None)
