from manage import test
import unittest

from app.main import db
import json
from app.test.base import BaseTestCase

test_resume = {
    'id': '',
    'job': 'floogle-meister tester',
    'company': 'Bar of Obscure BookS',
    'contact': 'test contact',
    'phone': 'test phone',
    'comms': 'hahaha',
    'address': 'test address',
    'website': 'test.org',
    'date_submitted': '2021-03-16 13:28:24',
    'cover_letter_date': '2021-03-16 13:28:24',
    'references': 'oopsie',
    'discovered_by': 'accident',
    'job_description': 'master of the floogles',
    'status': 'Hired, but we need to hire you first.',
    'comments': 'Weird, but ok'
}

def add_a_resume(self):
    return self.client.post(
        '/resume/',
        data=json.dumps(
            test_resume
        ),
        content_type='application/json'
    )

def update_a_resume(self, id, resume):
    return self.client.post(
        '/resume/' + id,
        data=json.dumps(
            resume
        ),
        content_type='application/json'
    )

def get_a_resume(self, id):
    return self.client.get(
        '/resume/' + id
    )

def delete_a_resume(self, id):
    return self.client.delete(
        '/resume/' + id
    )

class TestResumeBlueprint(BaseTestCase):
    def test_resume_submission(self):
        """ Tests new resume submission """
        with self.client:
            response = add_a_resume(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Resume successfully saved.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_find_a_resume(self):
        """ Tests finding a resume submission """
        add_a_resume(self)
        with self.client:
            resume = get_a_resume(self, '1')

            comparrison_resume = test_resume
            comparrison_resume['id'] = '1'
            
            data = json.loads(resume.data.decode())
            
            self.assertEqual(data, comparrison_resume)

    def test_deleting_a_resume(self):
        """ Tests deleting a resume submission """
        add_a_resume(self)
        with self.client:
            response = delete_a_resume(self, '1')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(response.content_type == 'application/json')
            self.assertTrue(response.status_code, 201)

    def test_updating_a_resume(self):
        """ Tests updating a resume submission """
        add_a_resume(self)
        with self.client:
            comparrison_resume = test_resume
            comparrison_resume['id'] = '1'
            comparrison_resume['job'] = 'Job of changing data.'
            update_a_resume(self, '1', comparrison_resume)
            response = get_a_resume(self, '1')
            data = json.loads(response.data.decode())
            self.assertEqual(comparrison_resume, data)

    def test_failed_update_of_resume(self):
        """ Tests failed update of submission """
        with self.client:
            update_a_resume(self, '1', test_resume)
            response = get_a_resume(self, '1')
            self.assertTrue(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()