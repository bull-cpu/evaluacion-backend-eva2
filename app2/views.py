from django.shortcuts import render

# Create your views here.
def app2v1(request):
    return render(request,"app2/v1.html")

def app2v2(request):
    return render(request,"app2/v2.html")