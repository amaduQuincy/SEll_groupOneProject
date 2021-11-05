from django.test import Client
from io import BytesIO
from django.test import TestCase

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
        auth.login(request, user)
    else:
        pass

test.py:

class TestSuite(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='admin', email='admin@gmail.com', password='admin')

    def test_user_can_login(self):
        r = self.factory.post("/login", {"username": "admin", "password": "admin"})
        login(r)

# Create your tests here.
