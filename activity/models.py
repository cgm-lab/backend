from uuid import uuid4

from django.db import models

from cgm.settings import GSHEETS_DB
from common.models import BaseSheet


class Activity(BaseSheet, models.Model):
    spreadsheet_id = GSHEETS_DB["Album"]

    sheet_name = "Activity"
    guid = models.CharField(primary_key=True, max_length=36, default=uuid4)

    activity = models.CharField(max_length=50)
    photo = models.URLField(max_length=200)  # TODO: optimize image size
    name = models.CharField(max_length=50)
    date = models.DateField()
    location = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ["-date", "activity"]

    def __str__(self):
        return f"{self.name} {self.date} {self.activity} // {self.photo} ({self.guid})"
