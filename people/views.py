from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class People(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse("登录页面")
    def post(self, request):
        username = request.POST.get("username")
        return HttpResponse(username)
