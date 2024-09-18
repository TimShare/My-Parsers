import requests
from bs4 import BeautifulSoup
import openpyxl
from urllib3 import disable_warnings, exceptions

disable_warnings(exceptions.InsecureRequestWarning)

wb = openpyxl.load_workbook("/Users/timursarafiev/Documents/feron/feron_wb.xlsx")
sheet = wb.active

r = requests.Session()
r.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0)   Gecko/20100101 Firefox/69.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ru,en-US;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'}
for i in range(2, 159):
    id = str(sheet[f"A{i}"].value).split()[1]
    print(id, i)
    try:
        url = "https://shop.feron.ru" + BeautifulSoup(r.get(f"https://shop.feron.ru/search/?q={id}", verify=False).text,
                                                      "lxml"). \
            find("p", "name-product").find("a").get("href")
        bs = BeautifulSoup(r.get(url, verify=False).text, "lxml")
        chars = list(map(lambda x: x.find_all("p"), bs.find_all("div", "item-wrap")))
        w, l, h, form = 0, 0, 0, ""
        for char in chars:
            ch = list(map(lambda x: x.get_text(), char))
            if "Высота" in ch[0]:
                h = int(ch[1])
            if "Ширина" in ch[0]:
                w = int(ch[1])
            if "Глубина" in ch[0]:
                l = int(ch[1])
            if "Вид лампы" in ch[0]:
                form = ch[1]
        if "таблетка" not in form:
            sheet[f"T{i}"] = max(w, l, h)
            sheet[f"U{i}"] = min(w, l, h)
        else:
            sheet[f"T{i}"] = min(w, l, h)
            sheet[f"U{i}"] = max(w, l, h)
    except:
        print(id, "err")
wb.save("/Users/timursarafiev/Documents/feron/feron_wb.xlsx")