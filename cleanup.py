# imports
# from howlongtobeatpy import HowLongToBeat
# from langchain.chat_models import ChatOpenAI
# from langchain.chains import ConversationChain
# from langchain.memory import ConversationBufferMemory
# import openai
# import os
# import requests
import json

# getting video game data from API
""" api_url = "https://api.rawg.io/api/games?key=b299f11fbcf546f582963c5841705189&page=1&page_size=10000000&stores=1,2,3,6,11"
response = requests.get(api_url)
data = response.json()['results']

page = 2
for page in range(2, 251):
    api_url = "https://api.rawg.io/api/games?key=b299f11fbcf546f582963c5841705189&page=" + str(page) + "&page_size=10000000&stores=1,2,3,6,11"
    response = requests.get(api_url)
    new_data = response.json()['results']
    data.extend(new_data)
    print(str(page) + "added to list")

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4) """

# openai.api_key = os.getenv("OPEN_API_KEY")
# openai.api_key = "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"

# Specify the path to your JSON file
json_file_path = 'updated_data.json'
with open(json_file_path, 'r') as file:
    game_data = json.load(file)

for game in game_data:
    if 'tags' in game:
        for tag in game['tags']:
            del tag["slug"]
            del tag["games_count"]
    if 'parent_platforms' in game:
        del game['parent_platforms']

with open('new_data.json', 'w', encoding='utf-8') as f:
    json.dump(game_data, f, ensure_ascii=False, indent=4)

# testing HowLongToBeat API
# results = HowLongToBeat().search(game_data[0]['name'])
