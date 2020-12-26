from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import ShortenForm
from .models import url_shorten
import random


def main_index(request):
    if request.method == "POST":
        form = ShortenForm(request.POST)
        genurl = gen_url()
        if form.is_valid():
            shorten_form = url_shorten(
                original_link=form.cleaned_data['original_link'],
                gen_link=genurl
            )

            messages.success(request, "{}".format(genurl))
            shorten_form.save()

    context = {
        "form": ShortenForm()
    }
    return render(request, 'url_shorten/index.html', context)


def redirect_view(request, gen_link):
    link = get_object_or_404(url_shorten, gen_link=gen_link)

    return HttpResponseRedirect('{}'.format(link.original_link))


def gen_url():

    url_list = url_shorten.objects.all()

    list_of_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
    gen_link = ""

    while gen_link == "" or gen_link == url_list:
        for i in range(0, 6):
            gen_link += (random.choice(list_of_letters))


    return gen_link
