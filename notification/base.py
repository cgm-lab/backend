import requests
from django.core.mail import send_mail

from cgm.settings import SECRETS


class Notification:
    @staticmethod
    def send_line(text, token, *args, **kwargs):
        # TODO: check success
        res = requests.post(
            "https://notify-api.line.me/api/notify",
            data={"message": text},
            headers={"Authorization": "Bearer " + token},
        )

    @staticmethod
    def send_telegram(text, token, *args, **kwargs):
        # TODO: check success
        res = requests.post(
            f"https://api.telegram.org/bot{kwargs['id']}/sendMessage",
            data={"chat_id": token, "text": text},
        )

    @staticmethod
    def send_mail(text, token, *args, **kwargs):
        # TODO: Next stage
        success = send_mail(
            "CGM Lab Notification",
            text,
            "CGM Lab <no-reply@cgm.im>",
            ["b10509017@gapps.ntust.edu.tw"],
            fail_silently=False,
        )

    @staticmethod
    def subscribe():
        # TODO: move to models.py
        # add to push_env.json
        pass

    @staticmethod
    def unsubscribe():
        # remove from push_env.json
        pass

    @classmethod
    def broadcast(cls, text):
        # TODO: reload PUSH_ENV
        for platform, params in SECRETS["notification"].items():  # str, dict
            send = getattr(cls, f"send_{platform}")
            # traverse tokens
            tokens = params.pop("tokens")
            for token in tokens:
                send(token, **params)
