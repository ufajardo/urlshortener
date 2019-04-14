from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import ShortenForm
from .models import url_shorten
import random

def main_index(request):
    form = ShortenForm()
    if request.method == "POST":
        form = ShortenForm(request.POST)
        genurl = gen_url()
        if form.is_valid():
            shorten_form = url_shorten(
                original_link=form.cleaned_data['original_link'],
                gen_link=genurl
            )

            messages.success(request, "Your link is 127.0.0.1:8000/{}".format(genurl))
            shorten_form.save()

    context = {
        "form": ShortenForm()
    }
    return render(request, 'url_shorten/index.html', context)


def redirect_view(request, gen_link):
    link = get_object_or_404(url_shorten, gen_link=gen_link)

    return HttpResponseRedirect('{}'.format(link.original_link))


def gen_url():
    list_of_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    gen_list = ""

    for i in range(0, 6):
        gen_list += (random.choice(list_of_letters))

    return gen_list