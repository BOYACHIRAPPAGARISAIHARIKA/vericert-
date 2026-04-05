import unittest
import os
from ela_processor import calculate_ela  # Import your ELA function

class TestELAProcessor(unittest.TestCase):

    def test_ela_calculation(self):
        # Provide a test image and expected ELA value
        test_image_path = 'path/to/test_image.jpg'
        expected_ela_value = 100.0  # Set the expected value based on the image
        self.assertAlmostEqual(calculate_ela(test_image_path), expected_ela_value, places=1)

    def test_output_file_existence(self):
        # Path to the image for which ELA file should be created
        test_image_path = 'path/to/test_image.jpg'
        output_file_path = 'output/ela_output.jpg'  # Adjust as per your logic
        calculate_ela(test_image_path)
        self.assertTrue(os.path.exists(output_file_path), "Output ELA file does not exist")

    def test_invalid_image_handling(self):
        invalid_image_path = 'path/to/invalid_image.jpg'
        with self.assertRaises(ValueError):  # Adjust the exception type as necessary
            calculate_ela(invalid_image_path)

if __name__ == '__main__':
    unittest.main()