from django.test import TestCase

from django.contrib import auth
from django.contrib.auth.models import User

from game.models import Resource, Building

class SignUpViewTests(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='john', password='secret')
        user.save()
        resource = Resource.objects.create(user_id=user)
        resource.save()

    def test_already_authenticated_user_is_redirected(self):
        self.client.login(username='john', password='secret')
        response = self.client.get('/signup/')
        self.assertRedirects(response, '/')
        self.client.logout()

    def test_user_account_is_created(self):
        response = self.client.post('/signup/', {
            'username': 'beth', 
            'password1': 'secret123456', 
            'password2': 'secret123456'
        }) # Password must have at least 8 chars
        user = auth.get_user(self.client)
        self.assertEqual(user.is_authenticated, True)
        resource = Resource.objects.get(user_id=user)
        building = Building.objects.get(user_id=user)
        self.assertEqual(building.gold_mine, 1)
        self.assertEqual(building.rock_mine, 1)
        self.assertEqual(building.lumber_camp, 1)
        self.assertEqual(resource.gold, 0)
        self.assertEqual(resource.rock, 0)
        self.assertEqual(resource.wood, 0)

class LoginViewTests(TestCase):
    
    def setUp(self):
        user = User.objects.create_user(username='john', password='secret')
        user.save()
        resource = Resource.objects.create(user_id=user)
        resource.save()

    def test_redirect_if_authenticated(self):
        self.client.login(username='john', password='secret')
        response = self.client.get('/login/')
        self.assertRedirects(response, '/')

    def test_user_is_logged_in(self):
        response = self.client.post('/login/', {'username': 'john', 'password': 'secret'})
        user = auth.get_user(self.client)
        self.assertEqual(user.is_authenticated, True)
        self.assertRedirects(response, '/')
        self.client.logout()

class LogoutViewTests(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='john', password='secret')
        user.save()
    
    def test_user_is_logged_out(self):
        self.client.login(username='john', password='secret')
        response = self.client.get('/logout/')
        user = auth.get_user(self.client)
        self.assertEqual(user.is_authenticated, False)
        self.assertRedirects(response, '/login/')