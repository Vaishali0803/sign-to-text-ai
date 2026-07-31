import numpy as np

def extract_features(pose_results, hand_results):
    features = []

    # -----------------------------
    # Pose landmarks (shoulders, elbows, wrists)
    # -----------------------------
    if pose_results.pose_landmarks:
        pose = pose_results.pose_landmarks.landmark

        pose_indices = [11, 12, 13, 14, 15, 16]

        for idx in pose_indices:
            features.extend([
                pose[idx].x,
                pose[idx].y,
                pose[idx].z
            ])
    else:
        features.extend([0.0] * 18)

    # -----------------------------
    # Left & Right Hand
    # -----------------------------
    if hand_results.multi_hand_landmarks:

        hands = hand_results.multi_hand_landmarks

        for i in range(2):

            if i < len(hands):

                for lm in hands[i].landmark:

                    features.extend([
                        lm.x,
                        lm.y,
                        lm.z
                    ])

            else:
                features.extend([0.0] * 63)

    else:
        features.extend([0.0] * 126)
    print(len(features))

    return np.array(features, dtype=np.float32)