from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Thing
# Create your tests here.
class ThingTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test', email='test@@test.com',
            password='test@12345'
        )
        self.thing = Thing.objects.create(
            name="Test",
            rank=10,
            reviewer=self.user,
        )
    def test_list_status(self):
        url = reverse("things_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_list_template(self):
        url = reverse("things_list")
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'things_list.html')

    def test_str_method(self):
        self.assertEqual(str(self.thing), 'Test')

    def test_detail_view(self):
        url = reverse('thing_detail', args=[self.thing.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'thing_detail.html')

    def test_create_view(self):
        url = reverse('thing_create')
        data = {
            "name": "Test Create",
            "reviewer": self.user.id
        }
        response = self.client.post(path=url, data=data, follow=True)
        self.assertTemplateUsed(response, 'thing_detail.html')
        self.assertRedirects(response, reverse('thing_detail', args=[2]))
        self.assertEqual(len(Thing.objects.all()), 2)