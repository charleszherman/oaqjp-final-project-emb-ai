import requests  # Import the requests library to handle HTTP requests
import json


def emotion_detector(text_to_analyse):  # Define a function named emotion_detection that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers

    formatted_response = json.loads(response.text)

    anger_score = formatted_response['emotionPredictions']['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions']['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions']['emotion']['fear']
    joy_score = formatted_response['emotionPredictions']['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions']['sadness']

    dominant_list = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
    dominant_list.sort()
    dominant_score = dominant_list[0]

    return {'anger_score': anger, 'disgust_score': disgust, 'fear_score': fear, 'joy_score': joy, 'sadness_score': sadness, 'dominant_emotion': demoinant_score}

    #return response.text  # Return the response text from the API