import requests
import json

'''
This function offers the ability to predict the sentiment of a single sentence 
through the API, the sentiment is one of three classes (positive negative, neutral)
Input: 
        sentence(str): the input sentence of which the sentiment is to be predicted
Output:
        prediction(str): the sentiment of the given sentence 
'''


def predict(sentence):
    url = "http://mazajak.inf.ed.ac.uk:8000/api/predict"
    to_sent = {'data': sentence}
    data = json.dumps(to_sent,ensure_ascii=False).encode('utf8')
    headers = {'content-type': 'application/json'}
    # sending get request and saving the response as response object
    response = requests.post(url=url, data=data, headers=headers)

    prediction = json.loads(response.content)['data']

    return prediction


'''
This function offers the ability to predict the sentiment of a list of sentences
through the API, the sentiment is one of three classes (positive negative, neutral)
Input: 
        sent_lst(list of str): the input list of which the sentiment of its sentences is to be predicted
Output:
        prediction(list of str): the sentiments of the given sentences
'''


def predict_list(sent_lst):
    url = "http://mazajak.inf.ed.ac.uk:8000/api/predict_list"
    to_sent = {'data': sent_lst}
    data = json.dumps(to_sent)
    headers = {'content-type': 'application/json'}
    # sending get request and saving the response as response object
    response = requests.post(url=url, data=data, headers=headers)

    prediction = json.loads(response.content)['data']

    return prediction


'''
This is an example to use the functions
'''
tweets = ['انا زعلان منك', 'انا مبسوط اوي']
l = []
for tweet in tweets:
    print(predict(tweet))

print(predict_list(tweets))
