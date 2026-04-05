import cv2
from PIL import Image
import numpy as np

def calculate_ela(original_image_path, output_image_path, scale_factor=10):
    # Load the original image
    original = Image.open(original_image_path)
    # Save the image to create a compressed copy
    original.save(output_image_path, "JPEG", quality=95)
    
    # Load the images using OpenCV
    original_cv = cv2.imread(original_image_path)
    modified_cv = cv2.imread(output_image_path)

    # Calculate the absolute difference between the two images
    diff = cv2.absdiff(original_cv, modified_cv)

    # Convert the difference to grayscale
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Scale the difference image
    ela_image = np.uint8(np.clip(gray_diff * scale_factor, 0, 255))

    # Save the ELA image
    ela_output_path = 'ela_output.png'  
    cv2.imwrite(ela_output_path, ela_image)

    return ela_output_path

def main():
    original_image_path = 'path_to_your_image.jpg'  # Provide the path to the original image
    output_image_path = 'path_to_compressed_image.jpg'  # Provide the path for the compressed image
    ela_image_path = calculate_ela(original_image_path, output_image_path)
    print(f"ELA image saved as: {ela_image_path}")

if __name__ == "__main__":
    main()