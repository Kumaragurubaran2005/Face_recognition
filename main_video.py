import cv2
import threading
from simple_facerec import SimpleFacerec
from detect_all_cam import detect_cameras as dc  # Import your camera detection function
import os
import time
from datetime import datetime

# Initialize face recognizer and load encodings (do this ONCE)
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")  
unknown_folder = "unknown"
if not os.path.exists(unknown_folder):
    os.makedirs(unknown_folder)


def process_and_display(camera_index):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"Error: Could not open camera {camera_index}.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print(f"Camera {camera_index} disconnected.")
            break

        face_locations, face_names = sfr.detect_known_faces(frame)  # Detect on the frame

        # Draw bounding boxes and names
        for face_loc, name in zip(face_locations, face_names):
            top, right, bottom, left = face_loc  # Correct unpacking
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 1)
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 200), 2)

        cv2.imshow(f"Camera {camera_index} Feed", frame)  # Unique window name

        key = cv2.waitKey(1)
        if key == 27 or cv2.getWindowProperty(f"Camera {camera_index} Feed", cv2.WND_PROP_VISIBLE) < 1 or key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def main():
    available_cameras = dc(5)  # Use your detect_cameras function (up to 5 cameras)
    working_cameras = []

    for cam_index in available_cameras:
        cap = cv2.VideoCapture(cam_index)
        if cap.isOpened():
            working_cameras.append(cam_index)
            cap.release()  # Release the camera after checking
        else:
            print(f"Camera {cam_index} is not working.")

    if not working_cameras:
        print("No working cameras found.")
        return

    threads = []
    for camera_index in working_cameras:
        thread = threading.Thread(target=process_and_display, args=(camera_index,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Wait for all threads to complete


if __name__ == "__main__":
    main()
