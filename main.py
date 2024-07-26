from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

# Akceptowanie ekranu wyboru wyszukiwarki, jeśli się pojawi
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Zgadzam się')]"))
    )
    agree_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Zgadzam się')]")
    agree_button.click()
    print("Kliknięto przycisk 'Zgadzam się'")
except:
    print("Ekran wyboru wyszukiwarki nie pojawił się")

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
    )
    print("Element wyszukiwania znaleziony")
except Exception as e:
    print("Błąd: Element wyszukiwania nie został znaleziony", e)
    driver.quit()
    exit()

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("tech with tim" + Keys.ENTER)

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='g']"))
    )
    print("Wyniki wyszukiwania załadowane")
except Exception as e:
    print("Błąd: Wyniki wyszukiwania nie zostały załadowane", e)
    driver.quit()
    exit()

# Wyświetl tytuły wszystkich linków na stronie wyników wyszukiwania
try:
    links = driver.find_elements(By.XPATH, "//h3")
    for link in links:
        print(link.text)
except Exception as e:
    print("Błąd: Nie można pobrać linków", e)
    driver.quit()
    exit()

# Kliknij na link "Tech With Tim"
try:
    tech_with_tim_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
    tech_with_tim_link.click()
    print("Kliknięto na link 'Tech With Tim'")
except Exception as e:
    print("Błąd: Link 'Tech With Tim' nie został znaleziony", e)

time.sleep(15)
driver.quit()
