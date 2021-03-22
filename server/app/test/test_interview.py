from manage import test
import unittest

from app.main import db
import json
from app.test.base import BaseTestCase

test_interview = {
    'id': '',
    'date': '2021-03-03 05:05:05',
    'interviewer': 'Bob - Master of Deduction',
    'phone': 'test phone',
    'comms': 'hahaha',
    'interview_address': 'test address',
    'mailing_address': 'test address',
    'follow_up_date': '2021-03-03 05:05:05',
    'comments': 'Weird, but ok'
}

def add_an_interview(self):
    return self.client.post(
        '/interview/',
        data=json.dumps(
            test_interview
        ),
        content_type='application/json'
    )

def update_an_interview(self, id, interview):
    return self.client.post(
        '/interview/' + id,
        data=json.dumps(
            interview
        ),
        content_type='application/json'
    )

def get_an_interview(self, id):
    return self.client.get(
        '/interview/' + id
    )

def delete_an_interview(self, id):
    return self.client.delete(
        '/interview/' + id
    )

class TestInterviewBlueprint(BaseTestCase):
    def test_submit_interview(self):
        """ Tests new interview submission """
        with self.client:
            response = add_an_interview(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Interview successfully saved.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_find_an_interview(self):
        """ Tests finding a interview submission """
        add_an_interview(self)
        with self.client:
            interview = get_an_interview(self, '1')

            comparrison_interview = test_interview
            comparrison_interview['id'] = '1'
            
            data = json.loads(interview.data.decode())
            
            self.assertEqual(data, comparrison_interview)

    def test_deleting_an_interview(self):
        """ Tests deleting a interview submission """
        add_an_interview(self)
        with self.client:
            response = delete_an_interview(self, '1')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(response.content_type == 'application/json')
            self.assertTrue(response.status_code, 201)

    def test_updating_an_interview(self):
        """ Tests updating a interview submission """
        add_an_interview(self)
        with self.client:
            comparrison_interview = test_interview
            comparrison_interview['id'] = '1'
            comparrison_interview['interviewer'] = 'Cthulhu - Arbiter of positivity.'
            update_an_interview(self, '1', comparrison_interview)
            response = get_an_interview(self, '1')
            data = json.loads(response.data.decode())
            self.assertEqual(comparrison_interview, data)

    def test_failed_update_of_interview(self):
        """ Tests failed update of submission """
        with self.client:
            update_an_interview(self, '1', test_interview)
            response = get_an_interview(self, '1')
            self.assertTrue(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()