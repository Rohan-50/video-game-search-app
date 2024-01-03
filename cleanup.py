# imports
# from howlongtobeatpy import HowLongToBeat
# from langchain.chat_models import ChatOpenAI
# from langchain.chains import ConversationChain
# from langchain.memory import ConversationBufferMemory
# import openai
# import os
# import requests
# import json

# getting video game data from API
""" api_url = "https://api.rawg.io/api/games?key=b299f11fbcf546f582963c5841705189&platforms=187,18,1,186,7&stores=2,3,6&dates=2019-01-01,2024-12-31&page_size=100000&page=1"
response = requests.get(api_url)
data = response.json()['results']

page = 2
for page in range(2, 99):
    api_url = "https://api.rawg.io/api/games?key=b299f11fbcf546f582963c5841705189&platforms=187,18,1,186,7&stores=2,3,6&dates=2019-01-01,2024-12-31&page_size=100000&page=" + \
        str(page)
    response = requests.get(api_url)
    new_data = response.json()['results']
    data.extend(new_data)
    print(str(page) + " added to list")

with open('game_list.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# Specify the path to your JSON file
json_file_path = 'game_list.json'
with open(json_file_path, 'r') as file:
    game_data = json.load(file)

for game in game_data:
    api_url = "https://api.rawg.io/api/games/" + \
        str(game['id']) + "?key=b299f11fbcf546f582963c5841705189"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        game.update(response.json())
        print(str(game['id']) + " details have been added")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching API data for game {game['id']}: {e}")

with open('game_details.json', 'w', encoding='utf-8') as f:
    json.dump(game_data, f, ensure_ascii=False, indent=4)

# Specify the path to your JSON file

for game in game_data:
    if 'stores' in game:
        for store in game['stores']:
            store.pop('id', None)
        for store_info in game['stores']:
            store_info.update(store_info.pop('store'))
    print("[" + str(counter) + "] " + str(game['name']) + " updated")
    counter += 1 """

# testing HowLongToBeat API
# results = HowLongToBeat().search(game_data[0]['name'])
