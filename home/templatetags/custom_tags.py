from django import template
from service import camnvr_service
from service.camnvr_service import CamNVR
from django.http import StreamingHttpResponse
import time, base64
from django.template.loader import get_template

register = template.Library()

users_template = get_template('home.html')

# @register.simple_tag
# def stream():
# 	cameras = camnvr_service.get_cameras()
# 	for camera_id, cameras in cameras.items():
# 		return StreamingHttpResponse(CamNVR.gen_frames()) 
# def gen_frames():
#     while True:
#         frame_detail = CamNVR._frames.get(str(cam_id), None)
#         if frame_detail is not None:
#             frame = frame_detail.get("frame", None)
#             if frame is not None:
#                 ret, buffer = cv2.imencode('.jpg', frame)
#                 frame = buffer.tobytes()
#                 frame = (b'--frame\r\n'
#                          b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#                 yield frame
#             time.sleep(1)

# register.inclusion_tag(users_template)(gen_frames)
