from django.shortcuts import render
from django.http import HttpResponse


def index_page_view(request):
    return render(request, 'index/index_page.html')
