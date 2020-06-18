#  Project 3 - Election Scraper

import csv
from typing import List

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102"

def main():
    answer = get_answer()
    parsed = pull_data(answer)
    table = find_tab(parsed)
    rows = find_row(table)
    villages = [villages_info(row) for row in rows]
    print(villages)
    save_csv(villages)
    # merger("election1.csv", "election_data.csv")

def get_answer():
    return requests.get(URL)

def pull_data(ans):
    return bs(ans.text, "html.parser")

def find_tab(cont):
    return cont.find('div', class_='t3')

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
    with open("election1.csv", "w", newline="") as csv_file:
        header = ["Cislo", "Obec",]
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        for index, _ in enumerate(data):
            writer.writerow(
                {
                    "Cislo": data[index]["cislo"],
                    "Obec": data[index]["Obec"]

                }
            )


# def merger(csv1, csv2):
#     first = pd.read_csv(csv1)
#     second = pd.read_csv(csv2)
#     merged = pd.merge(first, second, how='right', on='Voliči v seznamu')
#     merged.to_csv('merged.csv', index=False)


if __name__ == '__main__':
    main()