FOR WINDOWS

## check if you have python on system

type cmd and open on pc, then run
`python --version`

- if python is not installed, download latest python from python.org and install after it is downloaded
  tick all boxes and true to whatever pop ups while installing it
- open cmd again and confirm if its installed by checking python version

## check if pip is installed

`pip --version`

## Then download virtualenv, run on cmd

`pip install virtualenv`

N:B it is good practice to always create a virtual environment in python projects, it helps to install the packages needed for that particular project, without affecting other project(e.g if project a was built with python version 3, and my new project is built with python version 12, with the help of virtual environment, i builds like a compartment for indiviual projects in such that one doesnt affect the other and the code doesnt break)(to avoid conflict of packages)

- run on project terminal in vscode, you can call your virtual environment any name but its recommended to mostly use 'env' or 'venv' because git .ignore already automatically use env but if you use adifferent name, youll havve to manually add it youself
  `python -m venv env`
- Activate virtual environment (N:B: you replace the env with your virtual environment name if you used a different name from env), run on terminal for windows
  `env\scripts\activate` </br>
  run on mac/linux `source env/bin/activate`
- if it throws an error after about it being disabled, it is the window security that is preventing it from running, just switch the terminal from powershell to command prompt and run the code again, it will work.
- Then install the necessary packages needed for your project,
  N:B make sure youre installing in your project that has env in terminal e.g ((env) PS C:\Users\user\OneDrive\Desktop\PYTHON> pip install django)
- You need to always reactivate the virtual environment anytime you come back to the project by running `env\scripts\activate`

# Install Django

- run `pip install django`
  N:B: ignore the pip upgrade notice
- then create django project, run `django-admin startproject projectname .`
  N:B: the "." after the project name is important because without it, it'll create a nested project folder for us
- Do not modify anything in the manage.py file

# Comment in python

single-line `# a single line comment`, multiple-line """this is for multiple line comments/docstring"""

# To start development server

- run ` python manage.py runserver` and open the port on browser
  N:B: Always change the default 'admin/' path in the urls.py file to a diff name to avoid hack `urlpatterns = [
    path('anynameyouwant/', admin.site.urls),
]`
- To stop server, click ctrl + c

# Create Django App

- then create django app, run `django-admin startapp projectname .` or run ` python manage.py startapp projectname`

# Register the app into the project

- Go to the project folder, open the settings.py file, then add all your created apps app into the 'INSTALLED_APPS' code block e.g
- `INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apptest'
]`
- Then create urls.py file in created app folder, then type `from django.urls import path`
- type `urlpatterns = [  
]`
- In project folder, urls.py file, import include e.g `from django.urls import path, include`
- then put a path for each app that you want your requests to be directed to e.g all requests will go to this url `path('', include('apptest.urls'))` and all request with apptest/ will go to this url `path('apptest/', include('apptest.urls'))`

# Create Template

- Go to project, the settings.py file, the 'TEMPLATES' code block, just put somethings showing where our template is located in the `'DIRS': []` configuraton or the better approach is in each app folder you create, create a new folder called templates in them so each app has their template folder
- then create html file in the created template folder

# Views

- then navigate to views.py file.
  N:B: There is Function based views(easier to learn but with more code blocks) and Class based views(bit complex to learn but with more lesser code blocks)

## Function based views

- define function that takes a request argument and return with the template page html e.g in the views.py file, type
  `def homepage(request):
   return render(request, 'home.html')`

# urls

- then navigate to urls.py file, import your function from the app views e.g `from apptest.views import homepage`
- and then add the path inside the 'urlpatterns' codeblock e.g `urlpatterns = [  
path('', homepage)
]`
- ### STEPS
- create other pages in template folder
- then in views.py file define function that returns the page e.g
  `def aboutpage(request):
   return render(request, 'about.html')`
- Then in urls.py file, add the path e.g `path('about', aboutpage)`

# To link pages

- you give the url name in url.py file e.g `path('', homepage, name='home')` and in the page html, for the anchor tag href, you put `{% url 'urlname' %}` to link the page e.g `<a href="{% url 'about' %}">About Her</a>`

# Block

- We create a block with a title name so we can dynamically change based on the active page... that is any page that extends from this page can provide their own title, or content unique to them (if our app contains something common to all pages of the app like a nav bar, we create a file that will contain the content so the other pages can just inherit it instead of repeating the codes and the block will be for the part that will change.) e.g
- `<title>{% block titlename %} {% endblock titlename %}</title>`
- in the other pages(home.html,about.html), no need to rewrite the doctype and other informations already in base.html, just include the new information that is different on the new page and extend the base.html data into i.e `{% extends 'base.html' %}` this code automatically imports all thats in base html.
- Then to add new contents on the page like home.html page, you put your contents within the starting and closing of the block tag e.g `{% block title %} Homepage {% endblock title %}`, it updates the page title and this contains the body content e.g
  `{% block main %} <h1>A girl named Fola</h1>
 <a href="{% url 'about' %}">About Her</a>
{% endblock main%}`
- You can include a page in another page(e.g each pages should show in homepage in sections) with `{% include 'nameofpage.html' %}` e.g `{% include 'testimony.html' %}` the testimonial will show in te home page.

# Form Submission

- for form submission, when you use get method, it shows all form details in the url, best method is post but it'll show csrf error, so add `{% csrf_token %}` in the form so django will automaticcally generate random token for us and the data will be hidden
- in views.py, we can retrieve the form details the user is sending to us by extracting it from the request code in the function e.g in contact function of view.py
  `def contactpage(request):
  if request.method == "POST":
  fullname = request.POST["fullname"]
  print(f'User submitted name {fullname}')
  return render(request, 'contact.html')
return render(request, 'contact.html')`
  - But the better approach is to add `.get` to extract because if a key name is not there using only POST to extract, it will throw an error but if we use `.get` to extract, if it is not there, it will ignore it and check for others e.g
    `def contactpage(request):
if request.method == "POST":
  fullname = request.POST.get("fullname")
  email = request.POST.get("email")
  about = request.POST.get("about")
  print(f'User submitted name {fullname}, about {about}')`

# Backend Security Check

- django has built in message app found inside INSTALLED_APPS = [], project settings.py file, which is used to send message from our backend to frontend. So we import it in views.py i.e `from django.contrib import messages` and use it in our function e.g
  `def contactpage(request):
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
    if len(fullname) <br 5:
      messages.error(request, "Name is too short")
      return render(request, 'contact.html')
    messages.success(request, "Details submitted")
`
  </br>N:B: Django uses JINJA Template just like React uses JSX
- We display the backend error message on the page by looping through the message inside the base.html file because all page inherits from it and so our error message can show wherever page we are
  `<div class="error_container">
{% for msg in messages %} <p>{{msg}}</p> 
{% endfor %}</div>`
  </br> remember to close the for loop with `endfor`

# Redirect and Resolve

- Import `from django.shortcuts import render, redirect, resolve_url`, then redirect after all requirements are filled to the page function you want to redirect to and/or to resolve if the page function is in a different file e.g `return redirect(homepage)` or `return redirect(resolve_url('home'))`

## Class based views

- import in views.py file, `from django.views import View`. The first letter of classname must be capitalized or PascalCasing e.g
  `class Contactview(View):
  def get(self, request):
      return render(request, 'contact.html')
  def post(self, request):
      return render(request, 'contact.html')`
- import your Class from the app views e.g `from apptest.views import homepage, aboutpage, contactpage, testimonialpage, ContactView`
- to add the path inside the 'urlpatterns' codeblock, you add `.as_view()` to the class name e.g `path('contact', ContactView.as_view(), name='contact')`

### To check python code error

- run `python manage.py check`</br> (not 100% valid, might not tell you some error)

# Creatin Table to store data in Database

- navigate to models.py, create models by creating a class but with `models.Model` e.g `class ContactMessage(models.Model):`
- N:B: django automatically gives each model an id value
- run `python manage.py makemigrations` to create migration file for our models
- then run `python manage.py migrate`, this will run all our migration file against our database to create the tables and it clears the error message `"You have 19 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions."`
- N:B anytime we modify our models or create new ones, we need to run the two migrations command
- in views.py, we import the models from app e.g `from app.models import ModelName`
- then put the details in database when form is successfully submitted by `ModelName.objects.create(databaseName=createdVariable)` e.g ` ContactMessage.objects.create(fullname = fullname, email = email, about = about )`

# Check our Database && Models

- go to project urls.py file and check the admin path, the open it on browser
- There are 3 users in django {SuperUser, StaffUser, NormalUser}
- We create superuser account by running `python manage.py createsuperuser`, it'll ask for username, email, password(it won't show on terminal when you're typing it in), then create the account successfully.
- N:B if you encOunter password not strong error and ask you to bypass it, type "y" to bypass it
- Then login with the details on the admin dashboard in browser
- A model by default is not registered on the admin panel so in admin.py file, we import our models e.g `from app.models import ModelName`
- Then we regsiter our model by `admin.site.register(ModelName)`. Then go reload Admin panel in browser
- to make the data more readable in the db, we add a method in the class model `def __str__(self):
  return self.valuename`
  </br>so the data will store the persons name as header in database e.g `class ContactMessage(models.Model):
fullname = models.CharField(max_length=250)
email = models.EmailField()
def __str__(self):
  return f'Name: {self.fullname} Email: {self.email}'`
  - Create a new app for authentication, do the necessary steps for app creation, create a signup.html in the new app templates and write your code, create class based view in view.py
  - Then import `from django.contrib.auth.models import User` in views.py, then write a check to see if a user data already exists in database `if User.objects.filter(variable=variable).exists()` but convert the value to lowercase first so it doesn't escape the check `variable = variable.lower()` e.g

#### OR

- if we don't want the models id to be predictable, in models.py file we `import uuid` then input `id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)` e.g
  `from django.db import models
import uuid
class Product(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
  name = models.CharField(max_length=250)
  description = models.TextField()
  price = models.PositiveBigIntegerField()
  quantity = models.PositiveIntegerField()
  image = models.ImageField()`
- if we want to link another table e.g if products belongs and was posted by different users, import `from django.contrib.auth.models import User` and then use `user = models.ForeignKey(User, on_delete= models.CASCADE)` in models.py file

# Go to page

def get(self, request):
return render(request, 'signup.html')

# Extract Details

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

# variable case conversion

    username = username.lower()
    email =email.lower()

# Database exist checks

    if User.objects.filter(username=username).exists():
      messages.error(request, "Username is taken")
      return render(request, 'signup.html')
    if User.objects.filter(email=email).exists():
      messages.error(request, "Email already exists")
      return render(request, 'signup.html')```

- then save the details `user = User.objects.create(username=username, email=email, first_name=firstname, last_name=lastname)`
- N:B check out the user model (ctrl + click User) to see how the databaseName is written e.g first_name also don't put password together because it is always hashed and it'll be tried to save as plain text there, put it separate.
- then set the password `user.set_password(password)` and then save it `user.save()`
- then inurls.py, import view e.g `from authz.views import SignupView` and in urlpath codeblock, input class based view path e.g `path('signup', SignupView.as_view(), name='signup')`
- Then add the signup to navigation in base.html
- - Create login.html in templates and put the necessary code in it, then in the views.py, create a login view function with the necessary checks for form submission e.g
    ` def Loginview(request):
    if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      if not username or not password:
        messages.error(request, "All fields are required")
        return render(request, 'login.html')
    username = username.lower()
    username_exists = User.objects.filter(username = username).first()
    if not username_exists:
      messages.error(request, "Invalid login credentials")
      return render(request, 'login.html')
    return render(request, 'login.html')`

- import `from django.contrib.auth import login, logout, authenticate` in views.py
- then we authenticate to see if password match for the account created `user = authenticate(username = username, password=password)`
- then we allow login if all is correct with `login(request, user)` e.g `login(request, user)
   messages.success(request, "Successful Login")
   return redirect(resolve_url('home'))`
- then add the path in urls.py
- go to views.py and create a logout function `def Logoutview(request):
    logout(request)
    return render(request, 'login.html')`
- then add the path in urls.py, also add it to navigation in base.html header
- in the main page to do condition so logout only displays when user is logged in `	{% if user.is_authenticated %}` e.g
- `{% if user.is_authenticated %}
				<li><a href="{% url 'logout' %}">Logout</a></li>
				{% else %}
				<li><a href="{% url 'signup' %}">Signup</a></li>
				<li><a href="{% url 'login' %}">Login</a></li>
				{% endif %}`

# To Display on LoggedIn

- in app view.py, import `from django.contrib.auth.decorators import login_required`, then we put this decorator `@login_required` at the top of any function we want accessed only on login e.g `@login_required
def homepage(request):
  return render(request, 'home.html')`

- Then anywhere inside settings.py file, we input `LOGIN_URL = 'authz/login'`
- go to views.py, in the function, after the post request, put `next_page = request.GET.get('next')` this put the right url when you try accessing a page andor get redirected to login before accessing the page e.g `def Loginview(request):
  if request.method == "POST":
      next_page = request.GET.get('next')
      username = request.POST.get("username")
      password = request.POST.get("password")
      if not username or not password:
        messages.error(request, "All fields are required")
        return render(request, "login.html")`

# to style CSS

- At the root level, create folder called 'static', you can put css, js, images in here
- in the meta of the template pages, link the stylesheet `	<link rel="stylesheet" href="{% static 'css/style.css' %}">` but for it to work, at the top of the page before DOCTYPE, put `{% load static %}`
- them `import os` after the "from pathlib" in settings.py file, and put this after the "static_url" at the bottom `STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)`
- for different styling in each pages, create a block style in the base page and the use the block in each pages and put the link, also load static below "extends" e.g `{% extends 'base.html' %}
{% load static %}`
- add text e.g `<img src="{% static 'assets/6.png' %}" alt="contact image" width="250px" >`, load static at the head of page below extend

# storage for uploaded files (local storage) && Models

- create a folder at root level and add the url variable at bottom in setting.py file e.g `MEDIA_URL = '/media/'` and then add the directory variable to save our uploads to `MEDIA_ROOT = os.path.join(BASE_DIR, 'media')`
- N:B: `image = models.ImageField(upload_to="product/")` the "upload to" means it will create a product folder inside our media folder and save there, this is better because uploading can come from different part of the app so to keep things organized
- to show the recently uploaded first i.e when created `created_at = models.DateTimeField(auto_now_add=True)`
- to show when updated `updated_at = models.DateTimeField(auto_now=True)`
- N:B: Anytime we want to add image/file field in Models, we need to have a library called "Pillow" installed using `pip install pillow`
-

# .gitignore

- create a .gitignore file, go to gitignore.io, search for the software you're using on it (Django, React), copy and paste everything in the gitignore

# To Deploy ( on Render)
- we can deply projects with backend on render, vercel, pythonanywhere
- when deploying, wsgi server we can use is gunicorn or asgi server we can use is uvicorn, daphne
- On terminal install gunicorn `pip install gunicorn`, Render needs it.
- then Generate requirements.txt with `pip freeze > requirements.txt`, ensure you're at the root folder, this lists all our installed packages with their version, also you can rerun it whenever you install some other packages so that it can update
- Push to GitHub `git add .
git commit -m "Added requirements.txt"
git push`

- Go to: Render Dashboard
- Click: New + → Web Service
- Connect your GitHub repo:
- Fill manually: Runtime → Python
- for the start command box: $ gunicorn project-name.wsgi:application
- for environment variable: click import from .env file, then copy and paste everything in the .env file including secret key and paste there
- Open the settings.py and change the 'ALLOWED_HOSTS = []' to `ALLOWED_HOSTS = [
    "django-python-test.onrender.com",
    "localhost",
    "127.0.0.1",
]`
- or use this instead, The .onrender.com allows all Render subdomains. `ALLOWED_HOSTS = [
    "django-python-test.onrender.com",
    ".onrender.com",
]`
- Also change: 'DEBUG = True' to `DEBUG = False`
  -then Push to GitHub `git add .
git commit -m "Configured ALLOWED_HOSTS for Render"
git push`

# Create Dictionary

- ref to class Products in views.py, we create a context dictionary that takes key value pair and send it to frontend, the dict can be created outside the request and parsed in e.g `class Products(LoginRequiredMixin, View):
 def get(self, request):
    all_products = Product.objects.all().order_by('-created_at')
    context = {
       'all_productskey': all_products
    }
    return render(request, 'products.html', context)`
- then we write a for loop that picks the product one after the other in frontend, ref to products.html file e.g

```
<div class="all_products">
{% for prod in all_productskey %}
<div class="product-card">
 <h3>Name: {{prod.name}}</h3>
<img src="{{prod.image.url}}" alt="{{prod.name}}">
 <p>Description: {{prod.description}}</p>
 <p>Quantity: {{prod.quantity}}</p>
 <p>Seller: {{prod.user.username}}</p>
</div>
{% endfor %}
</div>
```
- N:B: The image will not display, so we go to project url.py and add a configuration. import settings and static i.e `from django.conf import settings` and `from django.conf.urls.static import static`
- then add to urlpatterns `urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`
# form files upload
- N:B we must include `enctype="multipart/form-data` in our form so that our uploaded files can be sent
# to edit a product
- ref to product urls.py, the path will have `<>` for dynamic input of the product id e.g `path('edit-product/<str:product_id>', EditProduct.as_view(), name='edit-product')`
- in product views.py, for the edirproduct view make checks to see it is the seller trying to update the product e.g
- ```python
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

      product.name = name or  product.name
      product.description = description or  product.description
      product.price = price or  product.price
      product.quantity = quantity or  product.quantity
      product.image = image or  product.image
      product.save()
      messages.success(request, "Product successfully updated")
      return redirect(resolve_url("products"))```
- then go to the editproduct html and the input boxes there put value to populate with the already existing informations of the product e.g
```html
<label for="">Name</label></br>
<input type="text" name="name" required value="{{product.name}}"></br>
<label for="">Description</label></br>
<textarea name="description">{{product.description}}</textarea></br>
```
# Json response
- to return json list of all our products, import Json Response by `from django.http import JsonResponse` and define a function in views.py e.g 
- `def list_products(request):`
- then import and add the view to path in urls.py e.g ` path("products/all", list_products, name="all-prod")`
- we convert the list of objects to a  dicionary we can send back to user, import in views.py `from django.forms import model_to_dict` this will convert all models to dictionary e.g 
   ```def list_products(request):
   all_products = Product.objects.all()
   data = [{'name': x.name, 'id': x.id, 'quantity': x.quantity, 'image': x.image.url} for x in all_products]
   return JsonResponse(data, safe=False)```
#  models products named properly in admin dashboard
- go to product models.py where we created the product, create a method in it and use the identifier you want 
```
  def __str__(self):
    return f' {self.name} || {self.id}'
```
# models slug
- it is used in url's to make them easier to read and search engine friendly
- Url Without Slug: 127.0.0.1:8000/members/details/1 vs Url With Slug: 127.0.0.1:8000/members/details/emil-refsnes
- go to models.py file and add a field called slug in the model, use the data type SlugField: e.g reference to Afriblog blog models.py file
```class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
```
- then makemigrations nd migrate to update the database
- if we want this field to be updated automatically when we set the title, we use `prepopulated_fields ` 
- go to admin.py and add it e.g ref to Afriblog blog admin.py file ```
  class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'featured', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'featured', 'category')
    search_fields = ('title', 'body')```

n:b the "slug" field will be auto populated with the title, and since the it is of type SlugField, it will "slugify" the value, meaning it will put a hyphen between each word.
  - we can replace the ID field with the slug field throughout the project. e.g ref to Afriblog >blog> template > blog index.html, detail.html, category.html
  ```
    {% for category in categories %}
        <a href="{% url 'category' category.slug %}" class="category-chip">{{ category.name }}</a>
    {% endfor %}
 <h4><a href="{% url 'detail' post.slug %}">{{ post.title }}</a></h4>}
  <a href="{% url 'post_update' post.slug %}" class="btn-edit-action">Modify Content</a>
```
- then go to urls.py, Change from <int:id> to <slug:slug> e.g ref to Afriblog blog urls.py file
```urlpatterns = [
     path('', views.index_view, name='index'),
    path('post/write/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/', views.detail_view, name='detail'),
    path('post/<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('category/<slug:slug>/', views.category_view, name='category'),
]```
- then finally go to views.py, change the details view to handle incoming request as slug instead of ID e.g ref to Afriblog blog views.py file
```def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, status='published')
    return render(request, 'blog/category.html', {'category': category, 'posts': posts})
  ```
# custom error messages
- create a html file for it in our template e.g 
- ```{% block main %}
    <h1>Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="{% url 'home' %}">
        <button>Go Home</button>
    </a>
{% endblock %}```
note: error 400 and above is error from udserend, maybe they navigated to page that doesnt exist while error 500 and above is from our end, maybe there was a break in our code
- the define the error in views.py e.g `def error_404(request, exception):
      return render(request, 'error_404.html', status=404)`
- then go to project level urls.py, create two variables called `handler404` and `handler500`, then direct them to the error message e.g `handler404 = 'product.views.error_404'` and `handler500 = 'product.views.error_500'` i.e it should go to our product app, the views and the error fuction there
  
# secret key
- in your project settings.py file, change your `SECRET_KEY` to something secure, you can search for 'django secret key generator' online site:https://djecrety.ir/ , and generate a secret key
note: change `DEBUG` to `False` before deployment
note: change database from the `db.sqlite3` we have for our project to one usable for production. one of the databases we can use is "Neon (https://console.neon.tech/)" or "superbase (https://supabase.com/)", create account on them

- then to connect to a postgress database, we need to install an engine called 'psycopg2'. run `pip install psycopg2`
- when we have secret key that we dont want to be exposed, we create an environment variable file for it and use python decouple to read the environment variable e.g create a file named '.env' file In your project root (the same folder that contains manage.py), so all secret keys can be kept in there and the file will not be pushed to github because its in listed .gitignignore file
- then clear the key value and python decouple can read it
- then install these two `pip install python-decouple` and `pip install dj-database-url`
- in settings.py file, import config from decouple whcich reads .env file, and dj-database-url  which allows us to connect to a database url using connection url  i.e `from decouple import config` and `import  dj_database_url`
- then in settings.py file, use config and the key of the key-value pair saved in .env file e.g `SECRET_KEY = config('SECRET_KEY')`, for debug, so the decoder doesnt read it as string, we add `cast=bool` e.g `DEBUG = config('DEBUG', default=False, cast=bool)`
- Also put the database url you get from neon(or other database) in .env file
- create or replace the database key in settings.py file and parse the database url into the default e.g 
  `DATABASES = {
    'default': dj_database_url.parse(config('DATABASE_URL')
    )
}`
- if on server run, it doesnt recognize the database, just deactivate the env. i.e run `deactivate`, then delete and open a new terminal, then reactivate env
- the reason we have unapplied migrations is bacuse we migrated on the previous local database, but this is a new online database, so we habve to run migration again i.e `python manage.py migrate`
- create user on the online db since it doesnt have any data yet, the prev data we have is on local db so run `python manage.py createsuperuser`

# Cloud for media
- we can create a cloud to save our medias in it instead of locally, use 'Cloudinary, Google Cloud e.t.c'
  
# static file not displaying properly on deployement, use WhitNoise
- Make sure staticfiles is configured correctly in settings.py file `STATIC_ROOT = BASE_DIR / "static"`
- Enable WhiteNoise- The WhiteNoise middleware should be placed directly after the Django SecurityMiddleware and before all other middleware e.g 
`MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]`
- then install whitenoise, run `pip install whitenoise`, rerun `pip freeze > requirements.txt  ` to add it to requirements.txt and commit changes