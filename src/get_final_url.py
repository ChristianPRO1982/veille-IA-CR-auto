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
        service = Service('/usr/local/bin/chromedriver/chromedriver')

        driver = webdriver.Chrome(service=service, options=options)
        driver.get(outer_url)
        time.sleep(0.5)
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
SELECT id, outer_url
  FROM ai_tools_concat
 WHERE outer_url IS NOT NULL
   AND processed = 0
 LIMIT 100
"""

    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        final_url = get_final_url(row[1])
        if final_url != False:
            print(row[1], "=>", final_url)

            query = f"""
UPDATE ai_tools_concat
   SET final_url = '{final_url}',
       processed = 1
 WHERE id = {row[0]}
"""
            cursor.execute(query)
            conn.commit()

    conn.close()


if __name__ == "__main__":
    scan_outer_url()