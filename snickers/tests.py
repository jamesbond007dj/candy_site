from django.test import SimpleTestCase
from django.urls import reverse

class SnickersTests(SimpleTestCase):

    def test_snickers_page_status(self):
        url = reverse ('snickers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snickers_page_templates(self):
        url = reverse ('snickers')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snickers.html')

