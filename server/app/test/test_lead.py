from manage import test
import unittest

from app.main import db
import json
from app.test.base import BaseTestCase

test_lead = {
    'id': '',
    'name': 'Ned - Cartographer of the Nether',
    'company': 'Burnt Maps of the Dark',
    'comms': 'hahaha',
    'comments': 'Weird, but ok'
}

def add_a_lead(self):
    return self.client.post(
        '/lead/',
        data=json.dumps(
            test_lead
        ),
        content_type='application/json'
    )

def update_a_lead(self, id, lead):
    return self.client.post(
        '/lead/' + id,
        data=json.dumps(
            lead
        ),
        content_type='application/json'
    )

def get_a_lead(self, id):
    return self.client.get(
        '/lead/' + id
    )

def delete_a_lead(self, id):
    return self.client.delete(
        '/lead/' + id
    )

class TestLeadBlueprint(BaseTestCase):
    def test_lead_submission(self):
        """ Tests new lead submission """
        with self.client:
            response = add_a_lead(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Lead successfully saved.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_find_a_lead(self):
        """ Tests finding a lead submission """
        add_a_lead(self)
        with self.client:
            lead = get_a_lead(self, '1')

            comparrison_lead = test_lead
            comparrison_lead['id'] = '1'
            
            data = json.loads(lead.data.decode())
            
            self.assertEqual(data, comparrison_lead)

    def test_deleting_a_lead(self):
        """ Tests deleting a lead submission """
        add_a_lead(self)
        with self.client:
            response = delete_a_lead(self, '1')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(response.content_type == 'application/json')
            self.assertTrue(response.status_code, 201)

    def test_updating_a_lead(self):
        """ Tests updating a lead submission """
        add_a_lead(self)
        with self.client:
            comparrison_lead = test_lead
            comparrison_lead['id'] = '1'
            comparrison_lead['comms'] = 'Transmutation circle.'
            update_a_lead(self, '1', comparrison_lead)
            response = get_a_lead(self, '1')
            data = json.loads(response.data.decode())
            self.assertEqual(comparrison_lead, data)

    def test_failed_update_of_lead(self):
        """ Tests failed update of submission """
        with self.client:
            update_a_lead(self, '1', test_lead)
            response = get_a_lead(self, '1')
            self.assertTrue(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()