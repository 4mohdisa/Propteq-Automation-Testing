from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Initialize the WebDriver
def initialize_driver():
    chrome_driver_path = "/opt/homebrew/bin/chromedriver"  # Mac Homebrew path
    chrome_options = Options()
    # Uncomment the line below if you want to run in headless mode
    # chrome_options.add_argument("--headless")
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Function to perform login
def perform_login(driver, email, password):
    try:
        # Navigate to the login page
        driver.get(login_url)
        wait = WebDriverWait(driver, 10)

        # Enter email
        email_field = wait.until(EC.presence_of_element_located((By.XPATH, email_xpath)))
        email_field.clear()
        email_field.send_keys(email)

        # Enter password
        password_field = wait.until(EC.presence_of_element_located((By.XPATH, password_xpath)))
        password_field.clear()
        password_field.send_keys(password)

        # Click submit button
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
        submit_button.click()

        # Wait for post-login indicator (e.g., URL change or dashboard element)
        wait.until(EC.url_contains("dashboard"))  # Adjust based on actual behavior
        return True
    except Exception as e:
        print(f"Login failed: {e}")
        return False

# Test case: Valid login
def test_valid_login(driver):
    print("Running test: Valid Login")
    if perform_login(driver, "isa@wemark.com.au", "WvwaroQCK8CCC#Ey"):
        print("Valid login test passed.")
    else:
        print("Valid login test failed.")
        capture_screenshot(driver, "valid_login_failure.png")

# Test case: Invalid login
def test_invalid_login(driver):
    print("Running test: Invalid Login")
    if not perform_login(driver, "invalid_email@example.com", "wrong_password"):
        print("Invalid login test passed.")
    else:
        print("Invalid login test failed.")
        capture_screenshot(driver, "invalid_login_failure.png")

# Test case: Empty fields
def test_empty_fields(driver):
    print("Running test: Empty Fields")
    try:
        driver.get(login_url)
        wait = WebDriverWait(driver, 10)

        # Click submit without entering any data
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
        submit_button.click()

        # Check for error messages (modify the XPath based on actual error message elements)
        error_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Please enter your email')]")))
        if error_message:
            print("Empty fields test passed.")
        else:
            print("Empty fields test failed.")
            capture_screenshot(driver, "empty_fields_failure.png")
    except Exception as e:
        print(f"Empty fields test failed: {e}")
        capture_screenshot(driver, "empty_fields_failure.png")

# Capture screenshot on failure
def capture_screenshot(driver, filename):
    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    screenshot_path = os.path.join(screenshots_dir, filename)
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")

# Main execution
if __name__ == "__main__":
    # Constants
    login_url = "https://app.propteq.ai/auth/sign-in"
    email_xpath = "//input[@name='email']"
    password_xpath = "//input[@name='password']"
    submit_button_xpath = "//button[@type='submit']"

    # Initialize driver
    driver = initialize_driver()

    try:
        # Run test cases
        test_valid_login(driver)
        test_invalid_login(driver)
        test_empty_fields(driver)
    finally:
        # Close the browser
        driver.quit()