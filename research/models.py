from datetime import date
from uuid import uuid4

from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import BaseSheet
from member.models import Member


class ResearchPhoto(BaseSheet, models.Model):
    # TODO: move to Research and change file name from original to guid
    models.TextField(_(""))
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=200)


class Research(BaseSheet, models.Model):
    sheet_name = "Research"
    guid = models.CharField(primary_key=True, max_length=36, default=uuid4)

    title = models.CharField(max_length=200)
    chinese_title = models.CharField(max_length=100, blank=True)
    year = models.IntegerField(default=date.today().year)  # AD
    link = models.URLField(max_length=200)
    photo = models.URLField(
        max_length=200
    )  # XXX: not sure foreign_key or url field or one-to-oen-field
    authors = models.ManyToManyField("member.Member", verbose_name=_("Authors"))

    @staticmethod
    def clean_year_data(value: str) -> int:
        return int(value)


class TechnicalReport(BaseSheet, models.Model):
    sheet_name = "TechnicalReport"
    guid = models.CharField(primary_key=True, max_length=36, default=uuid4)

    title = models.CharField(max_length=200)
    year = models.IntegerField()
    venue = models.CharField(max_length=50)
    authors = models.ManyToManyField("member.Member", verbose_name=_("Authors"))

    @staticmethod
    def clean_year_data(value: str) -> int:
        return int(value)
