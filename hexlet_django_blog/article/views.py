from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View


class IndexView(View):
    def get(self, request):
        return HttpResponse('Hello, World!')


# def index(request):
#     context = {'name': 'article app'}
#     return render(request, 'article/index.html', context=context)