import json

import requests
from bs4 import BeautifulSoup

from classes import Event, EventEncoder


def translate_file(filename):
    cinemas = ['Admiral Kino', 'Burg Kino', 'De France', 'Filmcasino', 'Filmhaus Kino Spittelberg', 'Gartenbaukino',
               'Schikaneder', 'Stadtkino im Künstlerhaus', 'Top Kino', 'Votiv Kino']

    cinemas_dict = {'Admiral Kino': [],
                    'Burg Kino': [],
                    'De France': [],
                    'Filmcasino': [],
                    'Filmhaus Kino Spittelberg': [],
                    'Gartenbaukino': [],
                    'Schikaneder': [],
                    'Stadtkino im Künstlerhaus': [],
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
                    case 'Stadtkino im Künstlerhaus':
                        cinemas_dict['Stadtkino im Künstlerhaus'].append(event)
                    case 'Top Kino':
                        cinemas_dict['Top Kino'].append(event)
                    case 'Votiv Kino':
                        cinemas_dict['Votiv Kino'].append(event)

        return clean_events

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
        json_object = json.dumps(cinemas_dict, indent=4, cls=EventEncoder)
        outfile.write(json_object)
