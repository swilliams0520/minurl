from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from ipware.ip import get_ip

from .models import URL, Analytic


class URLForm(ModelForm):

    class Meta:
        model = URL
        fields = ['url']

def new_url(request):
    return render(request, 'new.html', {'URLForm': URLForm()})


def create_url(request):
    """
    this submits a url to the database, saves it, and creates a random id (slug)
    """
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save()
            return redirect('view_url', slug=url.slug)

def view_url(request, slug):
    url_object = get_object_or_404(URL, slug=slug)
    url = request.build_absolute_uri(reverse('goto_url', args=(slug, )))
    return render(request, 'show.html', {'url_object':url_object, 'url':url})

def goto_url(request, slug):
    url_object = get_object_or_404(URL, slug=slug)
    url_object.clicks += 1
    url_object.save()
    analytic = Analytic(url=url_object, ip_address=get_ip(request), referrer=request.META['HTTP_REFERER'])
    analytic.save()
    return redirect(url_object.url)
