from django.test import TestCase

from .utils import render, setup


multiline_string = """
Hello,
boys.
How
are
you
gentlemen.
"""


class MultilineTests(TestCase):

    @setup({'multiline01': multiline_string})
    def test_multiline01(self):
        output = render('multiline01')
        self.assertEqual(output, multiline_string)
