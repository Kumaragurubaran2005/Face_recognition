import cv2

def detect_cameras(max_cameras_to_check=10):  # More descriptive argument name
    """Detects available cameras and their indices.

    Args:
        max_cameras_to_check: The maximum number of camera indices to check.

    Returns:
        A list of integers representing the indices of available cameras.
        Returns an empty list if no cameras are found.
    """

    available_cameras = []

    for i in range(max_cameras_to_check):
        cap = cv2.VideoCapture(i)  # Try opening the camera

        if cap.isOpened():  # Check if the camera opened successfully
            available_cameras.append(i)
            print(f"Camera {i} detected.")
            cap.release()  # Release the camera immediately after checking
        else:
            # Instead of printing an exception, provide more helpful info:
            print(f"Camera {i} not found or busy.")  # Or just remove this line for less output

    return available_cameras
