import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv
import openai
import json
import logging

# Configure logging
logging.basicConfig(
    filename="signup_test_report.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load environment variables
load_dotenv()

# Constants
SIGNUP_URL = "https://app.propteq.ai/auth/sign-up"
NAME_XPATH = "/html/body/div[1]/div//form//input[@name='name']"
EMAIL_XPATH = "/html/body/div[1]/div//form//input[@name='email']"
PASSWORD_XPATH = "/html/body/div[1]/div//form//input[@name='password']"
CONFIRM_PASSWORD_XPATH = "/html/body/div[1]/div//form//input[@name='confirm_password']"
TERMS_CHECKBOX_XPATH = "/html/body/div[1]/div//form//input[@name='isAgreed']"
SUBMIT_BUTTON_XPATH = "/html/body/div[1]//form//button[@type='submit']"

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

# Function to perform sign-up
def perform_signup(driver, name, email, password, confirm_password, agree_terms=True):
    driver.get(SIGNUP_URL)
    driver.find_element(By.XPATH, NAME_XPATH).send_keys(name)
    driver.find_element(By.XPATH, EMAIL_XPATH).send_keys(email)
    driver.find_element(By.XPATH, PASSWORD_XPATH).send_keys(password)
    driver.find_element(By.XPATH, CONFIRM_PASSWORD_XPATH).send_keys(confirm_password)
    if agree_terms:
        terms_checkbox = driver.find_element(By.XPATH, TERMS_CHECKBOX_XPATH)
        if not terms_checkbox.is_selected():
            terms_checkbox.click()
    driver.find_element(By.XPATH, SUBMIT_BUTTON_XPATH).click()

# Test Case: Valid Sign-Up
def test_valid_signup(driver):
    logging.info("Running test: Valid Sign-Up")
    try:
        perform_signup(driver, "John Doe", "johndoe@example.com", "SecurePass123!", "SecurePass123!")
        # Wait for success message or redirection (adjust based on actual behavior)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Account created')]")))
            logging.info("Valid sign-up test passed.")
        except TimeoutException:
            logging.error("Valid sign-up test failed. Success message not found.")
            assert False, "Valid sign-up test failed."
    except Exception as e:
        logging.error(f"Valid sign-up test failed. Error: {str(e)}")
        raise e

# Test Case: Invalid Email Format
def test_invalid_email(driver):
    logging.info("Running test: Invalid Email Format")
    try:
        perform_signup(driver, "John Doe", "invalid-email", "SecurePass123!", "SecurePass123!")
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Invalid email')]"))
        )
        assert error_message is not None, "Error message not displayed for invalid email."
        logging.info("Invalid email test passed.")
    except Exception as e:
        logging.error(f"Invalid email test failed. Error: {str(e)}")
        raise e

# Test Case: Password Mismatch
def test_password_mismatch(driver):
    logging.info("Running test: Password Mismatch")
    try:
        perform_signup(driver, "John Doe", "johndoe@example.com", "SecurePass123!", "WrongPass123!")
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Passwords do not match')]"))
        )
        assert error_message is not None, "Error message not displayed for password mismatch."
        logging.info("Password mismatch test passed.")
    except Exception as e:
        logging.error(f"Password mismatch test failed. Error: {str(e)}")
        raise e

# Test Case: Empty Fields
def test_empty_fields(driver):
    logging.info("Running test: Empty Fields")
    try:
        perform_signup(driver, "", "", "", "")
        error_messages = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(text(), 'required')]"))
        )
        assert len(error_messages) > 0, "Error messages not displayed for empty fields."
        logging.info("Empty fields test passed.")
    except Exception as e:
        logging.error(f"Empty fields test failed. Error: {str(e)}")
        raise e

# Test Case: Terms Not Agreed
def test_terms_not_agreed(driver):
    logging.info("Running test: Terms Not Agreed")
    try:
        perform_signup(driver, "John Doe", "johndoe@example.com", "SecurePass123!", "SecurePass123!", agree_terms=False)
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'must agree to terms')]"))
        )
        assert error_message is not None, "Error message not displayed for terms not agreed."
        logging.info("Terms not agreed test passed.")
    except Exception as e:
        logging.error(f"Terms not agreed test failed. Error: {str(e)}")
        raise e

# Test Case: SQL Injection
def test_sql_injection(driver):
    logging.info("Running test: SQL Injection")
    try:
        perform_signup(driver, "'; DROP TABLE users; --", "johndoe@example.com", "SecurePass123!", "SecurePass123!")
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Invalid input')]"))
        )
        assert error_message is not None, "SQL Injection test failed."
        logging.info("SQL Injection test passed.")
    except Exception as e:
        logging.error(f"SQL Injection test failed. Error: {str(e)}")
        raise e

# Test Case: AI-Generated Malicious Inputs
def test_ai_generated_inputs(driver):
    logging.info("Running test: AI-Generated Malicious Inputs")
    try:
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        if not OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not set in the environment variables.")
        openai_client = openai.OpenAI(api_key=OPENAI_API_KEY)
        prompt = "Generate a set of malicious inputs for a sign-up form (name, email, password)."
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        malicious_inputs = response.choices[0].message.content.split("\n")
        for input_set in malicious_inputs:
            name, email, password = input_set.split(",")[:3]
            logging.info(f"Testing AI-generated input: Name={name}, Email={email}, Password={password}")
            perform_signup(driver, name.strip(), email.strip(), password.strip(), password.strip())
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Invalid input')]")))
                logging.info(f"AI-generated input '{input_set}' failed to create an account as expected.")
            except TimeoutException:
                logging.error(f"AI-generated input '{input_set}' allowed account creation. This is a security issue.")
                assert False, f"AI-generated input '{input_set}' allowed account creation. This is a security issue."
    except Exception as e:
        logging.error(f"AI-generated inputs test failed. Error: {str(e)}")
        raise e

# Run tests
if __name__ == "__main__":
    pytest.main(["-v"])