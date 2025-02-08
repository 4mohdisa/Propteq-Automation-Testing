from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
chrome_driver_path = "/opt/homebrew/bin/chromedriver"  # Mac Homebrew path
chrome_options = Options()
# Comment out or remove the headless mode
# chrome_options.add_argument("--headless")  # Optional: Run in headless mode
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

# URL, credentials, and locators
login_url = "https://app.propteq.ai/auth/sign-in"
email = "isa@wemark.com.au"
password = "WvwaroQCK8CCC#Ey"

email_xpath = "//input[@name='email']"
password_xpath = "//input[@name='password']"
submit_button_xpath = "//button[@type='submit']"

try:
    # Navigate to the login page
    driver.get(login_url)

    # Wait for the email field to load
    wait = WebDriverWait(driver, 10)
    email_field = wait.until(EC.presence_of_element_located((By.XPATH, email_xpath)))
    email_field.send_keys(email)

    # Wait for the password field to load
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, password_xpath)))
    password_field.send_keys(password)

    # Wait for the submit button and click it
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
    submit_button.click()

    # Wait for a post-login indicator (modify based on actual behavior)
    wait.until(EC.url_contains("dashboard"))  # Adjust the condition to match the logged-in state

    print("Sign-in test passed: Successfully logged in.")
except Exception as e:
    print(f"Sign-in test failed: {e}")
finally:
    # Close the browser
    driver.quit()
