from django.shortcuts import render
from django.views.decorators import gzip
from django.views import View
from service.camnvr_service import CamNVR
from django.http import StreamingHttpResponse
import cv2
 
service = CamNVR()
service.start()

class HomeIndexView(View):
	template_name = "../templates/home.html"

	def __init__(self):
		super().__init__()

	def get(self, request, *args, **kwargs): 
		context = {}
		# context["img"] = frame
		# print(frame)
		return render(request, self.template_name, context=context)

		# def stream(request, id):
		# 	service.__class__._cam_id = id
		# 	return StreamingHttpResponse(gen_frames())  

