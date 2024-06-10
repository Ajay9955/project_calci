from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class claculatortests(TestCase):
    def testaddition(self):
        response = self.client.post(reverse('calculate'), {'num1':5, 'operation': 'add', 'num2':4})
        self.assertEqual(response.status_code, 200)#succesfull http request
        self.assertContains(response, '9')#checking the value 
    def testsubraction(self):
        response = self.client.post(reverse('calculate'),{'num1': 5, 'operation':'sub', 'num2': 4})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1')    
    def testmultiplication(self):
        response = self.client.post(reverse('calculate'),{'num1': 1, 'operation':'mul', 'num2': 1})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1')    
    def testdivision(self):
        response = self.client.post(reverse('calculate'),{'num1': 5, 'operation':'div', 'num2': 5})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1')    