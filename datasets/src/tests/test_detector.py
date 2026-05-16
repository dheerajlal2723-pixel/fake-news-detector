import unittest
from src.models.detector import FakeNewsDetector

class TestFakeNewsDetector(unittest.TestCase):

    def setUp(self):
        self.detector = FakeNewsDetector()
        self.detector.train_model()  # Assuming this method trains the model

    def test_predict(self):
        test_input = "This is a test news article."
        prediction = self.detector.predict(test_input)
        self.assertIn(prediction, ["fake", "real"])  # Assuming the model predicts 'fake' or 'real'

    def test_evaluate_model(self):
        accuracy = self.detector.evaluate_model()
        self.assertGreaterEqual(accuracy, 0.5)  # Assuming a model accuracy of at least 50% is acceptable

if __name__ == '__main__':
    unittest.main()