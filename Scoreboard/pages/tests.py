from django.test import TestCase

from django.test import SimpleTestCase
class SimpleTests(SimpleTestCase):
	
	def test_home_page_status_code(self):
		response = self.client.get('result/')
		self.assertEqual(response.status_code,  220)