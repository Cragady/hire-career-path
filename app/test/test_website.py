from manage import test
import unittest

from app.main import db
import json
from app.test.base import BaseTestCase

test_website = {
    'id': '',
    'website': 'heavensthread.com',
    'username': 'CreamBatter',
    'resume_date': '2021-10-10 08:08:08',
    'cover_letter_date': '2021-10-10 08:08:08',
    'comments': 'Weird, but ok'
}

def add_a_website(self):
    return self.client.post(
        '/website/',
        data=json.dumps(
            test_website
        ),
        content_type='application/json'
    )

def update_a_website(self, id, website):
    return self.client.post(
        '/website/' + id,
        data=json.dumps(
            website
        ),
        content_type='application/json'
    )

def get_a_website(self, id):
    return self.client.get(
        '/website/' + id
    )

def delete_a_website(self, id):
    return self.client.delete(
        '/website/' + id
    )

class TestWebsiteBlueprint(BaseTestCase):
    def test_website_submission(self):
        """ Tests new website submission """
        with self.client:
            response = add_a_website(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Website successfully saved.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_find_a_website(self):
        """ Tests finding a website submission """
        add_a_website(self)
        with self.client:
            website = get_a_website(self, '1')

            comparrison_website = test_website
            comparrison_website['id'] = '1'
            
            data = json.loads(website.data.decode())
            
            self.assertEqual(data, comparrison_website)

    def test_deleting_a_website(self):
        """ Tests deleting a website submission """
        add_a_website(self)
        with self.client:
            response = delete_a_website(self, '1')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(response.content_type == 'application/json')
            self.assertTrue(response.status_code, 201)

    def test_updating_a_website(self):
        """ Tests updating a website submission """
        add_a_website(self)
        with self.client:
            comparrison_website = test_website
            comparrison_website['id'] = '1'
            comparrison_website['username'] = 'PlanetJumper.'
            update_a_website(self, '1', comparrison_website)
            response = get_a_website(self, '1')
            data = json.loads(response.data.decode())
            self.assertEqual(comparrison_website, data)

    def test_failed_update_of_website(self):
        """ Tests failed update of submission """
        with self.client:
            update_a_website(self, '1', test_website)
            response = get_a_website(self, '1')
            self.assertTrue(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()