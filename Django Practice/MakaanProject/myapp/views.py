from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def error(request):
    return render(request,'404.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def propertyagent(request):
    return render(request,'property-agent.html')

def propertylist(request):
    return render(request,'property-list.html')

def propertytype(request):
    return render(request,'property-type.html')

def testimonial(request):
    return render(request,'testimonial.html')