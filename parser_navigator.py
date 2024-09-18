import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.load_workbook("/Users/timursarafiev/Downloads/brand.navigator.xlsx")
sheet = wb.active

r = requests.Session()

for i in range(2, 86):
    try:
        diam, dl = 0, 0
        code = sheet[f"A{i}"].value.split()[0]
        start_url = f"https://navigator-light.ru/search.html?search={code}"
        get_new_url = "https://navigator-light.ru/" + BeautifulSoup(r.get(start_url).text, "lxml").find("a",
                                                                                                        "page_link").get(
            "href")
        get_page = "https://navigator-light.ru/" + BeautifulSoup(r.get(get_new_url).text, "lxml").find("a", "BolunBtn").get(
            "href")
        chars = BeautifulSoup(r.get(get_page).text, "lxml").find("tbody").find_all("tr")
        for j in chars:
            char = j.get_text().split()[0]
            if "Диаметр" in char:
                diam = char[7:]
                print(diam)
            if "Длина" in char:
                dl = char[5:]
                print(dl)
        sheet[f"T{i}"] = dl
        sheet[f"U{i}"] = diam
    except:
        print(i)

wb.save("/Users/timursarafiev/Desktop/navigator.xlsx")
