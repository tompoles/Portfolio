#  Project 3 - Election Scraper

import csv
from typing import List

import requests
from bs4 import BeautifulSoup as bs

URL = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102"

URLS = ['https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598011&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598020&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=511633&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598038&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598046&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=511935&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598062&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598071&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598089&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=552542&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598101&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=511951&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=552607&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598135&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598003&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598143&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598160&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=512192&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=511986&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=552631&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=512176&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598232&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598691&xvyber=8102',
        'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598259&xvyber=8102',
        '']

def main():
    answer = get_answer()
    parsed = pull_data(answer)
    table = find_tab(parsed)
    rows = find_row(table)
    villages = [villages_info(row) for row in rows]
    print(villages)
    save_csv(villages)

def get_answer():
    return requests.get(URL)

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
#
# def election_info(data):


def save_csv(data: List[dict]):
    with open("election.csv", "w", newline="") as csv_file:
        header = ["Cislo", "Obec","Voliči v seznamu", "Vydané obálky", "Platné hlasy", "Občanská demokratická strana",
                  'Řád národa - Vlastenecká unie', 'CESTA ODPOVĚDNÉ SPOLEČNOSTI', 'Česká str.sociálně demokrat.',
                  'Radostné Česko', 'STAROSTOVÉ A NEZÁVISLÍ', 'STAROSTOVÉ A NEZÁVISLÍ', 'Komunistická str.Čech a Moravy',
                  'Strana zelených', 'ROZUMNÍ-stop migraci,diktát.EU', 'Strana svobodných občanů',
                  'Blok proti islam.-Obran.domova', 'Občanská demokratická aliance', 'Česká pirátská strana',
                  'Česká národní fronta', 'Referendum o Evropské unii', 'TOP 09', 'ANO 2011', 'Dobrá volba 2016',
                  'SPR-Republ.str.Čsl. M.Sládka', 'Křesť.demokr.unie-Čs.str.lid.', 'Česká strana národně sociální',
                  'REALISTÉ', 'SPORTOVCI', 'Dělnic.str.sociální spravedl.', 'Svob.a př.dem.-T.Okamura (SPD)',
                  'Strana Práv Občanů']
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        for index, _ in enumerate(data):
            writer.writerow(
                {
                    "Cislo": data[index]["cislo"],
                    "Obec": data[index]["Obec"]

                }
            )

import prettify
from unicodedata import normalize


# URL = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102"

URLS = 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598011&xvyber=8102'
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598020&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=511633&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598038&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598046&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=511935&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598062&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598071&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598089&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=552542&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598101&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=511951&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=552607&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598135&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598003&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598143&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598160&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=512192&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=511986&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=552631&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=512176&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598232&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598691&xvyber=8102',
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=598259&xvyber=8102',


def second():
    answer = get_answer1()
    parsed = pull_data1(answer)
    header_div = parsed.find_all('table', id='ps311_t1', class_='table')
    election_div = parsed.find_all('div', class_='t2_470')
    rows = find_row1(election_div)
    election = [election_info(row) for row in rows]
    info = county_info(header_div)
    print(info, election)
    save_csv_2(info,election)
    # save_csv(election)

def get_answer1():
    return requests.get(URLS)

def pull_data1(ans):
    return bs(ans.text, "html.parser")

def find_row1(tabl):
    return tabl[0].find_all('tr')[2:]

def county_info(parsed):
    for contain in parsed:
        people = contain.find('td',class_='cislo', headers='sa2').text
        is_env = contain.find('td',class_='cislo', headers='sa3').text
        submitted = contain.find('td',class_='cislo', headers='sa5').text
        return [{
            "Volici v seznamu":people,
            "Vydané obálky":is_env,
            "Platné hlasy":submitted
        }]
def election_info(tr) -> dict:
        party = tr.find_all("td")[1].text
        votes = tr.find_all('td')[2].text
        return {
            "PARTY": party,
            "VOTES": votes,
        }

def save_csv_2(data: List[dict], data2):
    with open('election', 'a+', newline="") as csv_file:
        header = ['Volici v seznamu', 'Vydané obálky', 'Platné hlasy', "Občanská demokratická strana",
                  'Řád národa - Vlastenecká unie', 'CESTA ODPOVĚDNÉ SPOLEČNOSTI', 'Česká str.sociálně demokrat.',
                  'Radostné Česko', 'STAROSTOVÉ A NEZÁVISLÍ', 'STAROSTOVÉ A NEZÁVISLÍ', 'Komunistická str.Čech a Moravy',
                  'Strana zelených', 'ROZUMNÍ-stop migraci,diktát.EU', 'Strana svobodných občanů',
                  'Blok proti islam.-Obran.domova', 'Občanská demokratická aliance', 'Česká pirátská strana',
                  'Česká národní fronta', 'Referendum o Evropské unii', 'TOP 09', 'ANO 2011', 'Dobrá volba 2016',
                  'SPR-Republ.str.Čsl. M.Sládka', 'Křesť.demokr.unie-Čs.str.lid.', 'Česká strana národně sociální',
                  'REALISTÉ', 'SPORTOVCI', 'Dělnic.str.sociální spravedl.', 'Svob.a př.dem.-T.Okamura (SPD)',
                  'Strana Práv Občanů']
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        for index, _ in enumerate(data):
            writer.writerow(
                {
                 'Volici v seznamu': data[index]["Volici v seznamu"],
                 'Vydané obálky': data[index]["Vydané obálky"],
                 'Platné hlasy': data[index]["Platné hlasy"],
                 }
            )
            writer.writeheader()
            for index, _ in enumerate(data2):
                writer.writerow(
                    {
                    "Občanská demokratická strana": data2[index]["VOTES"],
                    'Řád národa - Vlastenecká unie': data2[index]["VOTES"],
                    'CESTA ODPOVĚDNÉ SPOLEČNOSTI': data2[index]["VOTES"],
                    }
                )


def save_csv(data):
    with open("myFile.csv", "a", newline="") as csv_file:
        header = ["Voliči v seznamu", "Vydané obálky", "Platné hlasy", "Občanská demokratická strana",
                  'Řád národa - Vlastenecká unie', 'CESTA ODPOVĚDNÉ SPOLEČNOSTI', 'Česká str.sociálně demokrat.',
                  'Radostné Česko', 'STAROSTOVÉ A NEZÁVISLÍ', 'STAROSTOVÉ A NEZÁVISLÍ', 'Komunistická str.Čech a Moravy',
                  'Strana zelených', 'ROZUMNÍ-stop migraci,diktát.EU', 'Strana svobodných občanů',
                  'Blok proti islam.-Obran.domova', 'Občanská demokratická aliance', 'Česká pirátská strana',
                  'Česká národní fronta', 'Referendum o Evropské unii', 'TOP 09', 'ANO 2011', 'Dobrá volba 2016',
                  'SPR-Republ.str.Čsl. M.Sládka', 'Křesť.demokr.unie-Čs.str.lid.', 'Česká strana národně sociální',
                  'REALISTÉ', 'SPORTOVCI', 'Dělnic.str.sociální spravedl.', 'Svob.a př.dem.-T.Okamura (SPD)',
                  'Strana Práv Občanů']
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        for index, _ in enumerate(data):
            writer.writerow(
                {
                    "Občanská demokratická strana": data[index]["VOTES"],
                    'Řád národa - Vlastenecká unie': data[index]["VOTES"],
                    'CESTA ODPOVĚDNÉ SPOLEČNOSTI': data[index]["VOTES"],
                    'Česká str.sociálně demokrat.': data[index]["Česká str.sociálně demokrat."],
                    'Radostné Česko': data[index]["Radostné Česko"],
                    'STAROSTOVÉ A NEZÁVISLÍ': data[index]["STAROSTOVÉ A NEZÁVISLÍ"],
                    'Komunistická str.Čech a Moravy': data[index]["Komunistická str.Čech a Moravy"],
                    'Strana zelených': data[index]["Strana zelených"],
                    'ROZUMNÍ-stop migraci,diktát.EU': data[index]["ROZUMNÍ-stop migraci,diktát.EU"],
                    'Strana svobodných občanů': data[index]["Strana svobodných občanů"],
                    'Blok proti islam.-Obran.domova': data[index]["Blok proti islam.-Obran.domova"],
                    'Občanská demokratická aliance': data[index]["Občanská demokratická aliance"],
                    'Česká pirátská strana': data[index]["Česká pirátská strana"],

                }
            )



if __name__ == '__main__':
    main()
    second()


