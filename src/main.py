import time
import mediapipe as mp
import cv2

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

targets = {
    "Closed_Fist": 1,
    "Open_Palm": 2,
    "Pointing_Up": 3,
    "Thumb_Down": 4,
    "Thumb_Up": 5,
    "Victory": 6,
    "ILoveYou": 7
}

last_gesture = 0

def save_gesture(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    global last_gesture
    if result.gestures:
        gesture = result.gestures[0][0].category_name

        if gesture and gesture in targets:
            if last_gesture != gesture or last_gesture == 0:
                last_gesture = gesture
                print(gesture)

options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path='gesture_recognizer.task'),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=save_gesture)

recognizer = GestureRecognizer.create_from_options(options)

def detect_gesture():
    cap = cv2.VideoCapture(0)
    prev_timestamp_ms = 0
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture a frame")
            break

        current_timestamp_ms = int(time.time() * 1000)
        if current_timestamp_ms > prev_timestamp_ms+2000:
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
            recognizer.recognize_async(mp_image, current_timestamp_ms)
            prev_timestamp_ms = current_timestamp_ms

        cv2.putText(frame, str(last_gesture), (250, 50), 
            cv2.FONT_HERSHEY_COMPLEX, 0.9, 
            (0, 255, 0), 2)
        
        cv2.imshow('Camera Feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

detect_gesture()