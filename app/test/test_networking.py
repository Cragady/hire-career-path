from manage import test
import unittest

from app.main import db
import json
from app.test.base import BaseTestCase

test_networking = {
    'id': '',
    'acquaintance': 'Joe - Creator of the Cosmos',
    'company': 'Bar of Obscure BookS',
    'comms': 'hahaha',
    'comments': 'Weird, but ok'
}

def add_a_networking(self):
    return self.client.post(
        '/networking/',
        data=json.dumps(
            test_networking
        ),
        content_type='application/json'
    )

def update_a_networking(self, id, networking):
    return self.client.post(
        '/networking/' + id,
        data=json.dumps(
            networking
        ),
        content_type='application/json'
    )

def get_a_networking(self, id):
    return self.client.get(
        '/networking/' + id
    )

def delete_a_networking(self, id):
    return self.client.delete(
        '/networking/' + id
    )

class TestNetworkingBlueprint(BaseTestCase):
    def test_network_submission(self):
        """ Tests new networking submission """
        with self.client:
            response = add_a_networking(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Networking successfully saved.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_find_a_network(self):
        """ Tests finding a networking submission """
        add_a_networking(self)
        with self.client:
            networking = get_a_networking(self, '1')

            comparrison_networking = test_networking
            comparrison_networking['id'] = '1'
            
            data = json.loads(networking.data.decode())
            
            self.assertEqual(data, comparrison_networking)

    def test_deleting_a_network(self):
        """ Tests deleting a networking submission """
        add_a_networking(self)
        with self.client:
            response = delete_a_networking(self, '1')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(response.content_type == 'application/json')
            self.assertTrue(response.status_code, 201)

    def test_updating_a_network(self):
        """ Tests updating a networking submission """
        add_a_networking(self)
        with self.client:
            comparrison_networking = test_networking
            comparrison_networking['id'] = '1'
            comparrison_networking['company'] = 'Destructicator of Reconstructication.'
            update_a_networking(self, '1', comparrison_networking)
            response = get_a_networking(self, '1')
            data = json.loads(response.data.decode())
            self.assertEqual(comparrison_networking, data)

    def test_failed_update_of_network(self):
        """ Tests failed update of submission """
        with self.client:
            update_a_networking(self, '1', test_networking)
            response = get_a_networking(self, '1')
            self.assertTrue(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()