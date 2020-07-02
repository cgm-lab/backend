from datetime import date
from uuid import uuid4

from django.db import models

from common.models import BaseSheet


class Venue(BaseSheet, models.Model):
    sheet_name = "Venue"
    guid = models.CharField(primary_key=True, max_length=36, default=uuid4)

    name = models.CharField(max_length=10)
    full_nmae = models.CharField(max_length=200)
    type = models.CharField(
        max_length=50,
        choices=(("conference", "conference"), ("journal", "journal")),
        default="conference",
    )


class Paper(BaseSheet, models.Model):
    sheet_name = "Paper"
    guid = models.CharField(primary_key=True, max_length=36, default=uuid4)

    title = models.CharField(max_length=200)  # Use first result of Google Scholar
    year = models.IntegerField(default=date.today().year)  # AD
    venue = models.ForeignKey(
        Venue, verbose_name=_("Venue"), on_delete=models.PROTECT
    )

    class Meta:
        ordering = ["-year", "venue"]

    @staticmethod
    def clean_year_data(value: str) -> int:
        return int(value)
