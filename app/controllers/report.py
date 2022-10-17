from sqlalchemy.exc import SQLAlchemyError

from ..repositories.managers import ReportManager
from .base import BaseController


class ReportController(BaseController):
    manager = ReportManager

    @classmethod
    def get_report(cls):
        report = {}
        try:
            report['top_clients'] = cls.manager.get_top_clients()
            report['month_with_most_revenue'] = cls.manager.get_month_with_most_revenue()
            report['most_requested_ingredient'] = cls.manager.get_most_requested_ingredient()
            return report, None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
