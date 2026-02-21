import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """Unit tests for the emotion_detector function."""

    def test_emotion_detector(self):
        """Test cases for various emotional statements."""
        # Test Joy
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        
        # Test Anger
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        
        # Test Disgust
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        
        # Test Sadness
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4['dominant_emotion'], 'sadness')
        
        # Test Fear
        result_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()