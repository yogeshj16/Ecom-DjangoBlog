from django.shortcuts import render
from django.http import HttpResponse


def post_list(reguest):
    return render(reguest, "blog/post_list.html")
