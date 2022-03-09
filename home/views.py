from datetime import datetime

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
from django.views import View


class Home(View):
    def get(self, request):
        username = request.GET.get("username")
        if username is None:
            username = ""
        return render(request, "index.html", {"username": username, "hd": datetime.now()})
    def post(self, request):
        username = request.POST.get("username")
        if username is None:
            username = ""
        print(username)
        return render(request, "index.html", {"username": username, "hd": datetime.now()})
