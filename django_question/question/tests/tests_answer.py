import json
import logging
import unittest
from django.db.models import Count
import random

from database.models.question import Question
from django.test import Client
from django.urls import reverse
from rest_framework import status

with open('question.json', 'r') as r:
    question = json.loads(r.read())

with open('question_text.json', 'r') as r:
    question_text = json.loads(r.read())

class TestsAnswer(unittest.TestCase):
    def setUp(self):
        self.e = Client()

    @unittest.skipIf(Question.objects.count() == 0, "Question not have data")
    def test_record(self):
        urls = reverse('api:answer-list')
        quest = Question.objects.annotate(num_answer=Count("answer")).filter(num_answer__lt=4).first()
        right___ = quest.answer.filter(right=True).count()
        random_answer = random.randint(2,3)
        index = quest.id - 1
        already = None
        right = False

        if quest.num_answer == 0:
            if not right___:
                if random_answer % 2 == 0:
                    right = True
                    already = True
            questios_ = question.get(str(index)).get('answer')[quest.num_answer].get('a')
        elif quest.num_answer == 1:
            if not right___:
                if not already:
                    if random_answer % 2 == 0:
                        right = True
            questios_ = question.get(str(index)).get('answer')[quest.num_answer].get('b')
        elif quest.num_answer == 2:
            if not right___:
                if not already:
                    if random_answer % 2 == 0:
                        right = True
                        already = True
            questios_ = question.get(str(index)).get('answer')[quest.num_answer].get('c')
        elif quest.num_answer == 3:
            if not right___:
                if not already:
                    if random_answer % 2 == 0:
                        right = True
                        already = True
            questios_ = question.get(str(index)).get('answer')[quest.num_answer].get('d')
        data = json.dumps({
            "name":  questios_,
            "question": quest.id,
            "right": right
        })

        response = self.e.post(urls, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(response.data, None)
        log = logging.getLogger("Record Answer")
        log.info(response.data)

