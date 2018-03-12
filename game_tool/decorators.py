from django.core.exceptions import PermissionDenied


API_KEY = 'haohaoxuexi'


def api_key_required(function):
    def wrap(request):
        api_key = request.GET.get('api_key')
        if api_key == API_KEY:
            return function(request)
        else:
            raise PermissionDenied
    return wrap
