import cv2
import csv
import os
import time

from camera import Camera
from detectors.hand_detector import HandDetector
from detectors.pose_detector import PoseDetector
from utils.feature_extraction import extract_features
from utils.draw_utils import draw_hands, draw_pose

camera = Camera()
hand_detector = HandDetector()
pose_detector = PoseDetector()

word = "HELLO"

save_folder = "dataset/custom_dataset"
os.makedirs(save_folder, exist_ok=True)

csv_path = os.path.join(save_folder, f"{word}.csv")

samples = 200

print("\nGet ready...")
time.sleep(3)
print("Collecting...\n")

with open(csv_path, "w", newline="") as file:

    writer = csv.writer(file)

    for i in range(samples):

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

        row = list(features)
        row.append(word)

        writer.writerow(row)

        draw_hands(frame, hand_results)
        draw_pose(frame, pose_results)

        cv2.putText(
            frame,
            f"{word} : {i+1}/{samples}",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        cv2.imshow("Collecting Dataset", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

print("\nDone!")

camera.release()
cv2.destroyAllWindows()