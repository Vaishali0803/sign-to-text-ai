import cv2

from camera import Camera
from detectors.hand_detector import HandDetector
from detectors.pose_detector import PoseDetector
from utils.feature_extraction import extract_features
from utils.draw_utils import draw_hands, draw_pose
from recognizer import ASLRecognizer

camera = Camera()

hand_detector = HandDetector()
pose_detector = PoseDetector()
recognizer = ASLRecognizer()

while True:

    frame = camera.get_frame()

    if frame is None:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    pose_results = pose_detector.detect(rgb)
    hand_results = hand_detector.detect(rgb)

    features = extract_features(
        pose_results,
        hand_results
    )
  

    word, confidence = recognizer.predict(features)

    num_hands = (
        len(hand_results.multi_hand_landmarks)
        if hand_results.multi_hand_landmarks
        else 0
    )

    cv2.putText(
        frame,
        f"Word: {word}",
        (10, 110),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Confidence: {confidence:.2f}",
        (10, 150),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Hands: {num_hands}",
        (10, 190),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    draw_hands(frame, hand_results)
    draw_pose(frame, pose_results)

    cv2.imshow("Sign Language Detector", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()