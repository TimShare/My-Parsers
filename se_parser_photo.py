import requests
from bs4 import BeautifulSoup
import os


def save_img(photo_url, id, mkdir_needs=0, k=0):
    if not mkdir_needs:
        p = requests.get(photo_url)
        out = open(f"/Users/timursarafiev/Desktop/kosmos_photo/{id}.jpg", "wb")
        out.write(p.content)
        out.close()
    else:
        path_to_folder = f"/Users/timursarafiev/Desktop/se/parsed"
        os.mkdir(f"{path_to_folder}/{id}") if not os.path.exists(
            f"{path_to_folder}/{id}") else None
        p = requests.get(photo_url)
        out = open(f"{path_to_folder}/{id}/{k}.jpg", "wb")
        out.write(p.content)
        out.close()


def get_url(url_search):
    url_search = f"https://shop.systeme.ru/catalogsearch/result/?q={arc}"
    searc_text = r.get(url_search)
    bs = BeautifulSoup(searc_text.text, "lxml")
    url_to_item = bs.find("a", "product-item__title js-name").get("href")
    return url_to_item


arcs = ['BC10-001B', 'BC10-002B', 'BA10-001B', 'PC16-044B', 'PA16-007B', 'PC16-108B', 'PA16-008B', 'PA16-003B',
        'BLNRA010211', 'VS56-234-B', 'VS16-133-B', 'VA16-131-B', 'BA10-041B', 'PC16-003B', 'ATN540145', 'RS16-136-B',
        'RS16-134-B', 'PA16-005B', 'RA16-133-B', 'BLNRA010201', 'PA16-044B', 'RS16-236-B', 'BA10-004B', 'PA16-004B',
        'PA16-001B', 'RA16-238-B', 'PC16-007B', 'PA16-244C', 'BLNRA010213', 'RA16-237-B', 'PA16-244B', 'BLNRA011211',
        'BA10-002B', 'ATN540126', 'BLNRA011411', 'ATN540170', 'RA16-238I-B', 'ATN540111', 'RA10-131-B', 'BLNRA010116',
        'ATN540174', 'BLNVA061011', 'BLNRA010111', 'BA10-005B', 'PC16-004B', 'BLNVA101011', 'ATN544074', 'PA16-008D',
        'BLNRA010216', 'BA10-001K', 'ATN544013', 'PA16-011B', 'ATN540113', 'BA10-041C', 'ATN544011', 'BLNRA010311',
        'BLNRA010101', 'PA16-044C', 'RS16-231-B', 'BLNRA011311', 'PA16-007K', 'BA10-042B', 'ATN000351', 'PC16-001B',
        'ATN000511', 'PA16-009B', 'BA10-046B', 'RS16-235-B', 'BLNRA000111', 'RS10-132-B', 'ATN000251', 'ATN540161',
        'BA10-001D', 'RA16-411M-B', 'PC16-008B', 'ATN544070', 'BA10-002K', 'RPVA-B', 'ATN543045', 'BLNRA000311',
        'BLNIA045001', 'VA56-232-B', 'ATN544045', 'BLNVA061001', 'BLNVA105011', 'PA16-003K', 'ATN000189', 'BA10-002D',
        'ATN540151', 'BLNVA101001', 'ATN000551', 'ATN544026', 'ATN000751', 'BLNRA010113', 'ATN544051', 'BLNVA065011',
        'A56-029-BI', 'ATN000451', 'ATN001052', 'BLNRA000211', 'VA16-137-B', 'ATN543026', 'PA16-205B', 'ATN001012',
        'ATN000153', 'ATN000113', 'RS10-184-B', 'RA32-211R-B', 'BA10-005D', 'PC16-044K', 'PC16-003K', 'GSL000291',
        'KOMC-001B', 'BC10-005B', 'A56-007-B', 'PC16-005B', 'VS5U-218-B', 'BC10-006K', 'ATN001013', 'S56-039-BI',
        'ATN543061', 'PC16-007K', 'BA10-006B', 'PA16-001K', 'ATN000115', 'BC10-003B', 'BLNRA010215', 'ATN543051',
        'VS16-135-B', 'BA10-006D', 'PA16-008K', 'GSL000713', 'GSL000411', 'PA16-004K', 'PA16-002B', 'RA10-164-B',
        'BLNVA065111', 'BLNRA000216', 'ATN543011', 'BLNRA000114', 'PA16-011K', 'BLNVA105015', 'GSL000653', 'BA10-004D',
        'ATN000720', 'BLNVA101111', 'GSL000453', 'TVA-002K', 'PA16-009K', 'BC10-006B', 'BLNRS000026', 'GSL000253',
        'BLNVA101014', 'ATN000222', 'ATN000441', 'BC10-002K', 'BC10-005K', 'GSL001031', 'ATN000420', 'BA10-045B',
        'GSL001211', 'PA16-012B', 'GSL000491', 'ATN000147', 'BLNVA061101', 'ATN000385', 'BLNRA011117', 'TVA-002D',
        'ATN543015', 'GSL000831', 'ATN000226', 'GSL000885KK', 'GSL000951', 'BLNVS010506', 'BPA16-204B', 'ATN000246',
        'GSL000426', 'BLNVS006111', 'BLNVA065002', 'GSL000551', 'BLNVS010507', 'ATN543013', 'BLNRA010202', 'GSL000185',
        'BLNRA010312', 'GSL000485KK', 'GSL000853', 'ATN000526', 'ATN543019', 'BLNRA000217', 'GSL000285KK',
        'BLNVS010504', 'BLNRA000212', 'S16-053-BI', 'BLNRA010315', 'ATN000244', 'GSL000197', 'GSL000812', 'BLNVS010105',
        'BLNRA011315', 'PA16-105D', 'BLNSR003231', 'BC10-001K', 'BLNVA105115', 'GSL000231', 'BLNVS010502', 'BC10-003K',
        'BLNRA000417', 'PA16-009D', 'BLNTA000011', 'GSL000746', 'BLNRA000415', 'BLNIA011002', 'BLNRS001126',
        'BLNVA065112', 'BLNRS001123', 'BLNRA111114', 'ATN000326', 'BLNTS000015', 'BLNIS011005', 'BLNIS045005',
        'BLNRA011417', 'BLNVA105112', 'BLNRA011217', 'GSL000612', 'BLNVS010112', 'BLNVS010505', 'BLNIS011001',
        'BLNVA105014', 'GSL001443', 'GSL001251', 'BLNRA011313', 'BA10-046C', 'GSL000924', 'BLNVA061102', 'BLNRA000316',
        'VS110-153-1-86', 'RA16-233-B', 'VS210-152-1-86', 'VS110-154-7-86', 'RA16-213-BI', 'BLNVS006511', 'BLNIS045006',
        'VS510-251-7-86', 'GSL000748', 'VS110-153-7-86', 'RS16-212-B', 'RA10-137I-B', 'RA16-237I-B', 'BLNVA101117',
        'BLNVS100504', 'RS16-211-B', 'BLNVS010116', 'RS16-230-B', 'RA16-213-B', 'GSL000897', 'GSL000697',
        'VS110-153-28', 'GSL000797', 'BLNRS000022', 'BLNIS045111', 'VS510-251-2-86', 'RIN-144K5E-BE', 'RS10-135-B',
        'RS16-212-BI', 'RA16-213M-B', 'VS210-152-6-86', 'RIN-145K5E-BE', 'VS510-252-28', 'RA16-214M-B', 'BLNRS001017',
        'S16-053-B', 'A16-046-B', 'S56-039-B', 'RA10-125B-BI', 'RA16-227B-BI', 'VA56-225B-BI', 'VA1U-112-B',
        'RA16-112B-BI', 'RS16-126B-BI', 'VS510-251-1-86', 'RA16-239-B', 'VS410-253-2-86', 'RA16-214-B', 'RA16-239I-B',
        'VS510-252-5-86', 'RIN-144K5E-B', 'RA10-164M-B', 'S56-043-BI', 'RS16-004-BI', 'RS10-184-BI', 'VA16-131I-B',
        'VA56-232I-B', 'RA10-131I-B', 'RA16-133I-B', 'RAT-1S3-B', 'RT-4S3-B', 'A16-046I-B', 'A56-029-B',
        'RS16-152-5-86', 'RSI-152T-6-86', 'VS616-051-28', 'A16-046M-B', 'VA5U-214M-B', 'RS16-152-4-86', 'RS16-152B-28',
        'RS16-152B-2-86', 'RS16-152B-1-86', 'RSI-152T-2-86', 'RSI-152T-1-86', 'RS16-151-2-86', 'RS16-152-7-86',
        'A56-007-BI']

r = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
r.headers = headers
k = 0
for arc in arcs:
    url = get_url(f"https://shop.systeme.ru/catalogsearch/result/?q={arc}")
    bs = BeautifulSoup(r.get(url, headers=headers).text, "lxml")
    print(bs)
    urls_photos = bs.find_all("picture", "images-gallery__image slider-lazy webp lazy loaded")
    print(urls_photos)
    for k in range(len(urls_photos)):
        url_photo = urls_photos[k].find("img").get("src")
        save_img(url_photo, arc, 1, k)

    break
