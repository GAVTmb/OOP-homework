import requests
from operator import itemgetter

base_url = 'https://akabab.github.io/superhero-api/api/all.json'


def files_list():
    intelligence_dict = {}
    resault = requests.get(base_url).json()
    superheros_list = ['Hulk', 'Captain America', 'Thanos']
    for hero in resault:
        for key, values in hero.items():
            if values in superheros_list:
                intelligence_dict[values] = hero['powerstats']['intelligence']
    sort_hero = sorted(intelligence_dict.items(), key=itemgetter(1))
    print(sort_hero[-1][0])


files_list()
