from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Shortener

from .forms import ShortenerForm


# Create your views here.
def index_view(request):
    template = 'shortener/index.html'

    context = dict()
    context['form'] = ShortenerForm()
    if request.method == 'GET':
        used_form = ShortenerForm()
    elif request.method == 'POST':
        used_form = ShortenerForm(request.POST)

        if used_form.is_valid():
            shortened_obj = used_form.save()

            new_url = request.build_absolute_uri('/') + shortened_obj.short_url

            long_url = shortened_obj.long_url

            context['new_url'] = new_url
            context['long_url'] = long_url
            context['form'] = ShortenerForm()
            return render(request, template, context)

        context['errors'] = used_form.errors
    return render(request, template, context)


def redirect_short_url_view(request, shortened_url_part):
    try:
        shortener_obj = Shortener.objects.get(short_url=shortened_url_part)
        shortener_obj.times_followed += 1
        shortener_obj.save()

        return HttpResponseRedirect(shortener_obj.long_url)
    except:
        return Http404('This link is invalid :(')
