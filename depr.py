import csv
import json

import requests
from bs4 import BeautifulSoup
from classes import Event


def translate_file_depr(filename):

    cinemas = ['Admiral Kino', 'Burg Kino', 'De France', 'Filmcasino', 'Filmhaus Kino Spittelberg', 'Gartenbaukino',
               'Schikaneder',
               'Stadtkino im KÃ¼nstlerhaus', 'Top Kino', 'Votiv Kino']

    cinemas_dict = {'Admiral Kino': [],
                    'Burg Kino': [],
                    'De France': [],
                    'Filmcasino': [],
                    'Filmhaus Kino Spittelberg': [],
                    'Gartenbaukino': [],
                    'Schikaneder': [],
                    'Stadtkino im KÃ¼nstlerhaus': [],
                    'Top Kino': [],
                    'Votiv Kino': []}

    def filter_items(events):
        clean_events = []
        for event in events:
            if event.place in cinemas:
                clean_events.append(event)

                matching = event.place

                match matching:
                    case 'Admiral Kino':
                        cinemas_dict['Admiral Kino'].append(event)
                    case 'Burg Kino':
                        cinemas_dict['Burg Kino'].append(event)
                    case 'De France':
                        cinemas_dict['De France'].append(event)
                    case 'Filmcasino':
                        cinemas_dict['Filmcasino'].append(event)
                    case 'Filmhaus Kino Spittelberg':
                        cinemas_dict['Filmhaus Kino Spittelberg'].append(event)
                    case 'Gartenbaukino':
                        cinemas_dict['Gartenbaukino'].append(event)
                    case 'Schikaneder':
                        cinemas_dict['Schikaneder'].append(event)
                    case 'Stadtkino im KÃ¼nstlerhaus':
                        cinemas_dict['Stadtkino im KÃ¼nstlerhaus'].append(event)
                    case 'Top Kino':
                        cinemas_dict['Top Kino'].append(event)
                    case 'Votiv Kino':
                        cinemas_dict['Votiv Kino'].append(event)

        return clean_events

    # Adresse der Webseite
    url = 'https://www.film.at/kinoprogramm/wien'
    headers = {'Accept-Language': 'de-DE;q=0.8,de;q=0.7'}

    # GET-Request ausführen
    response = requests.get(url, headers=headers)

    # BeautifulSoup HTML-Dokument aus dem Quelltext parsen
    # html2 = BeautifulSoup(response.text, 'html.parser')

    with open('./input/' + filename) as fp:
        html = BeautifulSoup(fp, 'html.parser')

    movie_accordeons = html.find_all('accordeon', class_='accordeon ng-star-inserted')

    items = []
    for accordeon in movie_accordeons:

        title = accordeon.find('div', class_='accordeon-title').text.strip()
        events = accordeon.find_all('div', class_='filterList-results-item ng-star-inserted')

        event_items = []
        for event in events:
            event_location = event.find('div', class_='filterList-results-key').text.strip()
            event_time = event.find('div', class_='filterList-results-value').text.strip()
            event_items.append(Event(title, event_location, event_time))

        event_items_cleaned = filter_items(event_items)

        if len(event_items_cleaned) >= 1:
            items.extend(event_items_cleaned)

    with open('output/' + filename.replace('html', 'json'), 'w') as outfile:
        outfile.write('[')
        for event in items:
            outfile.write(json.dumps(event.__dict__, ensure_ascii=False))
            if event != items[-1]:
                outfile.write(',')
        outfile.write(']')

