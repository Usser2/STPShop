from django.contrib.auth import authenticate


class AuthTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'auth_token' in request.COOKIES:
            auth_token = request.COOKIES['auth_token']
            user = authenticate(request=request, auth_token=auth_token)
            if user is not None:
                request.user = user
        response = self.get_response(request)
        return response
