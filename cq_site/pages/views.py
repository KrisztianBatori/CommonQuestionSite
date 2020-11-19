from django.shortcuts import render, redirect
from comments.models import Comment
from threads.models import Thread
from categories.models import Category
from users.models import User
from django.db import connection
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.timezone import now
from .forms import ThreadCreationForm


def home_view(request):

    threads = Thread.objects.all()
    users = User.objects.all()
    categories = Category.objects.all()
    cursor = connection.cursor()
    cursor.execute("SELECT thr_title, thr_id, CASE thr_upvotes WHEN 0 THEN 0 ELSE FLOOR((thr_upvotes::float / (COALESCE(thr_upvotes,0) + COALESCE(thr_downvotes,0)) / 100::float) * 10000) END AS ratio FROM thread GROUP BY thr_downvotes, thr_title, thr_upvotes, thr_id ORDER BY thr_id")
    votes = cursor.fetchall()

    context = {
        'categories': categories,
        'users': users,
        'threads': threads,
        'votes': votes
    }

    return render(request, "home.html", context)


def thread_view(request, id):

    thread = Thread.objects.get(thr_id=id)
    users = User.objects.all()
    comments = Comment.objects.filter(com_thrlocation=id)

    context = {
        'thread': thread,
        'comments': comments,
        'users': users
    }

    return render(request, "thread.html", context)


def user_view(request, id):

    user = User.objects.get(usr_id=id)
    threads = Thread.objects.filter(thr_author=id)
    comments = Comment.objects.filter(com_author=id)

    context = {
        'user': user,
        'threads': threads,
        'comments': comments
    }

    return render(request, "user.html", context)


def reg_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, 'Account was created for ' + user)
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO usr (usr_name, usr_registrationdate, usr_totalupvotes, usr_totaldownvotes) values (%s, %s, %s, %s);", [user, now(), 0, 0])
        return redirect('/pages')
    context = {
        'form': form
    }
    return render(request, "register.html", context)


def log_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/pages')
        else:
            messages.info(request, 'Username or password is incorrect!')

    return render(request, "login.html")


def logoutUser(request):
    logout(request)
    return redirect('/pages')


def thread_creation_view(request):
    form = ThreadCreationForm(request.POST or None, initial={'thr_author': User.objects.get(usr_name=request.user.username).usr_id})
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, "createthread.html", context)
