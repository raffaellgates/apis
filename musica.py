"""
Api para bucar a letra de musicas e tambem para validar se existe
"""

import requests

artist = 'The Beatles'
title =  'Hey Jude'
requisicao = requests.get('https://api.lyrics.ovh/v1/{}/{}'.format(artist, title))

data = requisicao.json()
print(data["lyrics"])
