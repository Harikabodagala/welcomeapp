from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    res=HttpResponse("""<html><body bgcolor=blue><center>
    <h1>welcome to lokeshit</h1></cemter></body></html>""")
    return res
