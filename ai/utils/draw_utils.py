import mediapipe as mp

mpDraw = mp.solutions.drawing_utils

mpHands = mp.solutions.hands

mpPose = mp.solutions.pose


def draw_hands(frame, hand_results):

    if hand_results.multi_hand_landmarks:

        for hand in hand_results.multi_hand_landmarks:

            mpDraw.draw_landmarks(
                frame,
                hand,
                mpHands.HAND_CONNECTIONS
            )


def draw_pose(frame, pose_results):

    if pose_results.pose_landmarks:

        mpDraw.draw_landmarks(
            frame,
            pose_results.pose_landmarks,
            mpPose.POSE_CONNECTIONS
        )