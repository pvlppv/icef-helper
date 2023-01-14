import time
import os, fnmatch

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService

from loader import db_sql

def files_smartlms():
    while True:
        # calculus
        options1 = webdriver.ChromeOptions()
        options1.add_argument('--headless')
        options1.add_argument('--no-sandbox')
        options1.add_argument('--disable-dev-shm-usage')
        options1.add_experimental_option("prefs", {
            # "download.default_directory": r"/Users/pavelpopov/Downloads/Calculus",
            "download.default_directory": r"/root/bot/media/Calculus",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        # service = ChromeService(executable_path='/Users/pavelpopov/Downloads/chromedriver')
        service = ChromeService(executable_path='/root/bot/chromedriver')
        driver = webdriver.Chrome(service=service, options=options1)
        driver.maximize_window()
        driver.get('http://www.python.org')
        assert "Python" in driver.title

        username = 'pgpopov_1@edu.hse.ru'
        password = 'W1qU@TkUj9'
        driver.get('https://smartedu.hse.ru/login?target=/')
        driver.find_element(By.CLASS_NAME, 'hse-Button__text').click()
        driver.find_element(By.NAME, 'UserName').send_keys(username)
        driver.find_element(By.NAME, 'Password').send_keys(password)
        driver.find_element(By.CLASS_NAME, 'submit').click()
        driver.get('https://smartedu.hse.ru/course/0/133271')
        driver.implicitly_wait(10)
        # driver.find_element(By.XPATH, "//*[starts-with(text(),'Week 01')]").click()
        sections = driver.find_elements(By.CLASS_NAME, 'Section_Section__T6CM2')
        for section in sections:
            ActionChains(driver).move_to_element(section).perform()
            section.click()

        elements = driver.find_elements(By.TAG_NAME, 'a')
        for element in elements:
            href = element.get_attribute('href')
            if href and href.startswith('https://edu.hse.ru/tokenpluginfile.php'):
                ActionChains(driver).move_to_element(element).perform()
                file_name = element.text
                if db_sql.calculus_exists(calculus=file_name):
                    continue
                else:
                    db_sql.add_calculus(calculus=file_name)
                    element.click()
                    time.sleep(1)
            else:
                pass
        time.sleep(5)
        driver.quit()
        print('calculus done')

        # statistics
        options2 = webdriver.ChromeOptions()
        options2.add_argument('--headless')
        options2.add_argument('--no-sandbox')
        options2.add_argument('--disable-dev-shm-usage')
        options2.add_experimental_option("prefs", {
            "download.default_directory": r"/root/bot/media/Statistics",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        # ICEFHelper_service = ChromeService(executable_path='/Users/pavelpopov/Downloads/chromedriver')
        service = ChromeService(executable_path='/root/bot/chromedriver')
        driver = webdriver.Chrome(service=service, options=options2)
        driver.maximize_window()
        driver.get('http://www.python.org')
        assert "Python" in driver.title

        username = 'pgpopov_1@edu.hse.ru'
        password = 'W1qU@TkUj9'
        driver.get('https://edu.hse.ru/login/hselogin.php')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div[1]/a').click()
        driver.find_element(By.NAME, 'UserName').send_keys(username)
        driver.find_element(By.NAME, 'Password').send_keys(password)
        driver.find_element(By.CLASS_NAME, 'submit').click()

        # lectures
        driver.get('https://edu.hse.ru/mod/folder/view.php?id=559584')
        driver.implicitly_wait(10)
        elements_lectures = driver.find_elements(By.TAG_NAME, 'a')
        for element in elements_lectures:
            href = element.get_attribute('href')
            if href and href.startswith('https://edu.hse.ru/pluginfile.php'):
                ActionChains(driver).move_to_element(element).perform()
                file_name = element.text
                if db_sql.statistics_exists(statistics=file_name):
                    continue
                else:
                    db_sql.add_statistics(statistics=file_name)
                    element.click()
                    time.sleep(1)
            else:
                pass
        time.sleep(5)

        # home assignments
        driver.get('https://edu.hse.ru/mod/folder/view.php?id=559586')
        driver.implicitly_wait(10)
        elements_ha = driver.find_elements(By.TAG_NAME, 'a')
        for element in elements_ha:
            href = element.get_attribute('href')
            if href and href.startswith('https://edu.hse.ru/pluginfile.php'):
                ActionChains(driver).move_to_element(element).perform()
                file_name = element.text
                if db_sql.statistics_exists(statistics=file_name):
                    continue
                else:
                    db_sql.add_statistics(statistics=file_name)
                    element.click()
                    time.sleep(1)
            else:
                pass
        time.sleep(5)

        # exams
        driver.get('https://edu.hse.ru/mod/folder/view.php?id=604427')
        driver.implicitly_wait(10)
        elements_ha = driver.find_elements(By.TAG_NAME, 'a')
        for element in elements_ha:
            href = element.get_attribute('href')
            if href and href.startswith('https://edu.hse.ru/pluginfile.php'):
                ActionChains(driver).move_to_element(element).perform()
                file_name = element.text
                if db_sql.statistics_exists(statistics=file_name):
                    continue
                else:
                    db_sql.add_statistics(statistics=file_name)
                    element.click()
                    time.sleep(1)
            else:
                pass
        time.sleep(5)

        # lyulko
        driver.get('https://edu.hse.ru/mod/folder/view.php?id=539699')
        driver.implicitly_wait(10)
        elements_ha = driver.find_elements(By.TAG_NAME, 'a')
        for element in elements_ha:
            href = element.get_attribute('href')
            if href and href.startswith('https://edu.hse.ru/pluginfile.php'):
                ActionChains(driver).move_to_element(element).perform()
                file_name = element.text
                if db_sql.statistics_exists(statistics=file_name):
                    continue
                else:
                    db_sql.add_statistics(statistics=file_name)
                    element.click()
                    time.sleep(1)
            else:
                pass
        time.sleep(5)

        # books
        driver.get('https://edu.hse.ru/mod/folder/view.php?id=565867')
        driver.implicitly_wait(2)
        elements_ha = driver.find_elements(By.TAG_NAME, 'a')
        for element in elements_ha:
            href = element.get_attribute('href')
            if href and href.startswith('https://edu.hse.ru/pluginfile.php'):
                ActionChains(driver).move_to_element(element).perform()
                file_name = element.text
                if db_sql.statistics_exists(statistics=file_name):
                    continue
                else:
                    db_sql.add_statistics(statistics=file_name)
                    element.click()
                    time.sleep(1)
            else:
                pass
        time.sleep(10)
        driver.quit()
        print('statistics done')

        # microeconomics
        options3 = webdriver.ChromeOptions()
        options3.add_argument('--headless')
        options3.add_argument('--no-sandbox')
        options3.add_argument('--disable-dev-shm-usage')
        options3.add_experimental_option("prefs", {
            "download.default_directory": r"/root/bot/media/Microeconomics",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        # ICEFHelper_service = ChromeService(executable_path='/Users/pavelpopov/Downloads/chromedriver')
        service = ChromeService(executable_path='/root/bot/chromedriver')
        driver = webdriver.Chrome(service=service, options=options3)
        driver.maximize_window()
        driver.get('http://www.python.org')
        assert "Python" in driver.title

        username = 'pgpopov_1@edu.hse.ru'
        password = 'W1qU@TkUj9'
        driver.get('https://smartedu.hse.ru/login?target=/')
        driver.find_element(By.CLASS_NAME, 'hse-Button__text').click()
        driver.find_element(By.NAME, 'UserName').send_keys(username)
        driver.find_element(By.NAME, 'Password').send_keys(password)
        driver.find_element(By.CLASS_NAME, 'submit').click()
        driver.get('https://smartedu.hse.ru/course/0/133269')
        driver.implicitly_wait(10)
        # driver.find_element(By.XPATH, "//*[starts-with(text(),'Week 01')]").click()
        sections = driver.find_elements(By.CLASS_NAME, 'Section_Section__T6CM2')
        for section in sections:
            ActionChains(driver).move_to_element(section).perform()
            section.click()

        elements = driver.find_elements(By.TAG_NAME, 'a')
        for element in elements:
            href = element.get_attribute('href')
            if href and href.startswith('https://edu.hse.ru/tokenpluginfile.php'):
                ActionChains(driver).move_to_element(element).perform()
                file_name = element.text
                if db_sql.microeconomics_exists(microeconomics=file_name):
                    continue
                else:
                    db_sql.add_microeconomics(microeconomics=file_name)
                    element.click()
                    time.sleep(1)
            else:
                pass
        time.sleep(5)
        driver.quit()
        print('microeconomics done')

        # history
        options4 = webdriver.ChromeOptions()
        options4.add_argument('--headless')
        options4.add_argument('--no-sandbox')
        options4.add_argument('--disable-dev-shm-usage')
        options4.add_experimental_option("prefs", {
            "download.default_directory": r"/root/bot/media/History",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        # ICEFHelper_service = ChromeService(executable_path='/Users/pavelpopov/Downloads/chromedriver')
        service = ChromeService(executable_path='/root/bot/chromedriver')
        driver = webdriver.Chrome(service=service, options=options4)
        driver.maximize_window()
        driver.get('http://www.python.org')
        assert "Python" in driver.title

        username = 'pgpopov_1@edu.hse.ru'
        password = 'W1qU@TkUj9'
        driver.get('https://smartedu.hse.ru/login?target=/')
        driver.find_element(By.CLASS_NAME, 'hse-Button__text').click()
        driver.find_element(By.NAME, 'UserName').send_keys(username)
        driver.find_element(By.NAME, 'Password').send_keys(password)
        driver.find_element(By.CLASS_NAME, 'submit').click()
        driver.get('https://smartedu.hse.ru/course/0/122992')
        driver.implicitly_wait(10)
        sections = driver.find_elements(By.CLASS_NAME, 'Section_Section__T6CM2')
        for section in sections:
            ActionChains(driver).move_to_element(section).perform()
            section.click()

        elements = driver.find_elements(By.TAG_NAME, 'a')
        for element in elements:
            href = element.get_attribute('href')
            if href and href.startswith('https://edu.hse.ru/tokenpluginfile.php'):
                ActionChains(driver).move_to_element(element).perform()
                file_name = element.text
                if db_sql.history_exists(history=file_name):
                    continue
                else:
                    db_sql.add_history(history=file_name)
                    element.click()
                    time.sleep(1)
            else:
                pass
        time.sleep(5)
        driver.quit()
        print('history done')

        # timetable timetable
        options5 = webdriver.ChromeOptions()
        options5.add_argument('--headless')
        options5.add_argument('--no-sandbox')
        options5.add_argument('--disable-dev-shm-usage')
        options5.add_experimental_option("prefs", {
            "download.default_directory": r"/root/bot/media/Timetable/Timetable",
            # "download.default_directory": r"/Users/pavelpopov/Downloads/Timetable/Timetable",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        # service = ChromeService(executable_path='/Users/pavelpopov/Downloads/chromedriver')
        service = ChromeService(executable_path='/root/bot/chromedriver')
        driver = webdriver.Chrome(service=service, options=options5)
        driver.maximize_window()
        driver.get('http://www.python.org')
        assert "Python" in driver.title

        username = 'pgpopov_1@edu.hse.ru'
        password = 'W1qU@TkUj9'
        driver.get('https://smartedu.hse.ru/login?target=/')
        driver.find_element(By.CLASS_NAME, 'hse-Button__text').click()
        driver.find_element(By.NAME, 'UserName').send_keys(username)
        driver.find_element(By.NAME, 'Password').send_keys(password)
        driver.find_element(By.CLASS_NAME, 'submit').click()
        driver.get('https://smartedu.hse.ru/course/0/132869')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//*[text()='Timetable']").click()

        element = driver.find_element(By.PARTIAL_LINK_TEXT, 'The 1st course')
        path = '/root/bot/media/Timetable/Timetable'
        # path = '/Users/pavelpopov/Downloads/Timetable/Timetable'
        # files = os.listdir(path)
        # paths = [os.path.join(path, basename) for basename in files]
        # last_file = max(paths, key=os.path.getctime)
        # file_name = os.path.basename(last_file)
        # if db_sql.timetable_exists(timetable=file_name):
        #     pass
        # else:
        db_sql.delete_timetable()
        for root, dirs, files in os.walk(path):
            for f in files:
                os.unlink(os.path.join(root, f))
                element.click()
                db_sql.add_timetable(timetable=element.text)
        time.sleep(5)
        driver.quit()
        print('timetable done')

        # timetable office hours
        options6 = webdriver.ChromeOptions()
        options6.add_argument('--headless')
        options6.add_argument('--no-sandbox')
        options6.add_argument('--disable-dev-shm-usage')
        options6.add_experimental_option("prefs", {
            # "download.default_directory": r"/Users/pavelpopov/Downloads/Timetable/Office hours",
            "download.default_directory": r"/root/bot/media/Timetable/Office hours",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        # service = ChromeService(executable_path='/Users/pavelpopov/Downloads/chromedriver')
        service = ChromeService(executable_path='/root/bot/chromedriver')
        driver = webdriver.Chrome(service=service, options=options6)
        driver.maximize_window()
        driver.get('http://www.python.org')
        assert "Python" in driver.title

        username = 'pgpopov_1@edu.hse.ru'
        password = 'W1qU@TkUj9'
        driver.get('https://smartedu.hse.ru/login?target=/')
        driver.find_element(By.CLASS_NAME, 'hse-Button__text').click()
        driver.find_element(By.NAME, 'UserName').send_keys(username)
        driver.find_element(By.NAME, 'Password').send_keys(password)
        driver.find_element(By.CLASS_NAME, 'submit').click()
        driver.get('https://smartedu.hse.ru/course/0/132869')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//*[text()='Timetable']").click()

        element = driver.find_element(By.PARTIAL_LINK_TEXT, 'Office')
        # path = '/Users/pavelpopov/Downloads/Timetable/Office hours'
        path = '/root/bot/media/Timetable/Office hours'
        db_sql.delete_office_hours()
        for root, dirs, files in os.walk(path):
            for f in files:
                os.unlink(os.path.join(root, f))
                element.click()
                db_sql.add_office_hours(office_hours=element.text)
        time.sleep(5)
        driver.quit()
        print('office hours done')

        # timetable optional courses
        options7 = webdriver.ChromeOptions()
        options7.add_argument('--headless')
        options7.add_argument('--no-sandbox')
        options7.add_argument('--disable-dev-shm-usage')
        options7.add_experimental_option("prefs", {
            # "download.default_directory": r"/Users/pavelpopov/Downloads/Timetable/Optional courses",
            "download.default_directory": r"/root/bot/media/Timetable/Optional courses",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        # service = ChromeService(executable_path='/Users/pavelpopov/Downloads/chromedriver')
        service = ChromeService(executable_path='/root/bot/chromedriver')
        driver = webdriver.Chrome(service=service, options=options7)
        driver.maximize_window()
        driver.get('http://www.python.org')
        assert "Python" in driver.title

        username = 'pgpopov_1@edu.hse.ru'
        password = 'W1qU@TkUj9'
        driver.get('https://smartedu.hse.ru/login?target=/')
        driver.find_element(By.CLASS_NAME, 'hse-Button__text').click()
        driver.find_element(By.NAME, 'UserName').send_keys(username)
        driver.find_element(By.NAME, 'Password').send_keys(password)
        driver.find_element(By.CLASS_NAME, 'submit').click()
        driver.get('https://smartedu.hse.ru/course/0/132869')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//*[text()='Timetable']").click()

        element = driver.find_element(By.PARTIAL_LINK_TEXT, 'Optional')
        # path = "/Users/pavelpopov/Downloads/Timetable/Optional courses"
        path = '/root/bot/media/Timetable/Optional courses'
        db_sql.delete_optional_courses()
        for root, dirs, files in os.walk(path):
            for f in files:
                os.unlink(os.path.join(root, f))
                element.click()
                db_sql.add_optional_courses(optional_courses=element.text)
        time.sleep(5)
        driver.quit()
        print('optional courses done')

        # timetable exams timetable
        options8 = webdriver.ChromeOptions()
        options8.add_argument('--headless')
        options8.add_argument('--no-sandbox')
        options8.add_argument('--disable-dev-shm-usage')
        options8.add_experimental_option("prefs", {
            # "download.default_directory": r"/Users/pavelpopov/Downloads/Timetable/Exams timetable",
            "download.default_directory": r"/root/bot/media/Timetable/Exams timetable",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        # service = ChromeService(executable_path='/Users/pavelpopov/Downloads/chromedriver')
        service = ChromeService(executable_path='/root/bot/chromedriver')
        driver = webdriver.Chrome(service=service, options=options8)
        driver.get('http://www.python.org')
        assert "Python" in driver.title

        username = 'pgpopov_1@edu.hse.ru'
        password = 'W1qU@TkUj9'
        driver.get('https://smartedu.hse.ru/login?target=/')
        driver.find_element(By.CLASS_NAME, 'hse-Button__text').click()
        driver.find_element(By.NAME, 'UserName').send_keys(username)
        driver.find_element(By.NAME, 'Password').send_keys(password)
        driver.find_element(By.CLASS_NAME, 'submit').click()
        driver.get('https://smartedu.hse.ru/course/0/132869')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//*[text()='Timetable']").click()

        element = driver.find_element(By.PARTIAL_LINK_TEXT, 'Exams')
        # path = "/Users/pavelpopov/Downloads/Timetable/Exams timetable"
        path = '/root/bot/media/Timetable/Exams timetable'
        db_sql.delete_exams_timetable()
        for root, dirs, files in os.walk(path):
            for f in files:
                os.unlink(os.path.join(root, f))
                element.click()
                db_sql.add_exams_timetable(exams_timetable=element.text)
        time.sleep(5)
        driver.quit()
        print('exams timetable done')
        time.sleep(30)


if __name__ == '__main__':
    files_smartlms()
