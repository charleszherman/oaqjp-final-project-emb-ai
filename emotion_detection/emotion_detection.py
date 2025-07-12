import requests  # Import the requests library to handle HTTP requests
import json


def emotion_detector(text_to_analyse):  # Define a function named emotion_detection that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers

    if response.status_code == 400:
        empty_dict = {"anger":None, "disgust":None, "fear":None, "joy":None, "sadness":None, "dominant_emotion":None}
        return empty_dict

    formatted_response = json.loads(response.text)

    emotion = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotion['anger']
    disgust_score = emotion['disgust']
    fear_score = emotion['fear']
    joy_score = emotion['joy']
    sadness_score = emotion['sadness']

    dominant_score = max(emotion, key=emotion.get)

    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_score}

    #return response.text  # Return the response text from the API