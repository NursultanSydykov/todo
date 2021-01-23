from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3")

def fourth(request):
    return render(request, "index1.html")

def fifth(request):
    return render(request, "index2.html")

def sixth(request):
    return render(request, "index3.html")