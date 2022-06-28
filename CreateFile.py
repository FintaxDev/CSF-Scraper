import json
import requests
from bs4 import BeautifulSoup

def Json(url:str, filename:str)->None:
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'
    page = requests.get(url, verify=False)
    try:
        if page.ok:
            soup = BeautifulSoup(page.text, 'lxml')
            dicTable = {}
            for Table in soup.find_all("tbody", class_="ui-datatable-data ui-widget-content"):
                dicRows = {}
                for Row in Table.children:
                    try:
                        dicRows[Row.find("span").text] = Row.text.replace(Row.find("span").text, "")
                        dicTable[Table.parent.parent.parent.parent.parent.parent.parent.parent.parent.find("li").text] = dicRows
                    except:
                        pass
            with open(filename, "w") as outfile:
                json.dump(dicTable, outfile, indent=4, ensure_ascii=False)
    except requests.exceptions.ConnectionError as exc:
        print(exc)
