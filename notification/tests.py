from django.core.mail import send_mail
from django.test import TestCase


class NotificationTest(TestCase):
    def test_send_line(self):
        pass

    def test_send_telegram(self):
        pass

    def test_send_mail(self):
        success = send_mail(
            "系統測試 System testing!",
            "",
            "CGM Lab <no-reply@cgm.im>",
            ["b10509017@gapps.ntust.edu.tw"],
            fail_silently=False,
        )
        self.assertTrue(success)
