
# Instagram Account Signup Automation

This Python script utilizes the Selenium library to automate the signup process on Instagram. It opens a Firefox browser, navigates to the Instagram signup page, fills in the required information, and submits the form.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Selenium
- GeckoDriver (Firefox WebDriver)

You can install Selenium using the following command:

```shell
pip install selenium
```

To download GeckoDriver, visit the [official website](https://github.com/mozilla/geckodriver/releases) and download the appropriate driver version for your Firefox browser. Make sure to place the driver executable in your system's PATH.

## Usage

1. Import the necessary libraries:
   ```python
   from selenium import webdriver
   from selenium.webdriver.common.by import By
   import time
   ```

2. Instantiate a WebDriver:
   ```python
   driver = webdriver.Firefox()
   ```

3. Navigate to the Instagram signup page:
   ```python
   driver.get("https://www.instagram.com/accounts/emailsignup/")
   ```

4. Fill in the signup form fields:
   ```python
   username = driver.find_element(By.NAME, "username")
   password = driver.find_element(By.NAME, "password")

   username.send_keys("your_username")
   password.send_keys("your_password")
   ```

5. Submit the form:
   ```python
   driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]").click()
   ```

6. Add necessary delays (using `time.sleep()`) to wait for the page to load or perform specific actions.

7. Close the WebDriver:
   ```python
   driver.quit()
   ```

Make sure to replace `"your_username"` and `"your_password"` with your desired username and password.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgments

The automation functionality in this script is made possible by the Selenium library. Thanks to the developers of Selenium for their contributions to the field.



1:  You have to download selenium from cmd command.     pip install selenium

2:  You should download Geckodriver from this link. Please download in assets, according to operating system.  :https://github.com/mozilla/geckodriver/releases

browser = webdriver.Firefox()     ("your Firefox driver path here")


3:  You need to identify it to the computer's path. For this, we click on the left at-advanced system settings-environment variables-path.
Right click on the geckodriver that we downloaded to the desktop and copy the location. And add it to the path where it says. That's it.


4:  You can run it with any ide you want. I'm using Vscode.


5:   You are now ready to open the file I sent you.



   
