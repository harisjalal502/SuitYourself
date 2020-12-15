#!/usr/bin/env python3

# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from suitYourself.models import Upload
from suitYourself.forms import UploadForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form': form})


def index(request):
    uploads = Upload.objects.all()
    return render(request, "home.html", {'uploads': uploads, 'form': UploadForm()})

def upload(request):
	# Handle file upload
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['description']
            size = form.cleaned_data['size']
            price = form.cleaned_data['price']
            newupload = Upload(uploadfile = request.FILES['uploadfile'], title = title, description = desc, size = size, price = price)
            newupload.save()

            # Redirect to the document list after POST
            return redirect('home')

# Delete post
def delete(request, objectid):
	object = get_object_or_404(Upload, pk=objectid)
	object.delete()
	return redirect('home')

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')