import os
import sqlite3
import unittest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

HOST = "127.0.0.1"
PORT = 5000

driver = webdriver.Chrome(service=Service(r"/usr/bin/chromedriver"))


def check_application_status() -> None:
    r = requests.get(f"http://{HOST}:{PORT}")
    if r.status_code != 200:
        raise Exception(
            "The application server is not active! Run ./exec_app.sh before performing any tests."
        )
    print("Successful connection test!")


class TestSQLInjection(unittest.TestCase):
    """Performs a simple SQL injection to illustrate the capabilities of pytest for the team."""

    def setUp(self) -> None:
        # Verify if application is running
        check_application_status()

        # Fill user table with data
        requests.post(
            f"http://{HOST}:{PORT}/signup",
            data={
                "name": "Alice",
                "email": "alice@example.com",
                "password": "alice123",
            },
        )
        requests.post(
            f"http://{HOST}:{PORT}/signup",
            data={"name": "Bob", "email": "bob@example.com", "password": "bob123"},
        )

    def test_selenium_delete_rows(self):
        injection = "wxyz', '', '', '', ''); DELETE FROM users; --"

        # Use selenium to access the application
        driver.get("http://127.0.0.1:5000/signup")
        driver.find_element(by="id", value="name").send_keys(injection)
        driver.find_element(by="id", value="email").send_keys("test@example.com")
        driver.find_element(by="id", value="password").send_keys("test123")
        driver.find_element(by="id", value="submit").click()

        # Close browser
        driver.close()

        # Open connection
        db_connection = sqlite3.connect(
            "../vulnerable/users.db", check_same_thread=False
        )

        # Create a cursor object
        cursor = db_connection.cursor()

        # execute an SQL query to check if the table was emptied
        cursor.execute("SELECT COUNT() FROM users")
        num_users = cursor.fetchone()[0]

        self.assertFalse(num_users == 0)

    def test_requests_delete_rows(self):
        injection = "wxyz', '', '', '', ''); DELETE FROM users; --"

        req = requests.post(
            "http://127.0.0.1:5000/signup",
            data={
                "name": injection,
                "email": "test@example.com",
                "password": "test123",
            },
        )

        self.assertFalse(req.ok)


if __name__ == "__main__":
    unittest.main()
