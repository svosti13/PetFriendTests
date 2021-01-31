from selenium import webdriver  # подключение библиотеки
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest



@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(
        executable_path='C:\Program Files\webdriver\chromedriver.exe')  # получение объекта веб-драйвера для нужного браузера
    pytest.driver.get('http://petfriends1.herokuapp.com/login')
    yield
    pytest.driver.quit()


def test_cnt_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('s.svetlakov@live.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('12345678')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-deck")))

    pytest.driver.get('http://petfriends1.herokuapp.com/my_pets')
    names = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr')
    cnt = pytest.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]').text
    lines = cnt.split()
    print(lines[2])
    print(len(names))
    assert int(lines[2]) == len(names)


def test_pets_photo():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('s.svetlakov@live.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('12345678')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   pytest.driver.get('http://petfriends1.herokuapp.com/my_pets')
   names = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr')
   images = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr th img')
   k=0
   cnt = pytest.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]').text
   lines = cnt.split()
   cnt=int(lines[2])
   for i in range(len(names)):
      if images[i].get_attribute('src') != '':
         k+=1
   assert k>=cnt/2

def test_pets_alldata():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('s.svetlakov@live.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('12345678')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   pytest.driver.get('http://petfriends1.herokuapp.com/my_pets')
   names = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr td:nth-child(2)')
   tip = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr td:nth-child(3)')
   age = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr td:nth-child(4)')
   k=0
   cnt = pytest.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]').text
   lines = cnt.split()
   cnt=int(lines[2])
   for i in range(len(names)):
      assert names[i].text != ''
      assert tip[i].text != ''
      assert age[i].text != ''

def test_pets_uniqname():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('s.svetlakov@live.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('12345678')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   pytest.driver.get('http://petfriends1.herokuapp.com/my_pets')
   names = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr td:nth-child(2)')
   x=0
   for i in range(len(names) - 1):
      for j in range(i + 1, len(names)):
         if names[i].text == names[j].text:
            x=1
            quit()
   assert x == 0


def test_pets_uniqall():
   pytest.driver.implicitly_wait(10)
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('s.svetlakov@live.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('12345678')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   pytest.driver.get('http://petfriends1.herokuapp.com/my_pets')
   names = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr td:nth-child(2)')
   tip = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr td:nth-child(3)')
   age = pytest.driver.find_elements_by_css_selector('#all_my_pets table tbody tr td:nth-child(4)')
   uniq = 1
   for i in range(len(names) - 1):
      for j in range(i + 1, len(names)):
         if names[i].text == names[j].text:
            if tip[i].text == tip[j].text:
               if age[i].text == age[j].text:
                  uniq = 0
                  quit()
   assert uniq == 1