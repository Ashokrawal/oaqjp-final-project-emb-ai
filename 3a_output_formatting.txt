import requests
import json

def emotion_detector(text_to_analyze):

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=input_json)

    # Convert JSON string to dictionary
    response_dict = json.loads(response.text)

    # Extract emotions dictionary
    emotions = response_dict['emotionPredictions'][0]['emotion']

    # Get individual scores
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    # Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Return formatted result
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }