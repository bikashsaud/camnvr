import cv2, queue, threading
# from entities.camera import Camera
# from repo.camera_repo import CameraRepo
import collections
import time, base64
# from service.camera_service import CameraService

def get_cameras():
    # getting camera info from repo
    # camera_repo = CameraRepo()
    # camera_service = CameraService(camera_repo)

    # # list of camera details
    # camera_ids = [cam.camera_id for cam in camera_service.get_cameras()] 
    # camera_urls = [cam.camera_url for cam in camera_service.get_cameras()]
    # camera_names = [cam.camera_name for cam in camera_service.get_cameras()]
    # camera_details = list(zip(camera_ids, camera_urls, camera_names))
    
    # # dictionary of cameras with camera id as a key
    # cameras = dict({a: {"camUrl": b, "camName": c} for a,b,c in camera_details})
    cameras = {
        "1": {
            "camId": "1",
            "camName": "Office Camera",
            "location": "Kathmandu",
            "camUrl": 0
        },
        "2": {
            "camId": "2",
            "camName": "Office Camera",
            "location": "Pokhara",
            "camUrl": "rtsp://192.168.43.2:8080/h264_ulaw.sdp"
            # "camUrl": "/home/ashok/Videos/663474b089b746309cc96fc56a7a135f.mp4"
        }
    }
    
    return cameras


class ThreadSafeDict(dict):
    def __init__(self, *p_arg, **n_arg):
        dict.__init__(self, *p_arg, **n_arg)
        self._lock = threading.Lock()

    def __enter__(self):
        self._lock.acquire()
        return self

    def __exit__(self, type, value, traceback):
        self._lock.release()


class CamNVR:
    _frames = ThreadSafeDict()

    def __init__(self):
        self._cameras = get_cameras()

    def start(self):
        thread = threading.Thread(target=self.process, args=(), daemon=True)
        thread.start()

    def process(self):
        while True:
            print("hello im inside process")
            for cam_id, cam in self._cameras.items():
                cam_id = str(cam_id)
                print(cam["camUrl"])
                cap = cv2.VideoCapture(cam["camUrl"])
                success, frame = cap.read()
                if success:
                    q = collections.deque(maxlen=1)
                    data = {"cam_id": cam_id, "frame": frame}
                    q.append(data)
                    CamNVR._frames[cam_id] = data
                time.sleep(1)

    def gen_frames(self, cam_id):
        print("hello im genrating frames")
        while True:
            frame_detail = CamNVR._frames.get(str(cam_id), None)
            if frame_detail is not None:
                frame = frame_detail.get("frame", None)
                if frame is not None:
                    ret, buffer = cv2.imencode('.jpg', frame)
                    frame = buffer.tobytes()
                    frame = (b'--frame\r\n'
                             b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                    yield frame
                time.sleep(1)

    def get_cameras(self):
        return self._cameras

