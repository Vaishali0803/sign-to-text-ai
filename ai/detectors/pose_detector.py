import mediapipe as mp


class PoseDetector:

    def __init__(self):

        self.mpPose = mp.solutions.pose

        self.pose = self.mpPose.Pose(
            static_image_mode=False,
            model_complexity=1,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6
        )

    def detect(self, rgb):

        return self.pose.process(rgb)