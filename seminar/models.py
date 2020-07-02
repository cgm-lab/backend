from datetime import date
from uuid import uuid4

from django.db import models
from django.db.models.functions import Length
from django.utils.translation import ugettext_lazy as _

from common.models import BaseSheet


class Seminar(BaseSheet, models.Model):
    sheet_name = "Seminar"
    guid = models.CharField(primary_key=True, max_length=36, default=uuid4)

    date = models.DateField(auto_now=False, auto_now_add=False)
    topic = models.CharField(
        max_length=50,
        blank=True,
        choices=(
            ("Abstract", "Abstract"),
            ("Paper", "Paper"),
            ("Math", "Math"),
            ("Others", "Others"),
        ),  # or CGW / ...
    )
    # FIXME: when speaker is teacher
    speaker = models.ForeignKey(
        "member.Member",
        verbose_name=_("Speaker"),
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    papers = models.ManyToManyField("paper.Paper", verbose_name=_("Paper"))

    class Meta:
        ordering = ["-date", "topic"]  # ordering of topic `Abstract` -> `Paper`

    def __str__(self):
        params = []
        params.append(self.date)
        if self.topic:
            params.append(self.topic)
        if self.speaker:
            params.append(self.speaker)
        # XXX: not sure `count` and `all` will work
        if self.papers.count():
            params.append(
                [f"{i}. {str(paper)[:10]}" for i, paper in enumerate(self.papers.all())]
            )
        return " ".join(params)
