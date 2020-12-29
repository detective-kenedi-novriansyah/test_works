import json
import logging
import unittest

from database.models.question import Question
from django.test import Client
from django.urls import reverse
from rest_framework import status

with open('question.json', 'r') as r:
    question = json.loads(r.read())

class TestsQuestion(unittest.TestCase):
    def setUp(self):
        self.e = Client()

    @unittest.skipIf(Question.objects.count() == 13, "Question is over")
    def test_record(self):
        urls = reverse('api:question-list')
        qq = Question.objects.count()
        q_ = question.get(str(qq)).get('question')
        data = json.dumps({
            "quest": q_
        })
        response = self.e.post(urls,data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(response.data, None)
        log = logging.getLogger("Record Question")
        log.info(response.data)

    @unittest.skipIf(Question.objects.count() == 0, "Question not have data")
    def test_retrieve(self):
        quest = Question.objects.first()
        urls = reverse('api:question-detail',args=[quest.id])
        data = json.dumps({
            'quest': 'Question has been updated %s' % quest.quest
        })
        response = self.e.put(urls, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data, None)
        log = logging.getLogger("Retrieve Question")
        log.info(response.data)
