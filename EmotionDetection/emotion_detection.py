import requests
import json

text_to_analyse = "I am so happy I am doing this."

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse }}
    response = requests.post(url, json = myobj, headers= header)

    emotions = ''
    dominant_emotion = ''

    if response.status_code == 200:
        dico = response.text
        forma = json.loads(dico)
        emotions = forma['emotionPredictions'][0]['emotion']
        dominant_val = 0
        dominant_emotion = ''
        for emotion in emotions:
            if emotions[emotion] > dominant_val:
                dominant_val = emotions[emotion]
                dominant_emotion = emotion
    elif response.status_code == 500 or text_to_analyse.strip() == "":
        emotions = None
        dominant_emotion = None

    newdict = dict(emotions, dominant_emotion = dominant_emotion)
    return newdict