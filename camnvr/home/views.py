from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views import View

from camnvr.service.camnvr_service import CamNVR

service = CamNVR()
service.start()


class HomeIndexView(View):
    template_name = "../templates/home.html"

    def __init__(self):
        super().__init__()

    def get(self, request, *args, **kwargs):
        context = {"camera_details": service.get_cameras()}
        # context["cam_frames"] = service.gen_frames(cam_id)

        return render(request, self.template_name, context=context)


def stream(request, id):
    return StreamingHttpResponse(service.gen_frames(id), mimetype='multipart/x-mixed-replace; boundary=frame')
