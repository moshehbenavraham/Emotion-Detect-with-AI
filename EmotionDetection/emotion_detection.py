"""
Emotion Detection Module

This module provides functionality to analyze text and detect emotions
using the IBM Watson NLP API.
"""

import requests
import json


def emotion_detector(text_to_analyze):
    """
    Analyze text and detect emotions using IBM Watson NLP API.

    Args:
        text_to_analyze (str): The text to analyze for emotions.

    Returns:
        dict: A dictionary containing scores for anger, disgust, fear, joy,
              sadness, and the dominant_emotion. Returns None values for all
              fields if the input is invalid or the API request fails.
    """
    # Return None values for empty or None input
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, json=input_json, headers=headers, timeout=10)

        # Handle non-200 status codes
        if response.status_code != 200:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        response_dict = json.loads(response.text)
        emotions = response_dict['emotionPredictions'][0]['emotion']

        emotion_scores = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness']
        }

        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        return {
            'anger': emotion_scores['anger'],
            'disgust': emotion_scores['disgust'],
            'fear': emotion_scores['fear'],
            'joy': emotion_scores['joy'],
            'sadness': emotion_scores['sadness'],
            'dominant_emotion': dominant_emotion
        }

    except (requests.RequestException, json.JSONDecodeError, KeyError, IndexError):
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
