from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm, ProfileForm

def sign_in(request):
    if request.user.is_authenticated:
        return redirect("students:list")
    form = SignInForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, "Welcome back!")
        return redirect("students:list")
    return render(request, "accounts/login.html", {"form": form})

def sign_up(request):
    if request.user.is_authenticated:
        return redirect("students:list")
    form = SignUpForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        messages.success(request, "Account created. Please sign in.")
        return redirect("accounts:login")
    return render(request, "accounts/register.html", {"form": form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out.")
    return redirect("accounts:login")

@login_required
def profile_view(request):
    # simple read-only profile page; you can extend with edit form if needed
    return render(request, "accounts/profile.html", {})


@login_required
def edit_profile(request):
    user = request.user
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=user)
    return render(request, "accounts/edit_profile.html", {"form": form})
