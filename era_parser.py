import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.load_workbook("/Users/timursarafiev/Documents/era/era.xlsx")
sheet = wb.active
row_count = sheet.max_row

r = requests.Session()

for i in range(2, row_count):
    etm_code = sheet[f"B{i}"].value
    try:
        _response = r.get(f"https://www.eraworld.ru/search?q={etm_code}", verify=False)
        bs = BeautifulSoup(_response.text, "lxml")
        url = bs.find("div", "search-section").find("a").get("href")

        page = r.get(url, verify=False)
        bs = BeautifulSoup(page.text, "lxml")
        chars = list(map(lambda x: x.get_text().replace("\n", ""), bs.find_all("div", "row")))
        vs, form, cv, analog, potok, diam, power = [0, 0, 0, 0, 0, 0, 0]
        for char in chars:
            if "Высота" in char:
                vs = char[len("Высота") + 1:]
            if "Форма колбы" in char:
                form = char[len("Форма колбы") + 1:]
            if "Цветовая температура, К" in char:
                cv = char[len("Цветовая температура, К") + 1:]
            if "Аналог лампы накаливания" in char:
                analog = char[len("Аналог лампы накаливания") + 1:]
            if "Световой поток, Лм" in char:
                potok = char[len("Световой поток, Лм") + 1:]
            if "Диаметр" in char:
                diam = char[len("Диаметр") + 1:]
            if "Мощность" in char:
                power = char[len("Мощность") + 1:]
        sheet[f"L{i}"] = form
        sheet[f"O{i}"] = cv
        sheet[f"P{i}"] = analog
        sheet[f"R{i}"] = potok
        sheet[f"T{i}"] = diam
        sheet[f"Z{i}"] = vs
        sheet[f"AA{i}"] = diam
        sheet[f"AE{i}"] = diam
    except:
        print(etm_code)

wb.save("/Users/timursarafiev/Documents/era/era.xlsx")

