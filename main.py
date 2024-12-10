import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
from flask import Flask, request, jsonify
from flask_cors import CORS


# import matplotlib.pyplot as plt
# import matplotlib.image as pltimg

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 
df = pandas.read_csv("gry_planszowe.csv",sep=";")

d = {'1': 0, '2': 1, '3+': 2}
df['Liczba_graczy'] = df['Liczba_graczy'].map(d)


d = {'darmowe': 0, '<500': 1, 'premium': 2, "?": 3}
df['koszt1'] = df['koszt1'].map(d)

d = {'<500': 0, 'premium': 1, "?": 2}
df['koszt2'] = df['koszt2'].map(d)

d = {'nie': 0, 'tak': 1, '?': 2}
df['Przesten'] = df['Przesten'].map(d)

d = {'tak': 0, 'nie': 1, '?': 2}
df['Samodzielny_druk'] = df['Samodzielny_druk'].map(d)

d = {'tak': 0, 'nie': 1, '?': 2}
df['Duzy_stol'] = df['Duzy_stol'].map(d)

d = {'strategia': 0, 'logiczna': 1, 'przygodowa': 2}
df['typ_gry'] = df['typ_gry'].map(d)

d = {'deck building': 0, 'euro': 1, '"': 2}
df['mechanika_gry_s'] = df['mechanika_gry_s'].map(d)

d = {'pattern matching': 0, 'roll&write': 1, '?': 2}
df['mechanika_gry_l'] = df['mechanika_gry_l'].map(d)

d = {'dungeon crawl': 0, 'boss battler': 1, '?': 2}
df['mechanika_gry_p'] = df['mechanika_gry_p'].map(d)

features = ['Liczba_graczy', 'koszt1', 'koszt2', 'Przesten', 'Samodzielny_druk', 'Duzy_stol', 'typ_gry', 'mechanika_gry_l', 'mechanika_gry_s','mechanika_gry_p']

X = df[features]
y = df['gra']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
prediction = []
print(dtree.predict([[0, 0, 2, 0, 2,2, 0, 0, 2,2]]))

@app.route('/', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/predict', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        prediction.append(post_data)
        response_object['message'] = prediction
        print(prediction)
    else:
        response_object['books'] = prediction
    return jsonify(response_object)

if __name__ == "__main__":
    app.run(debug=True)
