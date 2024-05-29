# Взаимодействие с динамическим контентом. Использование Seleniu
from selenium import webdriver
from selenium.webdriver import Keys
# Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By
# Библиотека с поиском элементов на сайте
import time

browser = webdriver.Chrome()

browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
while True:
    try:
        # Находим окно поиска
        search_box = browser.find_element(By.ID, "searchInput")
        item = input("Что Вы хотите найти? ")
        # Прописываем ввод текста в поисковую строку.
        search_box.send_keys(item)
        search_box.send_keys(Keys.RETURN)
        break
    except:
        print("Произошла ошибка поиска строки ввода.")

while True:
    try:
        my_choice = input(
            '''Что дельше?
1) листать параграфы текущей статьи 
2) перейти на одну из связанных страниц 
3) выйти
Ваш выбор: ''')
        if my_choice == "1":
            paragraphs = browser.find_elements(By.TAG_NAME, "p")
            # Выводим параграфы текущей статьи
            for p in paragraphs:
                print(p.text)
                my_input = input("Нажмите Enter для продолжения или любую другую клавишу для выхода")
                if my_input != "":
                    break
        elif my_choice == "2":
            hatnotes = []
            for element in browser.find_elements(By.TAG_NAME, "div"):
                cl = element.get_attribute("class")
                if cl == "hatnote navigation-not-searchable":
                    hatnotes.append(element)
            # Для получения ссылки мы должны найти на сайте тег "a" внутри тега "div"
            if len(hatnotes) == 0:
                print("Ccылка не найдена.")
            else:
                link = hatnotes[0].find_element(By.TAG_NAME, "a").get_attribute("href")
                browser.get(link)
                paragraphs = browser.find_elements(By.TAG_NAME, "p")
                print(paragraphs[0].text)
        elif my_choice == "3":
            break
    except:
        print("Произошла ошибка работы со статьёй.")

browser.quit()
