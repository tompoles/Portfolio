import csv
from typing import List

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


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
        # 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xobec=507423&xvyber=8102',
        ]

def main():
    infos = []
    elections = []
    for url in URLS:
        answer = get_answer(url)
        parsed = pull_data(answer)
        header_div = parsed.find_all('table', id='ps311_t1', class_='table')
        election_div = parsed.find_all('div', class_='t2_470')
        rows = find_row(election_div)
        election = [election_info(row) for row in rows]
        info = county_info(header_div)
        print(election, info)
        infos.append(info)
        elections.append(election)
    save_csv_2(infos,elections)

def get_answer(url):
    return requests.get(url)

def pull_data(ans):
    return bs(ans.text, "html.parser")

def find_row(tables):
    return [
        row
        for table in tables
        for row in table.find_all('tr')[2:]
    ]

def county_info(parsed):
    for contain in parsed:
        people = contain.find('td',class_='cislo', headers='sa2').text
        is_env = contain.find('td',class_='cislo', headers='sa3').text
        submitted = contain.find('td',class_='cislo', headers='sa5').text
        return {
            "Volici v seznamu":people,
            "Vydané obálky":is_env,
            "Platné hlasy":submitted
        }
def election_info(tr) -> dict:
        party = tr.find_all("td")[1].text
        votes = tr.find_all('td')[2].text
        return {
            "PARTY": party,
            "VOTES": votes
        }

def save_csv_2(data: List[dict], data2):
    with open('election1.csv', 'a',) as csv_file:
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

        for data_row, data2_row in zip(data, data2):
            row_dict = data_row
            for party_votes in data2_row:
                row_dict[party_votes["PARTY"]] = party_votes["VOTES"]

            writer.writerow(row_dict)


df1 = pd.read_csv('election1.csv')
df2 = pd.read_csv('election_data.csv')

df = df1.merge(df2, on='Obec')

if __name__ == '__main__':
    main()
