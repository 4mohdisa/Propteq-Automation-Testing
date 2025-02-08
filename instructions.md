## Overview of Propteq Software
Propteq is software for real estate agents and brokers. It is designed to help agents and brokers manage their real estate business more efficiently.

### Features
- Property Management: Propteq provides a platform for agents and brokers to manage their properties and clients.
- Tenant Management: Propteq allows agents to manage tenants and their leases, ensuring that all tenants are properly accounted for.
- Payment Management: Propteq helps agents and brokers manage payment schedules for their clients, ensuring timely payments.
- Reporting and Analytics: Propteq provides detailed reporting and analytics, helping agents and brokers make informed decisions. 
- Property Sales: Propteq streamlines the process of selling properties, from listing to closing.
- Client Management: Propteq helps agents and brokers manage their clients, ensuring that all their information is up-to-date.
- Property Maintenance: Propteq helps agents and brokers manage property maintenance, ensuring that all properties are kept clean and in good condition.
- Property Listing: Propteq allows agents and brokers to list their properties for sale or rent, ensuring that all information is up-to-date and accurate.

## Getting Started with Automation Testing
I want to run the test cases using Python and Selenium and with integration with OpenAI's ChatGPT API, to create more detailed test cases, I want to test all the features for any scenarios for example I want to test the login test case, where I want to test if the user is able to login with valid credentials or not, I want to do deep testing where I put malicius scripts and see how the application responds, I want to test the email validation test case, where I want to test if the email is valid or not, I want to test all the feature for any kind of scenario, where I want to test if the user is able to perform any action or not, I want to do deep testing where I put malicius scripts and see how the application responds.

## Start creating test cases for Login page

```html
<header class="flex items-center justify-between p-4 lg:px-16 lg:py-6 2xl:px-24" data-sentry-component="AuthHeader"
    data-sentry-source-file="auth-wrapper-four.tsx"><a data-sentry-element="Link"
        data-sentry-source-file="auth-wrapper-four.tsx" href="/"><img alt="Propteq" data-sentry-element="Image"
            data-sentry-source-file="auth-wrapper-four.tsx" fetchPriority="high" width="6904" height="1576"
            decoding="async" data-nimg="1" class="w-32 dark:invert" style="color:transparent"
            src="/_next/static/media/propteq_dark.4046a052.svg" /></a></header>
<div class="flex w-full flex-col justify-center px-5">
    <div class="mx-auto w-full max-w-md py-12 md:max-w-lg lg:max-w-xl 2xl:pb-8 2xl:pt-2">
        <div class="flex flex-col items-center">
            <h2
                class="rizzui-title-h2 mb-7 text-center text-[28px] font-bold leading-snug md:text-3xl md:!leading-normal lg:mb-10 lg:text-4xl">
                Welcome Back! <br /> Sign in with your credentials.</h2>
        </div>
        <form noValidate="" data-sentry-element="Form" data-sentry-source-file="form.tsx" data-sentry-component="Form">
            <div class="space-y-5 lg:space-y-6">
                <div class="rizzui-input-root flex flex-col [&amp;&gt;label&gt;span]:font-medium"><label
                        class="block"><span class="rizzui-input-label block text-base mb-2">Email</span><span
                            class="rizzui-input-container flex items-center peer w-full transition duration-200 px-5 py-2.5 text-base h-14 leading-[56px] rounded-md bg-transparent [&amp;.is-focus]:ring-[0.6px] border border-gray-300 [&amp;_input::placeholder]:text-gray-500 hover:border-gray-1000 [&amp;.is-focus]:border-gray-1000 [&amp;.is-focus]:ring-gray-1000"><input
                                type="email" spellCheck="false" placeholder="Enter your email"
                                class="rizzui-input-field w-full border-0 bg-transparent p-0 focus:outline-none focus:ring-0"
                                style="font-size:inherit" required="" name="email" /></span></label></div>
                <div class="rizzui-password-root flex flex-col [&amp;&gt;label&gt;span]:font-medium"><label
                        class="block"><span class="rizzui-password-label block text-base mb-2">Password</span><span
                            class="rizzui-password-container flex items-center peer w-full transition duration-200 px-5 py-2.5 text-base h-14 leading-[56px] rounded-md bg-transparent [&amp;.is-focus]:ring-[0.6px] border border-gray-300 [&amp;_input::placeholder]:text-gray-500 hover:border-gray-1000 [&amp;.is-focus]:border-gray-1000 [&amp;.is-focus]:ring-gray-1000"><input
                                type="password" spellCheck="false" placeholder="Enter your password"
                                class="rizzui-password-field w-full border-0 bg-transparent p-0 focus:outline-none focus:ring-0"
                                style="font-size:inherit" required="" name="password" /><span role="button" tabindex="0"
                                class="rizzui-password-toggle-icon whitespace-nowrap leading-normal"><svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke-width="1.25" stroke="currentColor" class="h-5 w-5">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z">
                                    </path>
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88">
                                    </path>
                                </svg></span></span></label></div>
                <div class="flex items-center justify-end"><a
                        class="h-auto p-0 text-sm font-semibold text-gray-700 underline transition-colors hover:text-primary hover:no-underline"
                        href="/auth/forgot-password">Forgot Password?</a></div><button
                    class="rizzui-button inline-flex font-medium items-center justify-center active:enabled:translate-y-px focus:outline-none focus-visible:ring-2 focus-visible:ring-opacity-50 transition-colors duration-200 px-8 py-2.5 text-base h-14 rounded-md border border-transparent focus-visible:ring-offset-2 bg-gray-900 hover:enabled::bg-gray-800 active:enabled:bg-gray-1000 focus-visible:ring-gray-900/30 text-gray-0 w-full"
                    type="submit">Sign In</button>
            </div>
        </form>
        <p class="mt-6 text-center text-[15px] leading-loose text-gray-500 md:mt-7 lg:mt-9 lg:text-base">Don’t have an
            account?<!-- --> <a class="font-semibold text-gray-700 transition-colors hover:text-primary"
                data-sentry-element="Link" data-sentry-source-file="sign-in-form.tsx" href="/auth/sign-up">Sign Up</a>
        </p>
    </div>
</div>
<footer
    class="flex flex-col-reverse items-center justify-between px-4 py-5 lg:flex-row lg:px-16 lg:py-6 2xl:px-24 2xl:py-10"
    data-sentry-component="AuthFooter" data-sentry-source-file="auth-wrapper-four.tsx">
    <div class="text-center leading-relaxed text-gray-500 lg:text-start">© Copyright <!-- -->2025<!-- -->. All Rights
        Reserved.</div>
    <div class="-mx-2.5 flex items-center justify-end pb-3 font-medium text-gray-700 lg:w-1/2 lg:pb-0"><a
            class="px-2.5 py-1.5 transition-colors hover:text-primary" href="https://propteq.ai/contact/">Contact</a><a
            class="px-2.5 py-1.5 transition-colors hover:text-primary"
            href="https://propteq.ai/privacy-policy/">Privacy</a><a
            class="px-2.5 py-1.5 transition-colors hover:text-primary"
            href="https://propteq.ai/terms-and-condition/">Terms</a></div>
</footer>
</div>
<div style="position:fixed;z-index:9999;top:16px;left:16px;right:16px;bottom:16px;pointer-events:none"></div>
```

### Methods

-   ## Constants
    login_url = "https://app.propteq.ai/auth/sign-in"
    email_xpath = "//input[@name='email']"
    password_xpath = "//input[@name='password']"
    submit_button_xpath = "//button[@type='submit']"

-   ## Check for error messages (modify the XPath based on actual error message elements)
    error_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Please enter your email')]")))

-   ## Test case: Valid login
def test_valid_login(driver):
    print("Running test: Valid Login")
    if perform_login(driver, "isa@wemark.com.au", "WvwaroQCK8CCC#Ey"):
        print("Valid login test passed.")
    else:
        print("Valid login test failed.")
        capture_screenshot(driver, "valid_login_failure.png")

-   ## Test case: Invalid login
def test_invalid_login(driver):
    print("Running test: Invalid Login")
    if not perform_login(driver, "invalid_email@example.com", "wrong_password"):
        print("Invalid login test passed.")
    else:
        print("Invalid login test failed.")
        capture_screenshot(driver, "invalid_login_failure.png")

-   ## Test case: Empty fields
def test_empty_fields(driver):
    print("Running test: Empty Fields")
    try:
        driver.get(login_url)
        wait = WebDriverWait(driver, 10)
        driver.find_element(By.XPATH, email_xpath).send_keys("")
        driver.find_element(By.XPATH, password_xpath).send_keys("")
        driver.find_element(By.XPATH, submit_button_xpath).click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Please enter your email')]")))
        print("Empty fields test passed.")
    except Exception as e:
        print("Empty fields test failed. Error: ", str(e))
        capture_screenshot(driver, "empty_fields_failure.png")

-   ## Initialize the WebDriver
def initialize_driver():
    chrome_driver_path = "/opt/homebrew/bin/chromedriver"  # Mac Homebrew path
    chrome_options = Options()
    # Uncomment the line below if you want to run in headless mode
    # chrome_options.add_argument("--headless")
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

-   ## SQL Injection Test
def test_sql_injection(driver):
    print("Running test: SQL Injection")
    try:
        driver.get(login_url)
        wait = WebDriverWait(driver, 10)
        driver.find_element(By.XPATH, email_xpath).send_keys("'; DROP TABLE users; --")
        driver.find_element(By.XPATH, password_xpath).send_keys("password")
        driver.find_element(By.XPATH, submit_button_xpath).click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Please enter your email')]")))
        print("SQL Injection test passed.")
    except Exception as e:
        print("SQL Injection test failed. Error: ", str(e))
        capture_screenshot(driver, "sql_injection_failure.png")

-   ## OPEN AI API KEY
def test_openai_api_key(driver):
    print("Running test: OPEN AI API KEY")
    try:
        driver.get(login_url)
        wait = WebDriverWait(driver, 10)
        driver.find_element(By.XPATH, email_xpath).send_keys("'; DROP TABLE users; --")
        driver.find_element(By.XPATH, password_xpath).send_keys("password")
        driver.find_element(By.XPATH, submit_button_xpath).click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Please enter your email')]")))
        print("SQL Injection test passed.")
    except Exception as e:
        print("SQL Injection test failed. Error: ", str(e))
        capture_screenshot(driver, "sql_injection_failure.png")

OPEN_AI_API_KEY in .env file

-   ## Login successfully
if the login is successful, the user will be redirected to the agency page: https://app.propteq.ai/agency and xpath for agency page body element is "/html/body" you need to wait for the agency page to load.