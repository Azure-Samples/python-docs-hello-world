import unittest

from application import app

class BasicTestCase(unittest.TestCase):

	def test_empty_db(client):
	    response = app.test_client().get('/')
	    assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()
