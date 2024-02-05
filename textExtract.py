import os
import pytesseract
from PIL import Image
import pandas as pd

# Path to the resized folder
resized_folder = "./Resized2"

# Iterate over each image in the folder
for filename in os.listdir(resized_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(resized_folder, filename)
        
        # Open the image
        image = Image.open(image_path)
        
        # Extract text from the image using pytesseract
        text = pytesseract.image_to_string(image)
        
        # Split the extracted text into lines
        lines = text.split("\n")
        
        # Filter lines that start with "+"
        lines = [line for line in lines if line.startswith("+")]
        print(lines)
        # Create a DataFrame from the extracted text
        df = pd.DataFrame({"Numbers": lines})
        
        # Save the DataFrame to a CSV file
        csv_file_path = f"./extracted_text1.csv"
        df.to_csv(csv_file_path, index=False, mode='a', header=not os.path.exists(csv_file_path))
        
print("Text extraction completed and appended to", csv_file_path)
