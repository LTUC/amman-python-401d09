from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Thing

# Create your tests here.
class ThingTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='test', password='test1234')
        test_user.save()
        test_thing = Thing.objects.create(name="rake", owner=test_user, desc="Better for collecting leaves than a shovel.")
        test_thing.save()

    def test_thing_model(self):
        thing = Thing.objects.get(pk=1)
        self.assertEqual(str(thing.owner) , 'test')
        self.assertEqual(str(thing.name) , 'rake')
        self.assertEqual(str(thing.desc) , 'Better for collecting leaves than a shovel.')