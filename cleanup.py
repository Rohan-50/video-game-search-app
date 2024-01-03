# imports
# from howlongtobeatpy import HowLongToBeat
# from langchain.chat_models import ChatOpenAI
# from langchain.chains import ConversationChain
# from langchain.memory import ConversationBufferMemory
# import openai
# import os
# import requests
# import json
# import mysql.connector

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
    counter += 1

# Connect to the MySQL database
try:
    connection = mysql.connector.connect(
        host='',
        username='',
        password='',
        database=''
    )
    if connection.is_connected():
        print('Connected to the database!')
        cursor = connection.cursor()
except mysql.connector.Error as err:
    print(f"Error: {err}")
    raise SystemExit(0)

counter = 1

# Create a table (replace with your own schema)
cursor.execute(
    CREATE TABLE IF NOT EXISTS games (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    platforms JSON,
    stores JSON,
    released DATE,
    background_image VARCHAR(255),
    rating FLOAT,
    rating_top INT,
    ratings JSON,
    ratings_count INT,
    reviews_text_count INT,
    added INT,
    added_by_status JSON,
    metacritic INT,
    updated TIMESTAMP,
    tags JSON,
    esrb_rating JSON,
    reviews_count INT,
    saturated_color VARCHAR(6),
    dominant_color VARCHAR(6),
    short_screenshots JSON,
    genres JSON,
    name_original VARCHAR(255),
    description TEXT,
    metacritic_platforms JSON,
    background_image_additional VARCHAR(255),
    website VARCHAR(255),
    reactions JSON,
    reddit_url VARCHAR(255),
    metacritic_url VARCHAR(255),
    developers JSON,
    publishers JSON))

# Read JSON data
with open('updated_game_data.json', 'r') as file:
    game_data = json.load(file)

    # Insert data into the MySQL table
    for game in game_data:
        query = '''
                INSERT INTO games (
                    name,
                    platforms,
                    stores,
                    released,
                    background_image,
                    rating,
                    rating_top,
                    ratings,
                    ratings_count,
                    reviews_text_count,
                    added,
                    added_by_status,
                    metacritic,
                    updated,
                    tags,
                    esrb_rating,
                    reviews_count,
                    saturated_color,
                    dominant_color,
                    short_screenshots,
                    genres,
                    name_original,
                    description,
                    metacritic_platforms,
                    background_image_additional,
                    website,
                    reactions,
                    reddit_url,
                    metacritic_url,
                    developers,
                    publishers)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''

        data = (
            game['name'],
            json.dumps(game.get('platforms', [])),
            json.dumps(game.get('stores', [])),
            game.get('released'),
            game.get('background_image'),
            game.get('rating'),
            game.get('rating_top'),
            json.dumps(game.get('ratings', [])),
            game.get('ratings_count'),
            game.get('reviews_text_count'),
            game.get('added'),
            json.dumps(game.get('added_by_status', [])),
            game.get('metacritic'),
            game.get('updated'),
            json.dumps(game.get('tags', [])),
            json.dumps(game.get('esrb_rating', [])),
            game.get('reviews_count'),
            game.get('saturated_color'),
            game.get('dominant_color'),
            json.dumps(game.get('short_screenshots', [])),
            json.dumps(game.get('genres', [])),
            game.get('name_original'),
            game.get('description'),
            json.dumps(game.get('metacritic_platforms', [])),
            game.get('background_image_additional'),
            game.get('website'),
            json.dumps(game.get('reactions', {})),
            game.get('reddit_url'),
            game.get('metacritic_url'),
            json.dumps(game.get('developers', [])),
            json.dumps(game.get('publishers', []))
        )

        cursor.execute(query, data)
        print("[" + str(counter) + "] " +
              game['name'] + " was added to the database")
        counter += 1

# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close() """

# testing HowLongToBeat API
# results = HowLongToBeat().search(game_data[0]['name'])
