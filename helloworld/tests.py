from django.test import TestCase, Client

# Create your tests here.

class AppTests(TestCase):
  def setUp(self):
    self.c = Client()

  def test_helloworld(self):
    r = self.c.get("/")

    self.assertEqual(r.content.decode("utf-8"), "Hello World")
