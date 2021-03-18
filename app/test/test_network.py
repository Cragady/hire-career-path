from manage import test
import unittest

from app.main import db
import json
from app.test.base import BaseTestCase

test_network = {
    'id': '',
    'acquaintance': 'Joe - Creator of the Cosmos',
    'company': 'Bar of Obscure BookS',
    'comms': 'hahaha',
    'comments': 'Weird, but ok'
}

def add_a_network(self):
    return self.client.post(
        '/network/',
        data=json.dumps(
            test_network
        ),
        content_type='application/json'
    )

def update_a_network(self, id, network):
    return self.client.post(
        '/network/' + id,
        data=json.dumps(
            network
        ),
        content_type='application/json'
    )

def get_a_network(self, id):
    return self.client.get(
        '/network/' + id
    )

def delete_a_network(self, id):
    return self.client.delete(
        '/network/' + id
    )

class TestNetworkBlueprint(BaseTestCase):
    def test_network_submission(self):
        """ Tests new network submission """
        with self.client:
            response = add_a_network(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Network successfully saved.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_find_a_network(self):
        """ Tests finding a network submission """
        add_a_network(self)
        with self.client:
            network = get_a_network(self, '1')

            comparrison_network = test_network
            comparrison_network['id'] = '1'
            
            data = json.loads(network.data.decode())
            
            self.assertEqual(data, comparrison_network)

    def test_deleting_a_network(self):
        """ Tests deleting a network submission """
        add_a_network(self)
        with self.client:
            response = delete_a_network(self, '1')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(response.content_type == 'application/json')
            self.assertTrue(response.status_code, 201)

    def test_updating_a_network(self):
        """ Tests updating a network submission """
        add_a_network(self)
        with self.client:
            comparrison_network = test_network
            comparrison_network['id'] = '1'
            comparrison_network['company'] = 'Destructicator of Reconstructication.'
            update_a_network(self, '1', comparrison_network)
            response = get_a_network(self, '1')
            data = json.loads(response.data.decode())
            self.assertEqual(comparrison_network, data)

    def test_failed_update_of_network(self):
        """ Tests failed update of submission """
        with self.client:
            update_a_network(self, '1', test_network)
            response = get_a_network(self, '1')
            self.assertTrue(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()