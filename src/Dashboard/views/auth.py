from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..decorators import login_not_required
from ..forms import SignInForm

# Create your views here.
@login_not_required
def signIn(request: HttpRequest):
  form = SignInForm()
  if request.method == 'POST':
    form = SignInForm(request.POST)
    if form.is_valid():
      user = authenticate(request=request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
      if user is not None:
        login(request=request, user=user)
        return redirect('dashboard')
      else:
        messages.error(request=request, message="Wrong username or password")

  context = { 'form': form }
  return render(request, 'pages/auth/sign-in.html', context=context)

@login_required(login_url='sign-in')
def signOut(request: HttpRequest):
  logout(request=request)
  return redirect('sign-in')