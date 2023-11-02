from django.test import TestCase
from rest_framework.test import APIClient, RequestsClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="Pizza", price=100, inventory=50)
        Menu.objects.create(title="Burger", price=60, inventory=30)

    def test_getall(self):
        response = self.client.get('/your_menu_endpoint/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
