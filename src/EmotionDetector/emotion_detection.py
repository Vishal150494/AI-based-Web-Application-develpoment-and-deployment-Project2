"""
Author: Vishal Ashok Hegde
Function to perform Sentiment Analysis using Watson-nlp library
"""
import requests
import json

def emotion_detector(text_to_analyse: str):
    """
    Function to analyse the text input and predict the emotion of the text
    Emotions Categorized into :
    :1. Joy
    :2. Sadness
    :3. Anger 
    and so on
    """
    
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text)

    emotion_predictions = formatted_response.get('emotionPredictions', [])
    if emotion_predictions:
        prediction = emotion_predictions[0]
    
        if response.status_code == 200:
            emotion_scores = {
                'anger': prediction['emotion']['anger'],
                'disgust': prediction['emotion']['disgust'],
                'fear': prediction['emotion']['fear'],
                'joy': prediction['emotion']['joy'],
                'sadness': prediction['emotion']['sadness']
            }

            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            emotion_scores['dominant_emotion'] = dominant_emotion

        elif response.status_code == 400 or response.status_code == 500:
            emotion_scores = {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
            
    else:
        emotion_scores = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return emotion_scores
