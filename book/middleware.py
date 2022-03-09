from django.http import HttpRequest, HttpResponse

def simple_middleware(get_response):
    def middleware(request):
        # 这里是请求前
        print("请求前")
        response = get_response(request)
        # 这里是响应后
        print("响应后")
        return response
    return middleware
