# Face_recognition

How this code works?

   Step 1:Loads known face encodings (from images in the "images/" folder) once at the start.
   Step 2: Detects available cameras and uses threading to process each camera’s feed in parallel.
   Step 3: Each camera’s feed is continuously read, faces are detected and recognized, and the results (bounding boxes and labels) are overlaid on   the video.
   Step 4: The script listens for specific key presses or window closure to stop the feed and release resources properly.
