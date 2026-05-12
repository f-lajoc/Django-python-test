from django.shortcuts import render, redirect, resolve_url
from django.contrib import messages
from django.views import View
from apptest.models import ContactMessage
from django.contrib.auth.decorators import login_required

# Function based views

def homepage(request):
  return render(request, 'home.html')

@login_required
def aboutpage(request):
  return render(request, 'about.html')

def contactpage(request):
  if request.method == "POST":
    fullname = request.POST.get("fullname")
    email = request.POST.get("email")
    about = request.POST.get("about")
    if not fullname:
      messages.error(request, "Please provide your full name")
      return render(request, 'contact.html')
    if not email or not about:
      messages.error(request, "All fields are required")
      return render(request, 'contact.html')
    if len(fullname) < 5:
      messages.error(request, "Name is too short")
      return render(request, 'contact.html')
    
    messages.success(request, "Details is submitted")
    print(f'User submitted name {fullname}, email {email}, about {about}')
    return redirect(homepage)

  return render(request, 'contact.html')

def testimonialpage(request):
  return render(request, 'testimony.html')


  # CLASS BASED VIEWS
class ContactView(View):
  def get(self, request):
      return render(request, 'contact.html')
  
  def post(self, request):
    fullname = request.POST.get("fullname")
    email = request.POST.get("email")
    about = request.POST.get("about")
    if not fullname:
      messages.error(request, "Please provide your full name")
      return render(request, 'contact.html')
    if not email or not about:
      messages.error(request, "All fields are required")
      return render(request, 'contact.html')
    
    ContactMessage.objects.create(fullname = fullname, email = email, about = about )
    messages.success(request, "Details submitted")
    return redirect(resolve_url('home'))
  
