import cv2
import dlib
import numpy as np
from scipy.spatial import distance as dist
from imutils import face_utils
import imutils
from pygame import mixer
import threading
import time
import os

class DrowsinessDetector:
    def __init__(self):
        self.EYE_AR_THRESH = 0.25
        self.EYE_AR_CONSEC_FRAMES = 30
        self.YAWN_THRESH = 25
        self.YAWN_CONSEC_FRAMES = 20
        self.COUNTER = 0
        self.YARN_FRAME = 0
        self.alarm_status = False
        self.alarm_status2 = False
        self.saying = False
        self.running = False
        
        # Initialize sound mixer with proper file paths
        try:
            mixer.init()
            current_dir = os.path.dirname(os.path.abspath(__file__))
            sounds_dir = os.path.join(current_dir, 'static', 'sounds')
            
            # Create sounds directory if it doesn't exist
            os.makedirs(sounds_dir, exist_ok=True)
            
            # Load sound files with error handling
            wake_up_path = os.path.join(sounds_dir, 'wake_up.mp3')
            alert_path = os.path.join(sounds_dir, 'alert.mp3')
            
            if not os.path.exists(wake_up_path):
                raise FileNotFoundError(f"wake_up.mp3 not found at {wake_up_path}")
            if not os.path.exists(alert_path):
                raise FileNotFoundError(f"alert.mp3 not found at {alert_path}")
                
            self.sound1 = mixer.Sound(wake_up_path)
            self.sound2 = mixer.Sound(alert_path)
            
        except Exception as e:
            print(f"Sound initialization error: {e}")
            self.sound1 = None
            self.sound2 = None
            print("Continuing without audio alerts")
        
        # Load face detector and predictor
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.detector = cv2.CascadeClassifier(
            os.path.join(current_dir, 'haarcascade_frontalface_default.xml'))
        self.predictor = dlib.shape_predictor(
            os.path.join(current_dir, 'shape_predictor_68_face_landmarks.dat'))

    def alarm(self, msg):
        """Handle alarm sounds with thread-safe playback"""
        while self.alarm_status:
            print('Drowsiness detected!')
            self.saying = True
            if self.sound1:
                try:
                    # Stop any existing playback and start new one
                    self.sound1.stop()
                    self.sound1.play()
                except Exception as e:
                    print(f"Error playing alarm: {e}")
            self.saying = False
            time.sleep(0.1)  # Small delay to prevent CPU overload
            
        if self.alarm_status2:
            print('Yawning detected!')
            if self.sound2:
                try:
                    self.sound2.stop()
                    self.sound2.play()
                except Exception as e:
                    print(f"Error playing yawn alert: {e}")
    # ... [keep all your existing methods unchanged] ...

    def eye_aspect_ratio(self, eye):
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])
        C = dist.euclidean(eye[0], eye[3])
        ear = (A + B) / (2.0 * C)
        return ear

    def final_ear(self, shape):
        (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        leftEAR = self.eye_aspect_ratio(leftEye)
        rightEAR = self.eye_aspect_ratio(rightEye)

        ear = (leftEAR + rightEAR) / 2.0
        return (ear, leftEye, rightEye)

    def lip_distance(self, shape):
        top_lip = shape[50:53]
        top_lip = np.concatenate((top_lip, shape[61:64]))

        low_lip = shape[56:59]
        low_lip = np.concatenate((low_lip, shape[65:68]))

        top_mean = np.mean(top_lip, axis=0)
        low_mean = np.mean(low_lip, axis=0)

        distance = abs(top_mean[1] - low_mean[1])
        return distance

    def alarm(self, msg):
        while self.alarm_status:
            print('Drowsiness detected!')
            self.saying = True
            self.sound1.play()
            self.saying = False
            
        if self.alarm_status2:
            print('Yawning detected!')
            self.sound2.play()

    def start_detection(self):
        self.running = True
        vs = cv2.VideoCapture(0)
        
        while self.running:
            ret, frame = vs.read()
            if not ret:
                break
                
            frame = imutils.resize(frame, width=450)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            rects = self.detector.detectMultiScale(gray, scaleFactor=1.1, 
                                                minNeighbors=5, minSize=(30, 30),
                                                flags=cv2.CASCADE_SCALE_IMAGE)

            for (x, y, w, h) in rects:
                rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
                shape = self.predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)

                eye = self.final_ear(shape)
                ear = eye[0]
                leftEye = eye[1]
                rightEye = eye[2]

                distance = self.lip_distance(shape)

                leftEyeHull = cv2.convexHull(leftEye)
                rightEyeHull = cv2.convexHull(rightEye)
                cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
                cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

                lip = shape[48:60]
                cv2.drawContours(frame, [lip], -1, (0, 255, 0), 1)

                if ear < self.EYE_AR_THRESH:
                    self.COUNTER += 1

                    if self.COUNTER >= self.EYE_AR_CONSEC_FRAMES:
                        if not self.alarm_status:
                            self.alarm_status = True
                            t = threading.Thread(target=self.alarm, args=('wake up sir',))
                            t.daemon = True
                            t.start()

                        cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                else:
                    self.COUNTER = 0
                    self.alarm_status = False

                if distance > self.YAWN_THRESH:
                    self.YARN_FRAME += 1

                    if self.YARN_FRAME >= self.YAWN_CONSEC_FRAMES:
                        if not self.alarm_status2:
                            self.alarm_status2 = True
                            t = threading.Thread(target=self.alarm, args=('take some fresh air sir',))
                            t.daemon = True
                            t.start()

                        cv2.putText(frame, "YAWN Alert", (10, 60),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                else:
                    self.YARN_FRAME = 0
                    self.alarm_status2 = False

                cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "YAWN: {:.2f}".format(distance), (300, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            ret, jpeg = cv2.imencode('.jpg', frame)
            frame_bytes = jpeg.tobytes()
            
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')

        vs.release()
        cv2.destroyAllWindows()


    def stop_detection(self):
        self.running = False
        # Stop any playing sounds when detection stops
        if hasattr(self, 'sound1') and self.sound1:
            self.sound1.stop()
        if hasattr(self, 'sound2') and self.sound2:
            self.sound2.stop()    