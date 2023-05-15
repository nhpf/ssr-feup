import os
import sqlite3
import unittest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

DEBUG = False
HOST = "127.0.0.1"
PORT = 5000

driver = webdriver.Chrome(service=Service(r"/usr/bin/chromedriver"))


def check_application_status() -> None:
    r = requests.get(f"http://{HOST}:{PORT}")
    if r.status_code != 200:
        raise Exception(
            "The application server is not active! Run ./exec_app.sh before performing any tests."
        )
    if DEBUG:
        print("\nSuccessful connection test!\n")


def repopulate_db() -> None:
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


class TestSQLInjection(unittest.TestCase):
    """Performs a simple SQL injection to illustrate the capabilities of pytest for the team."""

    def setUp(self) -> None:
        # Ensure that the application is running well
        check_application_status()
        repopulate_db()

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

    def tearDown(self) -> None:
        # Ensure that the application is fine
        check_application_status()
        repopulate_db()


class TestSQLInjectionOnLogin(unittest.TestCase):
    """Performs SQL injection in Login"""

    def setUp(self) -> None:
        # Ensure that the application is running well
        check_application_status()
        repopulate_db()

    def test_requests_login_inject_in_email(self):
        injection = "wxyz' OR 1=1 --"

        req = requests.post(
            "http://127.0.0.1:5000/login",
            data={
                "email": injection,
                "password": "test123",
            },
        )

        if DEBUG and req.status_code == 200:
            print(f"We have exposed user data: {req.text}")

        self.assertNotEqual(req.status_code, 200)

    def test_requests_login_inject_in_password(self):
        injection = "wxyz' OR 1=1 --"

        req = requests.post(
            "http://127.0.0.1:5000/login",
            data={
                "email": "test123",
                "password": injection,
            },
        )

        if DEBUG and req.status_code == 200:
            print(f"We have exposed user data: {req.text}")

        self.assertNotEqual(req.status_code, 200)

    def tearDown(self) -> None:
        # Ensure that the application is fine
        check_application_status()
        repopulate_db()


class TestBruteForceAttacks(unittest.TestCase):
    """Tests if dictionary-based password cracking is feasible"""

    def setUp(self) -> None:
        # Ensure that the application is running well
        check_application_status()
        repopulate_db()

    def test_login_dictionary(self):
        known_email = "alice@example.com"
        has_cracked = False
        # Go through file
        with open("wordlist.txt", "r") as file:
            for potential_password in file.readlines():
                # Perform requests and check for success
                req = requests.post(
                    "http://127.0.0.1:5000/login",
                    data={"email": known_email, "password": potential_password},
                )
                if req.status_code == 200:
                    has_cracked = True
                    if DEBUG:
                        print(
                            f"Found user credentials: {known_email} -> {potential_password}"
                            f"\nWe have exposed user data: {req.text}"
                        )
                    break

        self.assertFalse(has_cracked)

    def tearDown(self) -> None:
        # Ensure that the application is fine
        check_application_status()
        repopulate_db()


class TestImageExploits(unittest.TestCase):
    def setUp(self) -> None:
        # Ensure that the application is running well
        check_application_status()
        repopulate_db()

    def test_xss_in_gif_metadata(self):
        # Define sample GIF image: 2x2 red square
        gif_data = bytes.fromhex("474946383761020002020180ff000000ffff2cff0000000000020002020084020051003b")

        # Separate GIF data from metadata
        gif_img_metadata = gif_data[:13]
        gif_img_data = gif_data[13:]

        # Define JavaScript to be executed and convert it to ASCII hex
        js_hex = "".join([hex(ord(c))[2:] for c in "<script>alert('XSS');</script>"])

        # Inject JavaScript into the image metadata
        gif_img_metadata += f";\n{js_hex}\n".encode("ascii")

        # Get new image by concatenating the new metadata with the old image data
        gif_data = gif_img_metadata + gif_img_data

        # Save the new GIF image to a file
        with open("exploited.gif", "wb") as f:
            f.write(gif_data)

    def tearDown(self) -> None:
        # Ensure that the application is fine
        check_application_status()
        repopulate_db()


if __name__ == "__main__":
    unittest.main()
