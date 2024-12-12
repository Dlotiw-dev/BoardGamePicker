import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import xml.etree.ElementTree as ET
# import matplotlib.pyplot as plt
# import matplotlib.image as pltimg

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 
df = pandas.read_csv("gry_planszowe.csv",sep=",")


d = {'1': 0, '2': 1, '3+': 2}
df['Liczba_graczy'] = df['Liczba_graczy'].map(d)


d = {'darmowe': 0, '<500': 1, 'premium': 2, "?": -1}
df['koszt1'] = df['koszt1'].map(d)

d = {'<500': 0, 'premium': 1, "?": -1}
df['koszt2'] = df['koszt2'].map(d)

d = {'nie': 1, 'tak': 0, '?': -1}
df['Przesten'] = df['Przesten'].map(d)

d = {'tak': 0, 'nie': 1, '?': -1}
df['Samodzielny_druk'] = df['Samodzielny_druk'].map(d)

d = {'tak': 0, 'nie': 1, '?': -1}
df['Duzy_stol'] = df['Duzy_stol'].map(d)

d = {'strategia': 0, 'logiczna': 1, 'przygodowa': 2}
df['typ_gry'] = df['typ_gry'].map(d)

d = {'deck building': 0, 'euro': 1, '?': -1}
df['mechanika_gry_s'] = df['mechanika_gry_s'].map(d)

d = {'pattern matching': 0, 'roll&write': 1, '?': -1}
df['mechanika_gry_l'] = df['mechanika_gry_l'].map(d)

d = {'dungeon crawl': 0, 'boss battler': 1, '?': -1}
df['mechanika_gry_p'] = df['mechanika_gry_p'].map(d)

features = ['Liczba_graczy', 'koszt1', 'koszt2', 'Przesten', 'Samodzielny_druk', 'Duzy_stol', 'typ_gry', 'mechanika_gry_l', 'mechanika_gry_s','mechanika_gry_p']

X = df[features]
y = df['gra']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

@app.route('/', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

def getPrediction(data):
    prediction = dtree.predict(data)
    print(prediction)
    return prediction

@app.route('/bgg/get', methods=['GET'])
def bgg():
    game_id = request.args.get('gameId')
    base_link = 'https://boardgamegeek.com/xmlapi/boardgame/'
    link = base_link + game_id
    response = requests.get(link)
    if response.status_code == 200:
        # Parse XML
        root = ET.fromstring(response.text)

        # Extract description and image for each boardgame
        boardgames = []
        for boardgame in root.findall('boardgame'):
            description = boardgame.find('description').text if boardgame.find('description') is not None else ""
            image_url = boardgame.find('image').text if boardgame.find('image') is not None else ""
            
            boardgames.append({
                'description': description,
                'image': image_url
            })

        # Return the list of descriptions and image URLs as JSON
        return jsonify(boardgames[0])
    else:
        # Return an error if the request failed
        return jsonify({"error": "Failed to fetch data from BoardGameGeek"}), 500

@app.route('/bgg/search', methods=['GET'])
def bgg_search():
    game_title = request.args.get('game').lower()
    response = requests.get('https://boardgamegeek.com/xmlapi/search', params={'search': game_title})
    if response.status_code == 200:
        # Parse XML
        root = ET.fromstring(response.text)

        # Extract all boardgame object IDs
        object_ids = []
        for boardgame in root.findall('boardgame'):
            object_id = boardgame.get('objectid')
            if object_id:
                object_ids.append(object_id)

        # Return the list of object IDs as JSON
        
        return jsonify(object_ids)
    else:
        # Return an error if the request failed
        return jsonify({"error": "Failed to fetch data from BoardGameGeek"}), 500
    


@app.route('/predict', methods=['POST'])
def predict():
    response_object = {'status': 'success'}
    response = ''
    prediction = [[]]
    if request.method == 'POST':
        post_data = request.get_json()
        for i in post_data.values():
            prediction[0].append(int(i)) 
        print(prediction)
        response = getPrediction(prediction)
        response_object['message'] = response[0]
    return jsonify(response_object)

if __name__ == "__main__":
    app.run(debug=True)
