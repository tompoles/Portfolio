import csv
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
    save_csv(villages)


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

def save_csv(data):
    with open("election1.csv", "w", newline="") as csv_file:
        header = ["Cislo", "Obec"]
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        for index, _ in enumerate(data):
            writer.writerow(
                {
                    "Cislo": data[index]["cislo"],
                    "Obec": data[index]["Obec"]
                }
            )
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
        ]

def second():
    infos = []
    elections = []
    for url in URLS:
        answer = get_answer_2(url)
        parsed = pull_data_2(answer)
        header_div = parsed.find_all('table', id='ps311_t1', class_='table')
        election_div = parsed.find_all('div', class_='t2_470')
        rows = find_row_2(election_div)
        election = [election_info(row) for row in rows]
        info = county_info(header_div)
        infos.append(info)
        elections.append(election)
        save_csv_2(infos,elections)


def get_answer_2(url):
    return requests.get(url)

def pull_data_2(ans):
    return bs(ans.text, "html.parser")

def find_row_2(tables):
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
    try:
        party = tr.find_all("td")[1].text
        votes = tr.find_all('td')[2].text
        return {
            "PARTY": party,
            "VOTES": votes
        }
    except AttributeError:
        print(f'Wrong assigned indexes')

def save_csv_2(data, data2):
    with open('election_data.csv', 'w',) as csv_file:
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

def cvs_merger(csv1, csv2):
    df1 = pd.read_csv(csv1)
    df2 = pd.read_csv(csv2)
    result = pd.concat([df1, df2], axis=1, ignore_index=False)
    result.to_csv("election.csv")

if __name__ == '__main__':
    main()
    second()
    cvs_merger('election1.csv', 'election_data.csv')