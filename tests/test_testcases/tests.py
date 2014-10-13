from django.test import TransactionTestCase

from . import models

class TestTransactionTestCase(TransactionTestCase):
    available_apps = ['test_testcases']

    def test_migration_data(self):
        self.assertEqual(1, models.Person.objects.count())

    def test_migration_data2(self):
        """
        Check that our 'Person' is kept after first test has run
        """
        self.assertEqual(1, models.Person.objects.count())
