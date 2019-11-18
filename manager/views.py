from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User
from manager.forms import VideoModelForm, RegisterForm
from .models import VideoModel
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password
import datetime
import subprocess
from django.db.models import Q


# Create your views here.
class HomeView(TemplateView):
    template_name = 'manager/home.html'

    def get(self, request, *args, **kwargs):
        q = VideoModel.objects.all()
        context = {
            'q': q
        }
        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class UploadView(TemplateView):
    template_name = 'manager/upload.html'

    def get(self, request, *args, **kwargs):
        form = VideoModelForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        profile = VideoModel()
        thumbnail = profile.thumbnail
        videofile = profile.videofile
        form = VideoModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            profile1 = form.save(commit=False)
            profile1.created_on = datetime.datetime.now()
            profile1.date = datetime.date.today()
            profile1.save()
            return redirect('home')
        else:
            form = VideoModelForm()
        context = {
            'thumbnail': thumbnail,
            'videofile': videofile,
            'form': form
        }
        return render(request, self.template_name, context)


@login_required()
def EditMetaView(request, title):
    post = VideoModel.objects.get(title=title)
    if request.method == "POST":
        form = VideoModelForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = VideoModelForm(instance=post)
    template = 'manager/editmeta.html'
    context = {
        'form': form,
        'post': post
    }
    return render(request, template, context)


class Signup(TemplateView):
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create(username=form.cleaned_data['email'],
                                       password=make_password(form.cleaned_data['password1']))
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class SearchView(ListView):
    model = VideoModel
    template_name = 'manager/search.html'

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        form = VideoModel.objects.get(title=query)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class FilterView(ListView):
    model = VideoModel
    template_name = 'manager/filter.html'

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        form = VideoModel.objects.filter(date=query)
        context = {
            'form': form,
            'query': query
        }
        return render(request, self.template_name, context)


class Filter1View(ListView):
    model = VideoModel
    template_name = 'manager/filter.html'

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        query = float(query)
        form = VideoModel.objects.filter(duration__lte=query)
        context = {
            'form': form,
            'query': query
        }
        return render(request, self.template_name, context)
