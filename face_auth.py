import cv2
try:
    import face_recognition
except ImportError:
    face_recognition = None


def capture_face_encoding():
    if face_recognition is None:
        return None
    cap = None
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            return None
        ret, frame = cap.read()
        if not ret or frame is None:
            return None
        encodings = face_recognition.face_encodings(frame)
        if len(encodings) > 0:
            return encodings[0].tolist()
        return None
    except Exception:
        return None
    finally:
        if cap is not None:
            cap.release()
        cv2.destroyAllWindows()


def compare_face(encode1, encode2):
    if face_recognition is None:
        return False
    try:
        res = face_recognition.compare_faces([encode1], encode2)
        return res[0]
    except Exception:
        return False
