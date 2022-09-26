from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import re

def create_driver():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # Disable loading images for faster load
    prefs = {'profile.managed_default_content_settings.images': 2}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.minimize_window()
    return driver

def get_related_questions(keyword):
    driver = create_driver()
    driver.get(f'https://www.google.com/search?q={keyword}&hl=en')
    
    questions = driver.find_elements(By.CSS_SELECTOR, '.related-question-pair')

    if len(questions) == 0:
        driver.quit()
        return []

    result = []
    for question in questions:
        question_div = question.find_element(By.CSS_SELECTOR, 'div[data-q]')
        question_div.click()
        sleep(1.5)
        answer_content = question_div.find_elements(By.CSS_SELECTOR, 'div[jsslot] > div[data-ved] > div')

        if len(answer_content) == 3:
            answer_content.pop(0)

        title = question_div.get_attribute('data-q')

        try:
            source_url = answer_content[-1].find_element(By.CSS_SELECTOR, '.g a').get_attribute('href')
        except:
            try:
                source_url = answer_content[0].find_elements(By.CSS_SELECTOR, 'a')[-1].get_attribute('href')
            except:
                source_url = ''

        try:
            answer = answer_content[0].text.replace('\n', ' ')
        except:
            answer = ''
        
        answer = re.sub(r'\s+', ' ', answer)
        answer = re.sub(r'More items\.\.\.', '', answer)
    
        result.append({
            'keyword': keyword,
            'title': title, 
            'answer': answer, 
            'source_url': source_url
        })
    
    driver.quit()
    return result

if __name__ == '__main__':
    questions = get_related_questions('game')
    print(questions)
