from datetime import date
from uuid import uuid4

from django.db import models

from common.models import BaseSheet


class Member(BaseSheet, models.Model):
    sheet_name = "Member"
    guid = models.CharField(primary_key=True, max_length=36, default=uuid4)

    student_id = models.CharField(max_length=9)
    avatar = models.URLField(blank=True)
    year = models.IntegerField(
        choices=[(r, r) for r in range(1984 - 1911, date.today().year + 1 - 1911)],
        default=date.today().year - 1911,
    )  # ROC
    name = models.CharField(max_length=30)
    foreign_name = models.CharField(max_length=30, blank=True, null=True)
    hobby = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    constellation = models.CharField(max_length=100)
    link = models.URLField(blank=True, max_length=200)
    email = models.EmailField(blank=True, max_length=254)
    education = models.CharField(
        max_length=15,
        choices=[(r, r) for r in ("Master", "Ph.D.", "EMBA", "EDBA", "Professor")],
        default="Master",
    )
    is_graduated = models.BooleanField(
        choices=[(True, True), (False, False)], default=False
    )

    @staticmethod
    def clean_year_data(value: str) -> int:
        return int(value)

    @staticmethod
    def clean_is_graduated_data(value: str) -> bool:
        return value == "TRUE"

    def __str__(self):
        return f"{self.name} {self.education} // {self.email} ({self.guid})"
