from django.shortcuts import render
from django.views.decorators import gzip
from django.views import View
from service.camnvr_service import CamNVR
from django.http import StreamingHttpResponse
import cv2
 
service = CamNVR() 
service.start()


# def index(reques):
# 	return render(request, '../templates/home.html')


class HomeIndexView(View):
	template_name = "../templates/home.html"

	def __init__(self):
		super().__init__()
		# self.service = CamNVR() 
		# self.service.start()

	def gen(self, cam_id):
		while True:
			frame = service.get_frame(cam_id)
			print(type(bytes))
			print(frame)
			return frame
			# yield (b'--frame\r\n'
			# 	b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

	def get(self, request, *args, **kwargs):
		while True:
			return StreamingHttpResponse(self.gen(1),
				content_type='multipart/x-mixed-replace; boundary=frame')  
		# cameras = service.get_cameras()
		# for cam_id, cam
		# context ={"img": service.get_frame(1), "txt": "this is text"}
		# print(context)
		# return render(request, self.template_name, context=context)

		# def stream(request, id):
		# 	service.__class__._cam_id = id
		# 	return StreamingHttpResponse(gen_frames())  

