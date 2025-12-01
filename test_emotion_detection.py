"""
Unit tests for the EmotionDetection package.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def test_joy_dominant(self):
        """Test that joy is detected as dominant emotion for joyful text."""
        statement = "I am glad this happened"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_dominant(self):
        """Test that anger is detected as dominant emotion for angry text."""
        statement = "I am really mad about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_dominant(self):
        """Test that disgust is detected as dominant emotion for disgusted text."""
        statement = "I feel disgusted just hearing about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_dominant(self):
        """Test that sadness is detected as dominant emotion for sad text."""
        statement = "I am so sad about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_dominant(self):
        """Test that fear is detected as dominant emotion for fearful text."""
        statement = "I am really afraid that this will happen"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_blank_input(self):
        """Test that blank input returns None for dominant emotion."""
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])
        self.assertIsNone(result['disgust'])
        self.assertIsNone(result['fear'])
        self.assertIsNone(result['joy'])
        self.assertIsNone(result['sadness'])

    def test_whitespace_only_input(self):
        """Test that whitespace-only input returns None for dominant emotion."""
        result = emotion_detector("   ")
        self.assertIsNone(result['dominant_emotion'])

    def test_none_input(self):
        """Test that None input returns None for dominant emotion."""
        result = emotion_detector(None)
        self.assertIsNone(result['dominant_emotion'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
