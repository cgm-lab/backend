import sys

from django.apps import AppConfig


class CommonConfig(AppConfig):
    name = "common"
    verbose_name = "Common"

    def ready(self):
        if "runserver" not in sys.argv:
            return

        from activity.models import Activity
        from member.models import Member

        # from paper.models import Paper

        Activity.pull_sheet()
        Member.pull_sheet()
        # Paper.pull_sheet()
