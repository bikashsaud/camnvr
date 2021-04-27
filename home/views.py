from django.shortcuts import render
from django.views.decorators import gzip
from django.views import View
from service.camnvr_service import CamNVR
from django.http import StreamingHttpResponse, HttpResponse
import cv2
 
service = CamNVR() 
service.start() 


def gen(cam_id):
	while True:
		frame = service.get_frame(cam_id)
		return frame
			# yield (b'--frame\r\n'
			# 	b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def stream(request):
	while True:
		# for num in range(1, numof_cameras):
		return StreamingHttpResponse(gen(2), content_type = 'multipart/x-mixed-replace; boundary=frame')

def home(request):
	numof_cameras = len(service.get_cameras())
	template_name = "../templates/home.html"
	context = {'number':numof_cameras}
	return render(request, template_name, context=context)#, context=context)

	# for n in range(1, self.num_cameras):
	# 	resp = self.stream_response(n)
	# 	print("value of get(): ",resp)
	# 	context={"frames": resp}


