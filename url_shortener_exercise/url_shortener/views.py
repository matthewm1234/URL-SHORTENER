from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import ShortURL
from .forms import ShortenURLForm


def shorten_url(request):
    if request.method == 'POST':
        form = ShortenURLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            # short_url is now generated using shortuuid
            shortened_url = ShortURL.objects.create(original_url=original_url)
            return JsonResponse({'shortened_url': shortened_url.short_url})
    else:
        form = ShortenURLForm()

    return render(request, 'url_shortener/shorten_url.html', {'form': form})


def resolve_url(request, short_url):
    shortened_url = get_object_or_404(ShortURL, short_url=short_url)
    original_url = shortened_url.original_url
    return render(request, 'url_shortener/resolve_url.html', {'original_url': original_url})
