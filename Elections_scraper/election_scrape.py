#  Project 3 - Election Scraper

import csv
from typing import List

import requests
from bs4 import BeautifulSoup as bs
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


def main():
    answer = get_answer()
    parsed = pull_data(answer)
    table = find_tab(parsed)
    # print(table)
    rows =  find_row(table)
    voters = []
    save_csv(rows)


    # print(rows)
    # elections = [election_info(row) for row in rows]
    # print(elections)
    # table_2 = find_tab2(parsed)
    # election_info_2 = [election_info2(r) for r in rows_2]
    # print(election_info_2)

def get_answer():
    return requests.get(URLS)

def pull_data(ans):
    return bs(ans.text, "html.parser")

def find_tab(cont):
    return cont.find('table', {'class':'table'})

def find_row(tabl):
    return tabl.find_all('tr')[2:]

def election_info(tr):
    try:
        voters = tr.find_all("td")[3].text
        envelopes = tr.find_all("td")[4].text
        votes = tr.find_all("td")[6].text
        return {
            "Voliči v seznamu": voters,
            "Vydané obálky": envelopes,
            "Platné hlasy": votes
        }
    except AttributeError:
        print(f'Wrong assigned indexes')

def find_tab2(cont):
    return cont.find('div', {'class':'t2_470'})

def find_row2(tabl):
    return tabl.find_all('tr')[2:]

def election_info2(tr):
    try:
        ODS = tr.find_all("td")[2].text
        RD_VU = tr.find_all("td")[2].text
        COS = tr.find_all("td")[2].text
        # CSSD =
        # RC =
        # STAN =
        # KSCM =
        # SZ =
        # ROZ =
        # SSO =
        # BLOK =
        # ODA =
        # CPS =
        # CNF =
        # REU =
        # TOP_09 =
        # ANO =
        # DV =
        # Rep =
        # KrestU =
        # CSNS =
        # REAL =
        # SPORT =
        # DSS =
        # SPD =
        # SPO =
        return {
            "Občanská demokratická strana": ODS,
            "Řád národa - Vlastenecká unie": RD_VU,
            "CESTA ODPOVĚDNÉ SPOLEČNOSTI": COS
        }
    except AttributeError:
        print(f'Wrong assigned indexes')

def save_csv(data: List[dict]):
    with open("election_2", "w", newline="") as csv_file:
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
                    "Voliči v seznamu" : data[index]["Voliči v seznamu"],
                    "Vydané obálky": data[index]["Vydané obálky"],
                    "Platné hlasy": data[index]["Platné hlasy"],
                    "Občanská demokratická strana": data2[index]["Občanská demokratická strana"],
                    'Řád národa - Vlastenecká unie': data2[index]["Řád národa - Vlastenecká unie"],
                    'CESTA ODPOVĚDNÉ SPOLEČNOSTI': data2[index]["CESTA ODPOVĚDNÉ SPOLEČNOSTI"],
                    'Česká str.sociálně demokrat.': data2[index]["Česká str.sociálně demokrat."],
                    'Radostné Česko': data2[index]["Radostné Česko"],
                    'STAROSTOVÉ A NEZÁVISLÍ': data2[index]["STAROSTOVÉ A NEZÁVISLÍ"],
                    'Komunistická str.Čech a Moravy': data2[index]["Komunistická str.Čech a Moravy"],
                    'Strana zelených': data2[index]["Strana zelených"],
                    'ROZUMNÍ-stop migraci,diktát.EU': data2[index]["ROZUMNÍ-stop migraci,diktát.EU"],
                    'Strana svobodných občanů': data2[index]["Strana svobodných občanů"],
                    'Blok proti islam.-Obran.domova': data2[index]["Blok proti islam.-Obran.domova"],
                    'Občanská demokratická aliance': data2[index]["Občanská demokratická aliance"],
                    'Česká pirátská strana': data2[index]["Česká pirátská strana"],
                    'Česká národní fronta': data2[index]["Česká národní fronta"],
                    'Referendum o Evropské unii': data2[index]["Referendum o Evropské unii"],
                    'TOP 09': data2[index]["TOP 09"],
                    'ANO 2011': data2[index]["ANO 2011"],
                    'Dobrá volba 2016': data2[index]["Dobrá volba 2016"],
                    'SPR-Republ.str.Čsl. M.Sládka': data2[index]["SPR-Republ.str.Čsl. M.Sládka"],
                    'Křesť.demokr.unie-Čs.str.lid.': data2[index]["Křesť.demokr.unie-Čs.str.lid."],
                    'Česká strana národně sociální': data2[index]["Česká strana národně sociální"],
                    'REALISTÉ': data2[index]["REALISTÉ"],
                    'SPORTOVCI': data2[index]["SPORTOVCI"],
                    'Dělnic.str.sociální spravedl.': data2[index]["Dělnic.str.sociální spravedl."],
                    'Svob.a př.dem.-T.Okamura (SPD)': data2[index]["Svob.a př.dem.-T.Okamura (SPD)"],
                    'Strana Práv Občanů': data2[index]["Strana Práv Občanů"]


                }
            )

if __name__ == '__main__':
    main()
#
#
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