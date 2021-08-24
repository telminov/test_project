from django.test import TestCase
from core import models


class BookModelTestCase(TestCase):

    def setUp(self):
        self.book = models.Book.objects.create(name='Test Book')

    def testStr(self):
        self.assertEqual(str(self.book), 'Test Book')

