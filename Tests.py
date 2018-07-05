from routes import app
import unittest

class FlaskTestCase(unittest.TestCase):
	def setup(self):
		tester = app.test_client(self)
	def test_login(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)
	def test_logout(self):
		tester = app.test_client(self)
		response = tester.get('/logout', content_type = 'html/text')
		self.assertEqual(response.status_code, 302)
	def test_info(self):
		tester = app.test_client(self)
		response = tester.get('/info', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)
	def test_home(self):
		tester = app.test_client(self)
		response = tester.get('/home', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)
	def test_register(self):
		tester = app.test_client(self)
		response = tester.get('/register', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
	unittest.main()
