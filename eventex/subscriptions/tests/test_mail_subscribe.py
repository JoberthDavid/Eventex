from django.core import mail
from django.test import TestCase

class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Joberth David', cpf='12345678901', email='joberthdavid@hotmail.com', phone='62-9999-9999')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]
    
    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'joberthdavid@gmail.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['joberthdavid@gmail.com', 'joberthdavid@hotmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Joberth David',
            '123456789',
            'joberthdavid@hotmail.com',
            '62-9999-9999',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)