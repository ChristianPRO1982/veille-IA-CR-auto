import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



def get_final_url(outer_url: str)->str:
    try:
        options = Options()
        options.headless = True
        service = Service('/usr/local/bin/chromedriver/chromedriver')  # Update with the correct path to chromedriver

        driver = webdriver.Chrome(service=service, options=options)
        driver.get(outer_url)
        time.sleep(1)
        final_url = driver.current_url
        driver.quit()
        return final_url
    
    except Exception as e:
        print('Try Error [get_final_url]: ', e)
        return False


def scan_outer_url()->bool:
    conn = sqlite3.connect('output/ai_tools.db')
    cursor = conn.cursor()

    query = """
SELECT outer_url
  FROM ai_tools_concat
 WHERE outer_url IS NOT NULL
 LIMIT 2
"""

    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        if get_final_url(row[0]) != False:
            print('Success')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    scan_outer_url()