import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_recent_question_is_recent(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        question = Question(pub_date=time)
        self.assertIs(question.was_published_recently(), True)

    def test_old_question_is_not_recent(self):
        time = timezone.now() - datetime.timedelta(days=2)
        question = Question(pub_date=time)
        self.assertIs(question.was_published_recently(), False)
