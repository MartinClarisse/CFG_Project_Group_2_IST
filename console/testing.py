from unittest.mock import patch
import unittest
from logins_sql import Authentication, User  # Replace with your actual module name

class TestAuthentication(unittest.TestCase):

    @patch('logins_sql.query_db')  # Mocking data to check if SQL query properly identifies existing user.
    def test_check_user_exists_user_found(self, mock_query_db):
        mock_query_db.return_value = [{'username': 'thedud'}]

        auth = Authentication('thedud', 'password')
        result = auth.check_user_exists()

        self.assertTrue(result)
        mock_query_db.assert_called_once_with("SELECT * FROM Authentication WHERE username = %s;", ('thedud',))

    @patch('logins_sql.query_db')  # Mocking data to see if SQL query properly identifies missing user.
    def test_check_user_exists_user_not_found(self, mock_query_db):
        mock_query_db.return_value = []

        auth = Authentication('unknownuser', 'password')
        result = auth.check_user_exists()

        self.assertFalse(result)
        mock_query_db.assert_called_once_with("SELECT * FROM Authentication WHERE username = %s;", ('unknownuser',))

    @patch('logins_sql.query_db')  # Checking password match encryption works with existing user.
    def test_check_password_match_success(self, mock_query_db):
        mock_query_db.return_value = [
            {'username': 'thedud', 'PWD': '5f4dcc3b5aa765d61d8327deb882cf99'}]  # md5('password')

        auth = Authentication('thedud', 'password')
        result = auth.check_password_match()

        self.assertTrue(result)
        mock_query_db.assert_called_once_with("SELECT * FROM Authentication WHERE username = %s AND PWD = %s;",
                                              ('thedud', '5f4dcc3b5aa765d61d8327deb882cf99')) # Correct MD5 hash.

    @patch('logins_sql.query_db')  # Checking password match returns mismatch with incorrect existing user detail.
    def test_check_password_match_fail(self, mock_query_db):
        mock_query_db.return_value = []

        auth = Authentication('thedud', 'wrongpassword')
        result = auth.check_password_match()

        self.assertFalse(result)
        mock_query_db.assert_called_once_with("SELECT * FROM Authentication WHERE username = %s AND PWD = %s;",
                                              ('thedud', 'd7eea11dffaf0936611d58d3c5aff066'))  # Correct MD5 hash, but from incorrect password.



class TestUser(unittest.TestCase):

    @patch('logins_sql.insert_db')  # Mocking query data to test inserting member details into SQL.
    def test_insert_member_details(self, mock_insert_db):
        mock_insert_db.return_value = 1

        user = User('Rachel Green', 'rachel.green@gmail.com', 'rachelg', 'centralperk')
        result = user.insert_member_details()

        self.assertEqual(result, 1)
        mock_insert_db.assert_called_once_with("INSERT INTO Member_Details (member_name, email) VALUES (%s, %s);",
                                               ('Rachel Green', 'rachel.green@gmail.com'))

    @patch('logins_sql.query_db')  # Mocking the query_db function
    @patch('logins_sql.insert_db')  # Mocking the insert_db function
    def test_insert_authentication_details(self, mock_insert_db, mock_query_db):
        mock_query_db.return_value = [(2,)]  # Assuming member_id 2 is returned if this test runs before console app launch. SQL script autogenerates dud user 1.
        mock_insert_db.return_value = 2

        user = User('Rachel Green', 'rachel.green@gmail.com', 'rachelg', 'centralperk')
        result = user.insert_authentication_details()

        self.assertEqual(result, 2)
        mock_query_db.assert_called_once_with("SELECT member_id FROM Member_details WHERE member_name = %s;",
                                              ('Rachel Green',))
        mock_insert_db.assert_called_once_with(
            "INSERT INTO Authentication (username, member_id, PWD)VALUES (%s,%s,md5(%s));",
            ('rachelg', 2, 'centralperk'))


if __name__ == '__main__':
    unittest.main()

