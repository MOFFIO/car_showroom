from django.utils.deprecation import MiddlewareMixin

from cars_project.models import RequestInfo


class CoolMiddleware(MiddlewareMixin):

    def process_request(self, request, *args, **kwargs):
        if request.method == 'POST' and 'carform' in request.path:
            user_ri = RequestInfo.objects.create(user=request.user)
            user_ri.http_cookie = request.COOKIES
            user_ri.post_data = request.POST
            user_ri.url = request.build_absolute_uri()
            user_ri.save()
            return None
        return



