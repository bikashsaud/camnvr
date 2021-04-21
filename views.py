from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from views.jazmin_view import JazminView
from views.mixins import AuthRequiredMixin
from service.camnvr_service import CamNVR
 
service = CamNVR()
service.start()

class DashboardIndexView(AuthRequiredMixin, JazminView):
    template_name = "../ui/dashboard.html"

    def __init__(self):
        super().__init__()

    def get(self, request, *args, **kwargs):
        context = self.auth_context(request)
        
        context["camera_details"] = service.get_cameras()
        # context["cam_frames"] = service.gen_frames(cam_id)

        return render(request, self.template_name, context=context)

def stream(request, id):
    return StreamingHttpResponse(service.gen_frames(id), mimetype='multipart/x-mixed-replace; boundary=frame')
    

        

