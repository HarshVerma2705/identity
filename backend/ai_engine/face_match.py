from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import os

def verify_face(input_image, database_path, model_name="VGG-Face"):
    """
    Compares input image against database using DeepFace.
    Returns matched image path, similarity score, model name, and score column.
    Handles DataFrame and list-of-DataFrames cases safely.
    """
    try:
        if not os.path.exists(input_image):
            raise FileNotFoundError(f"Input image not found: {input_image}")
        if not os.path.exists(database_path):
            raise FileNotFoundError(f"Database folder not found: {database_path}")

        results = DeepFace.find(
            img_path=input_image,
            db_path=database_path,
            model_name=model_name
        )
        print("Type of results:", type(results))

        # Normalize to DataFrame
        df = None
        if isinstance(results, pd.DataFrame):
            df = results
        elif isinstance(results, list):
            for item in results:
                if isinstance(item, pd.DataFrame) and item.shape[0] > 0:
                    df = item
                    break

        if df is None or df.shape[0] == 0:
            return None, None, None, None

        best_match = df.iloc[0]
        matched_image_path = best_match['identity']

        # Build expected score column dynamically
        score_col = f"{model_name}_cosine"
        match_score = best_match.get(score_col, None)

        return matched_image_path, match_score, model_name, score_col

    except Exception as e:
        print(f"Error in verify_face: {e}")
        return None, None, None, None
    

def display_images(input_image, matched_image):
    """
    Displays input and matched images side by side.
    """
    try:
        if not matched_image or not os.path.exists(matched_image):
            raise FileNotFoundError("Matched image not found or invalid.")

        img1 = cv2.imread(input_image)
        img2 = cv2.imread(matched_image)

        if img1 is None or img2 is None:
            raise ValueError("Error loading images with OpenCV.")

        # Convert BGR to RGB
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

        # Plot side by side
        plt.subplot(1, 2, 1)
        plt.imshow(img1)
        plt.title("Input Image")
        plt.axis("off")

        plt.subplot(1, 2, 2)
        plt.imshow(img2)
        plt.title("Matched Database Image")
        plt.axis("off")

        plt.show()

    except Exception as e:
        print(f"Error in display_images: {e}")