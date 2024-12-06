from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
import time

def get_final_url_with_selenium(url):
    driver = None
    try:
        # Configuration du driver
        options = Options()
        options.headless = True  # Exécute sans interface graphique
        driver_path = "/usr/local/bin/chromedriver"  # Remplacez par le chemin réel
        
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        
        # Ouvrir l'URL
        driver.get(url)
        time.sleep(1)  # Attendre les redirections ou scripts dynamiques
        
        # Obtenir l'URL finale
        final_url = driver.current_url
        return final_url
    except Exception as e:
        print(f"Erreur : {e}")
        return None
    finally:
        if driver:
            driver.quit()


# scan json file and get final url
def scan_json_and_get_final_urls(json_file_path, out_file):
    try:
        with open(out_file, 'r') as file:
            data = json.load(file)
        
        links = []
        for item in data:
            links.append(item['link'])

    except:
        links = []

    with open(json_file_path, 'r') as file:
        data = json.load(file)

    ai_tools = []

    count = 0
    for item in data:
        if 'link' in item:
            if item['link'] not in links:
                count += 1

                dict_ai_tool = {}
                dict_ai_tool['category'] = item['category']
                dict_ai_tool['title'] = item['title']
                dict_ai_tool['description'] = item['description']
                dict_ai_tool['tags'] = item['tags']
                dict_ai_tool['link'] = item['link']
                dict_ai_tool['type'] = item['type']

                url = item['link']
                final_url = get_final_url_with_selenium(url)
                print(f"Original URL: {url} -> Final URL: {final_url}")
                dict_ai_tool['final_url'] = final_url

                ai_tools.append(dict_ai_tool)

                if count > 3:
                    break
            
            else:
                print(f"URL already scanned: {item['link']}")

                dict_ai_tool = {}
                dict_ai_tool['category'] = item['category']
                dict_ai_tool['title'] = item['title']
                dict_ai_tool['description'] = item['description']
                dict_ai_tool['tags'] = item['tags']
                dict_ai_tool['link'] = item['link']
                dict_ai_tool['type'] = item['type']
                dict_ai_tool['final_url'] = item['final_url']   

                ai_tools.append(dict_ai_tool)
    
    with open(out_file, 'w') as outfile:
        json.dump(ai_tools, outfile, indent=4)

json_file_path = 'ai_tools.json'
out_file = 'final_ai_tools.json'
scan_json_and_get_final_urls(json_file_path, out_file)