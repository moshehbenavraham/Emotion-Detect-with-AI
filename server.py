"""
Flask Server for Emotion Detection Application

This module provides a web server that exposes an emotion detection API
using the EmotionDetection package.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
    """
    Handle emotion detection requests.

    Accepts both GET and POST requests with text to analyze.
    GET: Uses 'textToAnalyze' query parameter.
    POST: Uses 'text' form field.

    Returns:
        str: Formatted response with emotion scores and dominant emotion,
             or an error message for invalid input.
    """
    if request.method == 'POST':
        text_to_analyze = request.form.get('text', '')
    else:
        text_to_analyze = request.args.get('textToAnalyze', '')

    result = emotion_detector(text_to_analyze)

    # Check if the result is valid
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
