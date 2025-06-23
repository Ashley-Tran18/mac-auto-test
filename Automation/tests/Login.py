from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver (make sure you installed the right ChromeDriver)
driver = webdriver.Chrome()

# Open the login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Replace with the actual login URL

# wait for the page to load
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Wait for the dashboard to load after login
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
)

# Check login success (based on page URL or element)
if "dashboard" in driver.current_url:
    print("✅ Login successful!")
else:
    print("❌ Login may have failed.")

# Close the browser
driver.quit()
