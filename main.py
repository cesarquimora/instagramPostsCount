from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from time import sleep as slp
import config

df = pd.read_csv('links.csv')
newDf = pd.DataFrame(columns=['username', 'link', 'conteo'])

username = config.username
password = config.password

timeout = 5

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36")
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
links = []
listaPublicaciones = []
sd = 0
c = True

driver.get('https://www.instagram.com/')
slp(timeout)
wait.until(EC.presence_of_element_located((By.NAME, 'username'))).send_keys(username)
wait.until(EC.presence_of_element_located((By.NAME, 'password'))).send_keys(password)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\_acan > .x9f619"))).click()
slp(timeout)

try:
  for i, row in enumerate(df.values.tolist()):
    print(f'Starting {row[0]}.')
    driver.get(row[1])
    slp(timeout)
    driver.set_window_size(1200, 742)
    wait = WebDriverWait(driver, 2)
    actions = ActionChains(driver)

    sd += 700
    driver.execute_script(f"window.scrollTo(0,{str(sd)})")

    slp(timeout)
    elements0 = wait.until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[@class=\'_ac7v  _al3n\']/div[@class=\'_aabd _aa8k  _al3l\']/a')))

    for element in elements0:
      if element.get_attribute("href") not in links:
        links.append(element.get_attribute("href"))
      else:
        pass
    while True:
      try:
        elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[@class=\'_ac7v  _al3n\']/div[@class=\'_aabd _aa8k  _al3l\']/a')))
      except:
        break
      try:
        if (elements[0].get_attribute("href") not in links) or (elements[-1].get_attribute("href") not in links):
          for element in elements:
            if element.get_attribute("href") not in links:
              links.append(element.get_attribute("href"))
          1/0
        else:    
          slp(5)
          if driver.execute_script("return window.pageYOffset;") == initial_position:
            pass
          else:
            1/0
      except:
        sd += 800
        initial_position = driver.execute_script("return window.pageYOffset;")
        driver.execute_script(f"window.scrollTo(0,{str(sd)})")
        slp(5)
      else:
        break
    newDf.loc[i] = [row[0], row[1], len(links)]
    print(f'{row[0]} added. With a total of {len(links)} of publications.')
    links = []
    slp(300)
except Exception as e:
  print(e)
  newDf.to_csv('linksRecorded.csv')
  driver.quit()
else:
  newDf.to_csv('linksRecorded.csv')
  driver.quit()