import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from dotenv import load_dotenv
import openai
import json
import logging

# Configure logging
logging.basicConfig(
    filename="test_report.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load environment variables
load_dotenv()
print("Loaded OpenAI API Key:", os.getenv("OPENAI_API_KEY"))  # Debugging

# Constants
LOGIN_URL = "https://app.propteq.ai/auth/sign-in"
AGENCY_PAGE_URL = "https://app.propteq.ai/agency"
EMAIL_XPATH = "//input[@name='email']"
PASSWORD_XPATH = "//input[@name='password']"
SUBMIT_BUTTON_XPATH = "//button[@type='submit']"
AGENCY_PAGE_BODY_XPATH = "/html/body"

# Initialize WebDriver
@pytest.fixture(scope="function")
def driver():
    chrome_driver_path = "/opt/homebrew/bin/chromedriver"  # Update if needed
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless mode for speed
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)  # Reduce the need for explicit waits
    yield driver
    driver.quit()

# Function to perform login
def perform_login(driver, email, password):
    driver.get(LOGIN_URL)
    driver.find_element(By.XPATH, EMAIL_XPATH).send_keys(email)
    driver.find_element(By.XPATH, PASSWORD_XPATH).send_keys(password)
    driver.find_element(By.XPATH, SUBMIT_BUTTON_XPATH).click()

# Test Case: Valid Login
def test_valid_login(driver):
    logging.info("Running test: Valid Login")
    try:
        perform_login(driver, "isa@wemark.com.au", "WvwaroQCK8CCC#Ey")
        WebDriverWait(driver, 15).until(EC.url_to_be(AGENCY_PAGE_URL))
        assert driver.current_url == AGENCY_PAGE_URL, f"Valid login test failed. Current URL: {driver.current_url}"
        logging.info("Valid login test passed.")
    except Exception as e:
        logging.error(f"Valid login test failed. Error: {str(e)}")
        raise e

# Test Case: Invalid Login
def test_invalid_login(driver):
    logging.info("Running test: Invalid Login")
    try:
        # Perform login with invalid credentials
        perform_login(driver, "invalid_email@example.com", "wrong_password")

        # Wait for either redirection to the agency page or timeout
        try:
            WebDriverWait(driver, 5).until(EC.url_to_be(AGENCY_PAGE_URL))
            # If redirected, the login was successful (which is a failure for this test)
            logging.error("Invalid login credentials allowed access. This is a security issue.")
            capture_screenshot(driver, "invalid_login_success.png")
            assert False, "Invalid login credentials allowed access. This is a security issue."
        except TimeoutException:
            # If not redirected, the login failed (expected behavior)
            logging.info("Invalid login test passed.")
    except Exception as e:
        logging.error(f"Invalid login test failed. Error: {str(e)}")
        raise e

# Test Case: Empty Fields
def test_empty_fields(driver):
    print("Running test: Empty Fields")
    driver.get(LOGIN_URL)

    driver.find_element(By.XPATH, EMAIL_XPATH).send_keys("")
    driver.find_element(By.XPATH, PASSWORD_XPATH).send_keys("")
    driver.find_element(By.XPATH, SUBMIT_BUTTON_XPATH).click()

    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'required') or contains(text(), 'email')]"))
        )
        assert error_message is not None, "Error message not displayed for empty fields."
    except Exception as e:
        print("Error message not found. Debugging page source:")
        print(driver.page_source)
        raise e

# Test Case: SQL Injection
def test_sql_injection(driver):
    print("Running test: SQL Injection")
    perform_login(driver, "'; DROP TABLE users; --", "password")

    error_message = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Invalid email format')]"))
    )

    assert error_message is not None, "SQL Injection test failed."

# Test Case: AI-Generated Inputs for Edge Cases
def test_ai_generated_inputs(driver):
    logging.info("Running test: AI-Generated Inputs")
    try:
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        if not OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

        openai_client = openai.OpenAI(api_key=OPENAI_API_KEY)
        prompt = "Generate a set of malicious email inputs that could be used to test authentication security."
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        test_emails = response.choices[0].message.content.split("\n")

        for email in test_emails:
            email = email.strip()
            logging.info(f"Testing AI-generated input: {email}")

            # Perform login
            perform_login(driver, email, "password")

            # Wait for either redirection to the agency page or timeout
            try:
                WebDriverWait(driver, 5).until(EC.url_to_be(AGENCY_PAGE_URL))
                # If redirected, the login was successful (which is a failure for this test)
                logging.error(f"AI-generated input '{email}' allowed login. This is a security issue.")
                capture_screenshot(driver, f"security_issue_{email}.png")
                assert False, f"AI-generated input '{email}' allowed login. This is a security issue."
            except TimeoutException:
                # If not redirected, the login failed (expected behavior)
                logging.info(f"AI-generated input '{email}' failed to log in as expected.")
    except Exception as e:
        logging.error(f"AI-generated inputs test failed. Error: {str(e)}")
        raise e

# Run tests
if __name__ == "__main__":
    pytest.main(["-v"])
