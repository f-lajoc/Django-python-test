# Django Setup & Development Guide

A practical, step-by-step reference for building a Django web application from scratch — environment setup, routing, templates, forms, models, authentication, file uploads, error handling, and deployment to Render.

This guide is written as a working reference for Django beginners and as a personal knowledge base compiled while learning the framework hands-on.

---

## Table of Contents

- [Django Setup \& Development Guide](#django-setup--development-guide)
  - [Table of Contents](#table-of-contents)
  - [1. Prerequisites](#1-prerequisites)
    - [Check if Python is installed](#check-if-python-is-installed)
    - [Check if pip is installed](#check-if-pip-is-installed)
  - [2. Environment Setup](#2-environment-setup)
    - [Install virtualenv](#install-virtualenv)
    - [Create a virtual environment](#create-a-virtual-environment)
    - [Activate the virtual environment](#activate-the-virtual-environment)
  - [3. Creating the Django Project](#3-creating-the-django-project)
    - [Comments in Python](#comments-in-python)
    - [Start the development server](#start-the-development-server)
  - [4. Creating and Registering an App](#4-creating-and-registering-an-app)
    - [Register the app](#register-the-app)
    - [Wire up the app's URLs](#wire-up-the-apps-urls)
  - [5. Templates](#5-templates)
  - [6. Views](#6-views)
    - [Function-based views](#function-based-views)
  - [7. URL Routing \& Linking Pages](#7-url-routing--linking-pages)
    - [Wiring a view to a URL](#wiring-a-view-to-a-url)
    - [Adding more pages](#adding-more-pages)
    - [Linking pages in templates](#linking-pages-in-templates)
  - [8. Template Inheritance with Blocks](#8-template-inheritance-with-blocks)
    - [Including partial templates](#including-partial-templates)
  - [9. Handling Form Submissions](#9-handling-form-submissions)
    - [Reading submitted data](#reading-submitted-data)
  - [10. Displaying Backend Messages](#10-displaying-backend-messages)
    - [Rendering messages in a template](#rendering-messages-in-a-template)
  - [11. Redirects](#11-redirects)
  - [12. Class-Based Views](#12-class-based-views)
    - [Checking for code errors](#checking-for-code-errors)
  - [13. Models \& the Database](#13-models--the-database)
    - [Saving data to the database](#saving-data-to-the-database)
    - [Using non-sequential (UUID) primary keys](#using-non-sequential-uuid-primary-keys)
    - [Linking records with a foreign key](#linking-records-with-a-foreign-key)
  - [14. Admin Panel](#14-admin-panel)
    - [Registering a model](#registering-a-model)
    - [Making records human-readable](#making-records-human-readable)
  - [15. User Authentication (Signup, Login, Logout)](#15-user-authentication-signup-login-logout)
    - [Signup](#signup)
    - [Login](#login)
    - [Logout](#logout)
    - [Conditional navigation based on login state](#conditional-navigation-based-on-login-state)
  - [16. Restricting Access to Logged-In Users](#16-restricting-access-to-logged-in-users)
    - [Redirecting back to the originally requested page](#redirecting-back-to-the-originally-requested-page)
  - [17. Static Files (CSS, JS, Images)](#17-static-files-css-js-images)
  - [18. Media \& File Uploads](#18-media--file-uploads)
  - [19. .gitignore](#19-gitignore)
  - [20. Rendering and Linking Model Data](#20-rendering-and-linking-model-data)
    - [File uploads in forms](#file-uploads-in-forms)
  - [21. Editing Existing Records](#21-editing-existing-records)
  - [22. JSON Responses](#22-json-responses)
  - [23. Readable Admin Labels](#23-readable-admin-labels)
  - [24. Slugs (SEO-Friendly URLs)](#24-slugs-seo-friendly-urls)
    - [Using slugs instead of IDs throughout the project](#using-slugs-instead-of-ids-throughout-the-project)
  - [25. Custom Error Pages (404 / 500)](#25-custom-error-pages-404--500)
  - [26. Secret Keys \& Environment Variables](#26-secret-keys--environment-variables)
    - [Keeping secrets out of source control](#keeping-secrets-out-of-source-control)
  - [27. Cloud Storage for Media](#27-cloud-storage-for-media)
  - [28. Deploying to Render](#28-deploying-to-render)
  - [29. Serving Static Files in Production (WhiteNoise)](#29-serving-static-files-in-production-whitenoise)

---

## 1. Prerequisites

### Check if Python is installed

Open Command Prompt and run:

```bash
python --version
```

If Python isn't installed, download the latest version from [python.org](https://www.python.org) and run the installer. Accept all the default prompts during installation.

Reopen Command Prompt afterward and re-run `python --version` to confirm the installation succeeded.

### Check if pip is installed

```bash
pip --version
```

---

## 2. Environment Setup

### Install virtualenv

```bash
pip install virtualenv
```

> **Why use a virtual environment?**
> A virtual environment isolates the dependencies for each project. For example, if Project A uses Python 3 and Project B uses a newer version, a virtual environment keeps their packages separate so that installing or updating one project never breaks the other.

### Create a virtual environment

Run this in your project's terminal (VS Code or otherwise). You can name it anything, but `env` or `venv` is recommended — `.gitignore` templates for Django already exclude `env` by default. If you use a different name, you'll need to add it to `.gitignore` manually.

```bash
python -m venv env
```

### Activate the virtual environment

**Windows:**
```bash
env\scripts\activate
```

**macOS / Linux:**
```bash
source env/bin/activate
```

> **Note:** If Windows blocks the script with a "disabled" error, this is usually caused by PowerShell's execution policy. Switch to Command Prompt and run the activation command again.

Once active, your terminal prompt will be prefixed with `(env)`, confirming you're working inside the virtual environment — for example:

```bash
(env) PS C:\Users\user\OneDrive\Desktop\PYTHON>
```

Install all project packages while this prefix is visible. You'll need to reactivate the environment (`env\scripts\activate`) every time you return to the project in a new terminal session.

---

## 3. Creating the Django Project

Install Django:

```bash
pip install django
```

Create the project:

```bash
django-admin startproject projectname .
```

> The trailing `.` matters — without it, Django creates a nested project folder instead of placing files in the current directory.

**Do not modify `manage.py`.**

### Comments in Python

```python
# Single-line comment

"""
Multi-line comment
or docstring
"""
```

### Start the development server

```bash
python manage.py runserver
```

Then open the printed local address in your browser. Press `Ctrl + C` to stop the server.

> **Security tip:** Change the default `admin/` path in `urls.py` to something less predictable, to reduce the risk of automated attacks:
> ```python
> urlpatterns = [
>     path('anynameyouwant/', admin.site.urls),
> ]
> ```

---

## 4. Creating and Registering an App

Create an app:

```bash
django-admin startapp appname
```
or
```bash
python manage.py startapp appname
```

### Register the app

In the project's `settings.py`, add the app to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apptest',
]
```

### Wire up the app's URLs

In the app folder, create `urls.py`:

```python
from django.urls import path

urlpatterns = [
    # app-specific paths go here
]
```

In the project's `urls.py`, include the app's URLs:

```python
from django.urls import path, include

urlpatterns = [
    path('', include('apptest.urls')),          # root routes to the app
    path('apptest/', include('apptest.urls')),  # or under a prefix
]
```

---

## 5. Templates

In `settings.py`, under the `TEMPLATES` setting, either point `'DIRS': []` to a shared templates folder, or — the more common approach — create a `templates/` folder inside each app so every app owns its own templates.

Create your `.html` files inside that folder.

---

## 6. Views

Django supports two styles of views:

- **Function-based views (FBVs)** — simpler to learn, but require more repeated code.
- **Class-based views (CBVs)** — a slightly steeper learning curve, but more concise (see [Section 12](#12-class-based-views)).

### Function-based views

```python
def homepage(request):
    return render(request, 'home.html')
```

---

## 7. URL Routing & Linking Pages

### Wiring a view to a URL

Import the view and register its path:

```python
from apptest.views import homepage

urlpatterns = [
    path('', homepage),
]
```

### Adding more pages

1. Create the new template in the templates folder.
2. Define the view:
   ```python
   def aboutpage(request):
       return render(request, 'about.html')
   ```
3. Register the path:
   ```python
   path('about', aboutpage)
   ```

### Linking pages in templates

Name your URL in `urls.py`:

```python
path('', homepage, name='home')
```

Then reference it in a template using the `url` tag rather than a hardcoded path:

```html
<a href="{% url 'about' %}">About Her</a>
```

---

## 8. Template Inheritance with Blocks

Blocks let child templates override specific sections of a shared base template — ideal for elements common to every page, like the title or main content area, while still letting each page customize its own content.

**base.html:**
```html
<title>{% block titlename %}{% endblock titlename %}</title>
```

Pages that extend `base.html` don't need to repeat the `<!DOCTYPE>` or other boilerplate — they inherit everything automatically:

```html
{% extends 'base.html' %}

{% block title %}Homepage{% endblock title %}

{% block main %}
  <h1>A girl named Fola</h1>
  <a href="{% url 'about' %}">About Her</a>
{% endblock main %}
```

### Including partial templates

Use `{% include %}` to embed one template inside another — useful for reusable sections like a testimonials block on the homepage:

```html
{% include 'testimony.html' %}
```

---

## 9. Handling Form Submissions

Avoid the `GET` method for forms with sensitive data — it exposes all submitted values in the URL. Use `POST` instead, along with `{% csrf_token %}` in the form to protect against cross-site request forgery. Django generates a hidden, unique token automatically.

### Reading submitted data

```python
def contactpage(request):
    if request.method == "POST":
        fullname = request.POST["fullname"]
        print(f'User submitted name {fullname}')
        return render(request, 'contact.html')
    return render(request, 'contact.html')
```

> **Prefer `.get()` over direct key access.** Accessing `request.POST["key"]` raises an error if the key is missing. `request.POST.get("key")` returns `None` instead, so validation logic can run without crashing:

```python
def contactpage(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        about = request.POST.get("about")
        print(f'User submitted name {fullname}, about {about}')
```

---

## 10. Displaying Backend Messages

Django's built-in `messages` framework (already part of `INSTALLED_APPS`) sends feedback from the backend to the frontend.

```python
from django.contrib import messages

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

        messages.success(request, "Details submitted")
```

> Django templates use the Jinja-style template language, similar in spirit to how React uses JSX.

### Rendering messages in a template

Since every page inherits from `base.html`, placing the message loop there makes feedback appear on any page:

```html
<div class="error_container">
  {% for msg in messages %}
    <p>{{ msg }}</p>
  {% endfor %}
</div>
```

---

## 11. Redirects

```python
from django.shortcuts import render, redirect, resolve_url

return redirect(homepage)
# or, when the target view lives in a different file:
return redirect(resolve_url('home'))
```

---

## 12. Class-Based Views

```python
from django.views import View

class Contactview(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        return render(request, 'contact.html')
```

> Class names should use **PascalCase** (first letter capitalized).

Import and register the class-based view:

```python
from apptest.views import homepage, aboutpage, contactpage, testimonialpage, ContactView

path('contact', ContactView.as_view(), name='contact')
```

### Checking for code errors

```bash
python manage.py check
```

> This check isn't exhaustive — it won't catch every possible error.

---

## 13. Models & the Database

Define a model:

```python
from django.db import models

class ContactMessage(models.Model):
    fullname = models.CharField(max_length=250)
    email = models.EmailField()
```

> Django automatically adds an `id` field to every model.

Generate and apply migrations whenever a model is created or changed:

```bash
python manage.py makemigrations
python manage.py migrate
```

Running `migrate` also clears warnings like:
```
You have 19 unapplied migration(s). Your project may not work properly
until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
```

### Saving data to the database

```python
from app.models import ModelName

ModelName.objects.create(databaseField=value)
# e.g.
ContactMessage.objects.create(fullname=fullname, email=email, about=about)
```

### Using non-sequential (UUID) primary keys

To avoid predictable, sequential IDs:

```python
from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.PositiveBigIntegerField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField()
```

### Linking records with a foreign key

If, for example, products are posted by different users:

```python
from django.contrib.auth.models import User

user = models.ForeignKey(User, on_delete=models.CASCADE)
```

---

## 14. Admin Panel

Open the admin path defined in your project's `urls.py` to access the dashboard.

Django has three user types: **SuperUser**, **StaffUser**, and **NormalUser**.

Create a superuser:

```bash
python manage.py createsuperuser
```

You'll be prompted for a username, email, and password (input is hidden while typing).

> If prompted with a "password not strong enough" warning, type `y` to bypass it if desired.

### Registering a model

Models aren't visible in the admin panel by default. Register them in `admin.py`:

```python
from app.models import ModelName

admin.site.register(ModelName)
```

### Making records human-readable

Add a `__str__` method so records display meaningfully in the admin list, rather than as generic objects:

```python
class ContactMessage(models.Model):
    fullname = models.CharField(max_length=250)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.fullname} Email: {self.email}'
```

---

## 15. User Authentication (Signup, Login, Logout)

### Signup

Create an `authz` (or similarly named) app dedicated to authentication, with a `signup.html` template and a class-based view.

```python
from django.contrib.auth.models import User
from django.contrib import messages

class SignupView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        password = request.POST.get("password")

        if not username or not email or not firstname or not lastname or not password:
            messages.error(request, "All fields are required")
            return render(request, 'signup.html')

        if len(password) < 8:
            messages.error(request, "Password is too short")
            return render(request, 'signup.html')

        # Normalize case to prevent duplicate accounts differing only by case
        username = username.lower()
        email = email.lower()

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is taken")
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, 'signup.html')

        user = User.objects.create(
            username=username,
            email=email,
            first_name=firstname,
            last_name=lastname,
        )
        # Passwords are always hashed — never assign them directly on create()
        user.set_password(password)
        user.save()
```

> Inspect Django's built-in `User` model (Ctrl+Click on `User` in your editor) to confirm exact field names, such as `first_name`.

Register the view:

```python
from authz.views import SignupView

path('signup', SignupView.as_view(), name='signup')
```

Add a link to `signup` in your site navigation (`base.html`).

### Login

```python
from django.contrib.auth import login, logout, authenticate

def Loginview(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.error(request, "All fields are required")
            return render(request, 'login.html')

        username = username.lower()
        username_exists = User.objects.filter(username=username).first()

        if not username_exists:
            messages.error(request, "Invalid login credentials")
            return render(request, 'login.html')

        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, "Successful Login")
        return redirect(resolve_url('home'))

    return render(request, 'login.html')
```

### Logout

```python
def Logoutview(request):
    logout(request)
    return render(request, 'login.html')
```

Register both paths in `urls.py` and add them to the site navigation.

### Conditional navigation based on login state

```html
{% if user.is_authenticated %}
  <li><a href="{% url 'logout' %}">Logout</a></li>
{% else %}
  <li><a href="{% url 'signup' %}">Signup</a></li>
  <li><a href="{% url 'login' %}">Login</a></li>
{% endif %}
```

---

## 16. Restricting Access to Logged-In Users

```python
from django.contrib.auth.decorators import login_required

@login_required
def homepage(request):
    return render(request, 'home.html')
```

Tell Django where to send unauthenticated users, in `settings.py`:

```python
LOGIN_URL = 'authz/login'
```

### Redirecting back to the originally requested page

Capture the `next` parameter so users land on the page they originally tried to access after logging in:

```python
def Loginview(request):
    if request.method == "POST":
        next_page = request.GET.get('next')
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.error(request, "All fields are required")
            return render(request, "login.html")
```

---

## 17. Static Files (CSS, JS, Images)

Create a `static/` folder at the project root for CSS, JS, and images.

Load the `static` template tag at the top of the page, before `<!DOCTYPE>`, and link the stylesheet:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

In `settings.py`, after the `pathlib` import, add:

```python
import os

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
```

For per-page styling, define a `style` block in the base template and override it per page. Remember to load `static` below `extends`:

```html
{% extends 'base.html' %}
{% load static %}
```

Referencing an image:

```html
<img src="{% static 'assets/6.png' %}" alt="contact image" width="250px">
```

---

## 18. Media & File Uploads

Create a `media/` folder at the project root, then configure it in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

```python
image = models.ImageField(upload_to="product/")
```

`upload_to` organizes uploads into subfolders inside `media/` — useful since uploads can originate from different parts of the app.

Track creation and update timestamps:

```python
created_at = models.DateTimeField(auto_now_add=True)  # newest first
updated_at = models.DateTimeField(auto_now=True)
```

> Any model with an image or file field requires **Pillow**:
> ```bash
> pip install pillow
> ```

---

## 19. .gitignore

Generate a `.gitignore` file at [gitignore.io](https://www.toptal.com/developers/gitignore) for your stack (e.g., Django, React), and paste its contents into your project.

---

## 20. Rendering and Linking Model Data

Pass model data to a template via a context dictionary:

```python
class Products(LoginRequiredMixin, View):
    def get(self, request):
        all_products = Product.objects.all().order_by('-created_at')
        context = {'all_productskey': all_products}
        return render(request, 'products.html', context)
```

Loop through it in the template:

```html
<div class="all_products">
  {% for prod in all_productskey %}
    <div class="product-card">
      <h3>Name: {{ prod.name }}</h3>
      <img src="{{ prod.image.url }}" alt="{{ prod.name }}">
      <p>Description: {{ prod.description }}</p>
      <p>Quantity: {{ prod.quantity }}</p>
      <p>Seller: {{ prod.user.username }}</p>
    </div>
  {% endfor %}
</div>
```

> **Images not displaying?** Add media URL handling to your project's `urls.py`:
> ```python
> from django.conf import settings
> from django.conf.urls.static import static
>
> urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
> ```

### File uploads in forms

Forms that upload files must include `enctype="multipart/form-data"`, or the file data won't be sent.

---

## 21. Editing Existing Records

Use a dynamic URL segment for the record's ID:

```python
path('edit-product/<str:product_id>', EditProduct.as_view(), name='edit-product')
```

Verify ownership before allowing edits:

```python
class EditProduct(LoginRequiredMixin, View):
    def get(self, request, product_id):
        product = Product.objects.filter(id=product_id).first()
        if not product:
            return redirect(resolve_url("products"))
        if product.user != request.user:
            return redirect(resolve_url("products"))
        context = {"product": product}
        return render(request, 'edit_product.html', context)

    def post(self, request, product_id):
        product = Product.objects.filter(id=product_id).first()
        if not product:
            return redirect(resolve_url("products"))
        if product.user != request.user:
            return redirect(resolve_url("products"))

        name = request.POST.get("name")
        description = request.POST.get("description")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        image = request.FILES.get("image")

        product.name = name or product.name
        product.description = description or product.description
        product.price = price or product.price
        product.quantity = quantity or product.quantity
        product.image = image or product.image
        product.save()

        messages.success(request, "Product successfully updated")
        return redirect(resolve_url("products"))
```

Pre-populate the edit form with existing values:

```html
<label for="">Name</label><br>
<input type="text" name="name" required value="{{ product.name }}"><br>
<label for="">Description</label><br>
<textarea name="description">{{ product.description }}</textarea><br>
```

---

## 22. JSON Responses

Return a JSON list of records — useful for API-style endpoints.

```python
from django.http import JsonResponse
from django.forms import model_to_dict

def list_products(request):
    all_products = Product.objects.all()
    data = [
        {'name': x.name, 'id': x.id, 'quantity': x.quantity, 'image': x.image.url}
        for x in all_products
    ]
    return JsonResponse(data, safe=False)
```

Register the view:

```python
path("products/all", list_products, name="all-prod")
```

---

## 23. Readable Admin Labels

Add a `__str__` method to any model so it's easy to identify in the admin dashboard:

```python
def __str__(self):
    return f'{self.name} || {self.id}'
```

---

## 24. Slugs (SEO-Friendly URLs)

Slugs make URLs more readable and search-engine friendly:

```
Without slug: 127.0.0.1:8000/members/details/1
With slug:    127.0.0.1:8000/members/details/emil-refsnes
```

Add a `slug` field to the model:

```python
name = models.CharField(max_length=100)
slug = models.SlugField(unique=True, blank=True)
```

Run migrations after adding the field.

To auto-populate the slug from another field (e.g., a title), configure it in `admin.py`:

```python
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'featured', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'featured', 'category')
    search_fields = ('title', 'body')
```

> The slug is automatically "slugified" — hyphens replace spaces between words.

### Using slugs instead of IDs throughout the project

In templates:

```html
{% for category in categories %}
  <a href="{% url 'category' category.slug %}" class="category-chip">{{ category.name }}</a>
{% endfor %}

<h4><a href="{% url 'detail' post.slug %}">{{ post.title }}</a></h4>
<a href="{% url 'post_update' post.slug %}" class="btn-edit-action">Modify Content</a>
```

In `urls.py`, switch from `<int:id>` to `<slug:slug>`:

```python
path('', views.index_view, name='index'),
path('post/write/', views.PostCreateView.as_view(), name='post_create'),
path('post/<slug:slug>/', views.detail_view, name='detail'),
path('post/<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_update'),
path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
path('category/<slug:slug>/', views.category_view, name='category'),
```

In `views.py`, handle the slug instead of an ID:

```python
def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, status='published')
    return render(request, 'blog/category.html', {'category': category, 'posts': posts})
```

---

## 25. Custom Error Pages (404 / 500)

Create a template, e.g. `error_404.html`:

```html
<h1>Page Not Found</h1>
<p>The page you are looking for does not exist.</p>
<a href="{% url 'home' %}">
  <button>Go Home</button>
</a>
```

> **4xx** errors originate on the client side (e.g., a broken or mistyped link). **5xx** errors originate on the server side (e.g., an unhandled exception in your code).

Define the handler view:

```python
def error_404(request, exception):
    return render(request, 'error_404.html', status=404)
```

Wire it up at the project level in `urls.py`:

```python
handler404 = 'product.views.error_404'
handler500 = 'product.views.error_500'
```

---

## 26. Secret Keys & Environment Variables

Before deploying:

1. Replace `SECRET_KEY` in `settings.py` with a securely generated value — for example, via [Djecrety](https://djecrety.ir/).
2. Set `DEBUG = False`.
3. Replace the local `db.sqlite3` database with a production-ready one, e.g. [Neon](https://console.neon.tech/) or [Supabase](https://supabase.com/).
4. Install the PostgreSQL driver:
   ```bash
   pip install psycopg2
   ```

### Keeping secrets out of source control

Create a `.env` file in the project root (alongside `manage.py`) to store secret values. Since `.env` is listed in `.gitignore`, it won't be pushed to GitHub.

Install the packages needed to read it:

```bash
pip install python-decouple
pip install dj-database-url
```

In `settings.py`:

```python
from decouple import config
import dj_database_url

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

DATABASES = {
    'default': dj_database_url.parse(config('DATABASE_URL'))
}
```

Add your database connection URL (from Neon, Supabase, etc.) to `.env` as well.

> If your server doesn't recognize the new database, deactivate the virtual environment, open a fresh terminal, and reactivate it.

Since the online database is new, migrations must be re-applied:

```bash
python manage.py migrate
python manage.py createsuperuser
```

---

## 27. Cloud Storage for Media

For production, store uploaded media in the cloud rather than locally — options include **Cloudinary** and **Google Cloud Storage**.

---

## 28. Deploying to Render

1. Install Gunicorn (the WSGI server Render uses) — alternatives include Uvicorn or Daphne for ASGI:
   ```bash
   pip install gunicorn
   ```
2. Generate `requirements.txt` from the project root:
   ```bash
   pip freeze > requirements.txt
   ```
   Re-run this command whenever new packages are installed.
3. Push to GitHub:
   ```bash
   git add .
   git commit -m "Added requirements.txt"
   git push
   ```
4. In the Render dashboard: **New +** → **Web Service** → connect your GitHub repo.
5. Set the runtime to **Python**.
6. Start command:
   ```bash
   gunicorn project-name.wsgi:application
   ```
7. Environment variables: import directly from your `.env` file by copying and pasting it to render (including the secret key).
8. Update `ALLOWED_HOSTS` in `settings.py`:
   ```python
   ALLOWED_HOSTS = [
       "django-python-test.onrender.com",
       "localhost",
       "127.0.0.1",
   ]
   ```
   Or, to allow any Render subdomain:
   ```python
   ALLOWED_HOSTS = [
       "django-python-test.onrender.com",
       ".onrender.com",
   ]
   ```
9. Set `DEBUG = False`.
10. Push the changes:
    ```bash
    git add .
    git commit -m "Configured ALLOWED_HOSTS for Render"
    git push
    ```

---

## 29. Serving Static Files in Production (WhiteNoise)

If static files don't display correctly after deployment, configure **WhiteNoise**.

1. Confirm `STATIC_ROOT` is set in `settings.py`:
   ```python
   STATIC_ROOT = BASE_DIR / "static"
   ```
2. Add the WhiteNoise middleware directly after `SecurityMiddleware`:
   ```python
   MIDDLEWARE = [
       # ...
       "django.middleware.security.SecurityMiddleware",
       "whitenoise.middleware.WhiteNoiseMiddleware",
       # ...
   ]
   ```
3. Install WhiteNoise and update dependencies:
   ```bash
   pip install whitenoise
   pip freeze > requirements.txt
   ```
4. Commit and push the changes.

---

*This guide is a living document, updated as new concepts and patterns are learned.*
