from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def login_page(request):
	template = 'user_info/login.html'
	context = {}
	return render(request, template, context)


def login_user(request):
    username = request.POST['user_name']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        template = 'products/products.html'
        context = {}        
        return render(request, template, context_instance=RequestContext(request))
    else:
        raise Http404("User does not exist")


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
    return render(request, 'user_info/signup.html', {'form': form})