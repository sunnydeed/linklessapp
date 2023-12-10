from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from .forms import ShortenedLinkForm
from .models import ShortenedLink


class ShortenLinkView(FormView):
    form_class = ShortenedLinkForm
    template_name = "shortener/shorten_link.html"

    def form_valid(self, form):
        form.save()
        shortened_link_instance = form.instance
        short_code = shortened_link_instance.short_code

        # Redirect to the success URL with the short_code
        success_url = reverse("shortener:shorten_success", kwargs={"short_code": short_code})
        return HttpResponseRedirect(success_url)


class RedirectView(DetailView):
    model = ShortenedLink
    slug_field = "short_code"
    slug_url_kwarg = "short_code"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_expired():
            return render(request, "shortener/link_expired.html")
        return redirect(self.object.original_url)


class ShortenSuccessView(DetailView):
    model = ShortenedLink
    slug_field = "short_code"
    slug_url_kwarg = "short_code"
    template_name = "shortener/shorten_success.html"
