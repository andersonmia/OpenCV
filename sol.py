import cv2
import pytesseract

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh

def ocr_preprocessed_image(preprocessed_image):
    # Enhanced configuration for numeric data
    config = '--oem 3 --psm 6 outputbase digits'
    extracted_text = pytesseract.image_to_string(preprocessed_image, config=config)
    return extracted_text

image_path = 'Image.png'  # Update this path
preprocessed_image = preprocess_image(image_path)
extracted_text = ocr_preprocessed_image(preprocessed_image)
print(extracted_text)
