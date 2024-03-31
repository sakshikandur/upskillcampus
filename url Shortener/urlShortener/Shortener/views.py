from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Url
import uuid

def  index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST.get('link', '')
        uuid_str = str(uuid.uuid4())[:5]
        new_url = Url.objects.create(link=link, uuid=uuid_str)
        return HttpResponse(uuid_str)
    else:
        return HttpResponse("Only POST requests are allowed for this endpoint.")

from django.shortcuts import redirect, HttpResponse
from .models import Url

def go(request, pk):
    try:
        url_details = Url.objects.get(uuid=pk)  # Query based on the 'uuid' field
        redirect_url = url_details.link

        if not redirect_url.startswith(('http://', 'https://')):
            redirect_url = 'http://' + redirect_url

        print("Original URL:", redirect_url)  # Assuming HTTP if no protocol provided
        return redirect(redirect_url)
    except Url.DoesNotExist:
        return HttpResponse("URL not found", status=404)
    except Exception as e:
        return HttpResponse("Error: {}".format(str(e)), status=500)






# def go(request,pk):
#     try:
#         url_details= Url.objects.get(pk=pk)
#         redirect_url = url_details.link
       
#         if not redirect_url.startswith(('http://', 'https://')):
#             redirect_url = 'http://' + redirect_url
#         print("Original URL:", redirect_url)  # Assuming HTTP if no protocol provided
#         return redirect(redirect_url)
#     except Url.DoesNotExist:
#         return HttpResponse("URL not found", status=404)
#     except Exception as e:
#         return HttpResponse("Error: {}".format(str(e)), status=500)
    



