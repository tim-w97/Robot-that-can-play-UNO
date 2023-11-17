import cv2
import pytesseract
import matplotlib.pyplot as plt

def process_uno_card(image_path):
    # Load the image
    image = cv2.imread(image_path)

    if image is not None:
        # Resize the image while preserving its aspect ratio to fit within a 200x350 bounding box
        max_width = 240
        max_height = 340

        # Get the original image dimensions
        height, width = image.shape[:2]

        # Calculate the scaling factor to fit within the bounding box
        width_scale = max_width / width
        height_scale = max_height / height
        scale = min(width_scale, height_scale)

        # Resize the image
        resized_image = cv2.resize(image, None, fx=scale, fy=scale)

        # Convert the resized image to grayscale
        gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

        # Calculate the center coordinates of the resized image
        height, width = gray.shape
        center_x = width // 2
        center_y = height // 2

        # Define the region size around the center (adjust as needed)
        region_size = 100  # You can adjust this size

        # Calculate the region boundaries
        left = max(0, center_x - region_size)
        right = min(width, center_x + region_size)
        top = max(0, center_y - region_size)
        bottom = min(height, center_y + region_size)

        # Crop the region around the center
        number_region = gray[top:bottom, left:right]

        # Apply adaptive histogram equalization
        number_region = cv2.equalizeHist(number_region)

        # Apply binary thresholding to create a monochrome image
        _, thresh = cv2.threshold(number_region, 200, 255, cv2.THRESH_BINARY)

        try:
            # Use Tesseract OCR to recognize the number with custom configuration
            number = pytesseract.image_to_string(thresh, config='--psm 6 -c tessedit_char_whitelist=0123456789')
            # Clean up the detected text (extract only digits)
            number = ''.join(filter(str.isdigit, number))
            return number
        except Exception as e:
            return f"Error: {e}"
        
        
    else:
        return "Image not found."


