#  Project 3 - Election Scraper

import csv
from typing import List

import requests
from bs4 import BeautifulSoup as bs

URL1 = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102"

def main():
    answer = get_answer()
    parsed = pull_data(answer)
    table = find_tab(parsed)
    rows = find_row(table)
    villages = [villages_info(row) for row in rows]
    save_csv(villages)

def get_answer():
    return requests.get(URL1)

def pull_data(ans):
    return bs(ans.text, "html.parser")

def find_tab(cont):
    return cont.find('table', {'class':'table'})

def find_row(tabl):
    return tabl.find_all('tr')[2:]

def villages_info(tr):
    try:
        num = tr.find_all("td")[0].text
        location = tr.find_all("td")[1].text
        return {
            "cislo": num,
            "Obec": location
        }
    except AttributeError:
        print(f'Wrong assigned indexes')

def save_csv(data: List[dict]):
    with open("election", "w", newline="") as csv_file:
        header = ["CISLO", "OBEC"]
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        for index, _ in enumerate(data):
            writer.writerow(
                {
                    "CISLO": data[index]["cislo"],
                    "OBEC": data[index]["Obec"],
                }
            )


if __name__ == '__main__':
    main()
