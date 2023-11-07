from urllib.request import urlopen
import json

url = "https://opentdb.com/api.php?amount=10&category=18&type=boolean"


def get_questions():
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json['results']


question_data = get_questions()
