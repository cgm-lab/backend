from datetime import date
from uuid import uuid4

from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import BaseSheet


class Publication(BaseSheet, models.Model):
    title = models.CharField(max_length=200)
    yaer = models.IntegerField()
    venue = models.ForeignKey(
        "paper.Venue", verbose_name=_("Venue"), on_delete=models.PROTECT
    )
    link = models.URLField(max_length=200)

    @staticmethod
    def clean_year_data(value: str) -> int:
        return int(value)
