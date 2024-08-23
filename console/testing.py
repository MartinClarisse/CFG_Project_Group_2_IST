import unittest
from unittest.mock import patch
from logins_sql import Authentication, User  # Adjust the module name if needed


class TestAuthentication(unittest.TestCase):

    @patch('db.query_db')  # Mocking the query_db function (adjust the module name if necessary)
    def test_check_user_exists_user_found(self, mock_query_db):
        mock_query_db.return_value = [{'username': 'thedud'}]

        auth = Authentication('thedud', 'password')
        result = auth.check_user_exists()

        self.assertTrue(result)
        mock_query_db.assert_called_once_with("SELECT * FROM  Authentication WHERE username = %s;", ('thedud',))

    @patch('db.query_db')  # Mocking the query_db function (adjust the module name if necessary)
    def test_check_user_exists_user_not_found(self, mock_query_db):
        mock_query_db.return_value = []

        auth = Authentication('unknownuser', 'password')
        result = auth.check_user_exists()

        self.assertFalse(result)
        mock_query_db.assert_called_once_with("SELECT * FROM  Authentication WHERE username = %s;", ('unknownuser',))

    @patch('db.query_db')  # Mocking the query_db function (adjust the module name if necessary)
    def test_check_password_match_success(self, mock_query_db):
        mock_query_db.return_value = [
            {'username': 'thedud', 'PWD': '5f4dcc3b5aa765d61d8327deb882cf99'}]  # md5('password')

        auth = Authentication('thedud', 'password')
        result = auth.check_password_match()

        self.assertTrue(result)
        mock_query_db.assert_called_once_with("SELECT * FROM  Authentication WHERE username = %s AND PWD = %s;",
                                              ('thedud', '5f4dcc3b5aa765d61d8327deb882cf99'))

    @patch('db.query_db')  # Mocking the query_db function (adjust the module name if necessary)
    def test_check_password_match_fail(self, mock_query_db):
        mock_query_db.return_value = []

        auth = Authentication('thedud', 'wrongpassword')
        result = auth.check_password_match()

        self.assertFalse(result)
        mock_query_db.assert_called_once_with("SELECT * FROM  Authentication WHERE username = %s AND PWD = %s;",
                                              ('thedud', 'd8578edf8458ce06fbc5bb76a58c5ca4'))  # Correct MD5 hash


class TestUser(unittest.TestCase):

    @patch('db.insert_db')  # Mocking the insert_db function (adjust the module name if necessary)
    def test_insert_member_details(self, mock_insert_db):
        mock_insert_db.return_value = 1

        user = User('Rachel Green', 'rachel.green@gmail.com', 'rachelg', 'centralperk')
        result = user.insert_member_details()

        self.assertEqual(result, 1)
        mock_insert_db.assert_called_once_with("INSERT INTO Member_Details (member_name, email) VALUES (%s, %s);",
                                               ('Rachel Green', 'rachel.green@gmail.com'))

    @patch('db.query_db')  # Mocking the query_db function (adjust the module name if necessary)
    @patch('db.insert_db')  # Mocking the insert_db function (adjust the module name if necessary)
    def test_insert_authentication_details(self, mock_insert_db, mock_query_db):
        mock_query_db.return_value = [(1,)]  # Assuming member_id 1 is returned
        mock_insert_db.return_value = 1

        user = User('Rachel Green', 'rachel.green@gmail.com', 'rachelg', 'centralperk')
        result = user.insert_authentication_details()

        self.assertEqual(result, 1)
        mock_query_db.assert_called_once_with("SELECT member_id FROM Member_details WHERE member_name = %s;",
                                              ('Rachel Green',))
        mock_insert_db.assert_called_once_with(
            "INSERT INTO Authentication (username, member_id, PWD)VALUES (%s,%s,md5(%s));",
            ('rachelg', 1, 'centralperk'))


if __name__ == '__main__':
    unittest.main()