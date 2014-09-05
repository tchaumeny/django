# -*- coding: utf-8 -*-

import unittest

from django.db import connection
from django.test import TestCase, modify_settings

from .models import CharFieldModel, TextFieldModel

from django.contrib.postgres import unaccent

@unittest.skipUnless(
    connection.vendor == 'postgresql' and connection.pg_version >= 90000,
    'PostgreSQL >= 9.0 required')
@modify_settings(INSTALLED_APPS={'append': 'django.contrib.postgres.unaccent'})
class UnaccentTest(TestCase):

    Model = CharFieldModel

    def setUp(self):
        with connection.cursor() as cursor:
            cursor.execute("CREATE EXTENSION IF NOT EXISTS unaccent;")
        self.objs = [
            self.Model.objects.create(field="àéÖ"),
            self.Model.objects.create(field="aeO"),
            self.Model.objects.create(field="aeo"),
        ]

    def test_unaccent(self):
        self.assertSequenceEqual(
            self.Model.objects.filter(field__unaccent="aeO"),
            self.objs[:2]
        )

    def test_unaccent_iexact(self):
        """
        Check that unaccent can be used chained with a lookup (which should be
        the case since unaccent implements the Transform API)
        """
        self.assertSequenceEqual(
            self.Model.objects.filter(field__unaccent__iexact="aeO"),
            self.objs[:3]
        )

    def test_unaccent_accentuated_needle(self):
        self.assertSequenceEqual(
            self.Model.objects.filter(field__unaccent="aéO"),
            []
        )

class UnaccentTextFieldTest(UnaccentTest):
    """
    TextField should have the exact same behavior as CharField
    regarding unaccent lookups.
    """
    Model = TextFieldModel
