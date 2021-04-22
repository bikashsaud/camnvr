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

	def get(self, request, *args, **kwargs): 
		context = {}
		# cameras = service.get_cameras()
		# for cam_id, cam
		context["img"] = service.get_frame(0)
		print(context)
		return render(request, self.template_name, context=context)

		# def stream(request, id):
		# 	service.__class__._cam_id = id
		# 	return StreamingHttpResponse(gen_frames())  

