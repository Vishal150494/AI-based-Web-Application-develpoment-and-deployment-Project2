from EmotionDetector.emotion_detection import emotion_detector
import unittest

class TestEmotionAnalyzer(unittest.TestCase):
    def test_emotion_analyzer(self):
        result_1 = emotion_detector("I am glad this happened")
        emotion_1 = result_1['dominant_emotion']
        result_2 = emotion_detector("I am really mad about this")
        emotion_2 = result_2['dominant_emotion']
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        emotion_3 = result_3['dominant_emotion']
        result_4 = emotion_detector("I am so sad about this")
        emotion_4 = result_4['dominant_emotion']
        result_5 = emotion_detector("I am really afraid that this will happen")
        emotion_5 = result_5['dominant_emotion']
        self.assertEqual(emotion_1, 'joy')
        self.assertEqual(emotion_2, 'anger')
        self.assertEqual(emotion_3, 'disgust')
        self.assertEqual(emotion_4, 'sadness')
        self.assertEqual(emotion_5, 'fear')
        
if __name__ == '__main__':
    unittest.main()