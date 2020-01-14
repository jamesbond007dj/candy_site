from django.test import SimpleTestCase
from django.urls import reverse

class TwixTests(SimpleTestCase):

    def test_twix_page_status(self):
        url = reverse ('twix')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_twix_page_templates(self):
        url = reverse ('twix')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'twix.html')
