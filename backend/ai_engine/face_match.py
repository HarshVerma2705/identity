from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
import os

def verify_face(input_image, database_path):
    """
    Compares input image against database using DeepFace.
    Returns matched image path and similarity score.
    """
    try:
        # Check if input image exists
        if not os.path.exists(input_image):
            raise FileNotFoundError(f"Input image not found: {input_image}")

        # Check if database folder exists
        if not os.path.exists(database_path):
            raise FileNotFoundError(f"Database folder not found: {database_path}")

        # Perform face search
        results = DeepFace.find(img_path=input_image, db_path=database_path)

        if results is None or len(results) == 0:
            return None, None

        # Take best match (first row)
        best_match = results.iloc[0]
        matched_image_path = best_match['identity']
        match_score = best_match['VGG-Face_cosine']

        return matched_image_path, match_score

    except Exception as e:
        print(f"Error in verify_face: {e}")
        return None, None



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