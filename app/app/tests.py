from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    """test calc module"""

    def test_add(self):
        res = calc.add(5,6)
        self.assertEqual(res,11)
