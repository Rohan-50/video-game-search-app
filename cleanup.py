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
    json.dump(game_data, f, ensure_ascii=False, indent=4) """

# Specify the path to your JSON file
json_file_path = 'game_details.json'
with open(json_file_path, 'r') as file:
    game_data = json.load(file)

counter = 1

for game in game_data:
    game.pop('slug', None)
    game.pop('playtime', None)
    game.pop('tba', None)
    game.pop('suggestions_count', None)
    game.pop('score', None)
    game.pop('clip', None)
    game.pop('user_game', None)
    game.pop('parent_platforms', None)
    game.pop('screenshots_count', None)
    game.pop('movies_count', None)
    game.pop('creators_count', None)
    game.pop('achievements_count', None)
    game.pop('parent_achievements_count', None)
    game.pop('reddit_name', None)
    game.pop('reddit_description', None)
    game.pop('reddit_logo', None)
    game.pop('reddit_count', None)
    game.pop('twitch_count', None)
    game.pop('youtube_count', None)
    game.pop('alternative_names', None)
    game.pop('parents_count', None)
    game.pop('additions_count', None)
    game.pop('game_series_count', None)
    game.pop('description_raw', None)
    if 'platforms' in game:
        for platform in game['platforms']:
            if 'platform' in platform:
                platform['platform'].pop('slug', None)
                platform['platform'].pop('image', None)
                platform['platform'].pop('year_end', None)
                platform['platform'].pop('year_start', None)
                platform['platform'].pop('games_count', None)
                platform['platform'].pop('image_background', None)
                platform.pop('released_at', None)
                platform.pop('requirements', None)
    if 'stores' in game:
        for store in game['stores']:
            if 'store' in store:
                store['store'].pop('slug', None)
                store['store'].pop('games_count', None)
                store['store'].pop('image_background', None)
                store.pop('url', None)
    if 'tags' in game:
        for tag in game['tags']:
            tag.pop('slug', None)
            tag.pop('language', None)
            tag.pop('games_count', None)
            tag.pop('image_background', None)
    if 'genres' in game:
        for genre in game['genres']:
            genre.pop('slug', None)
            genre.pop('games_count', None)
            genre.pop('image_background', None)
    if 'metacritic_platforms' in game:
        for platform in game['metacritic_platforms']:
            if 'platform' in platform:
                platform['platform'].pop('platform', None)
                platform['platform'].pop('slug', None)
    if 'developers' in game:
        for developer in game['developers']:
            developer.pop('slug', None)
            developer.pop('games_count', None)
            developer.pop('image_background', None)
    if 'publishers' in game:
        for publisher in game['publishers']:
            publisher.pop('slug', None)
            publisher.pop('games_count', None)
            publisher.pop('image_background', None)
    print("[" + str(counter) + "] " + str(game['name']) + " updated")
    counter += 1

with open('game_data.json', 'w', encoding='utf-8') as f:
    json.dump(game_data, f, ensure_ascii=False, indent=4)


# testing HowLongToBeat API
# results = HowLongToBeat().search(game_data[0]['name'])
