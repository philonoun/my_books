from app import app

import unittest

class BasicTestCase(unittest.TestCase):

  def test_ping(self):
    tester = app.test_client(self)
    response = tester.get('/ping', content_type='html/text')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data, b'"pong!"\n')


if __name__ == '__main__':
  unittest.main()
