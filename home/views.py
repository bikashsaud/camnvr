from django.shortcuts import render
from django.views.decorators import gzip
from django.views import View
from service.camnvr_service import CamNVR
from django.http import StreamingHttpResponse, HttpResponse
import cv2
 
service = CamNVR() 
service.start() 


class VideoCam(object):
	_template_name = "../templates/home.html"

	def __init__(self):
		super().__init__()

num_cameras = len(service.get_cameras())

def gen(cam_id):
	while True:
		frame = service.get_frame(cam_id)
		return frame
			# yield (b'--frame\r\n'
			# 	b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def stream(request):
	while True:
		for num in range(1, num_cameras):
			return StreamingHttpResponse(gen(num), content_type = 'multipart/x-mixed-replace; boundary=frame')

def home(request):
	context = {'number':num_cameras}
	return render(request, '../templates/home.html', context=context)#, context=context)

	# for n in range(1, self.num_cameras):
	# 	resp = self.stream_response(n)
	# 	print("value of get(): ",resp)
	# 	context={"frames": resp}


