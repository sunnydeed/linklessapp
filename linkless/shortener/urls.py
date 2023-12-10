from django.urls import path

from .views import RedirectView, ShortenLinkView, ShortenSuccessView

app_name = "shortener"
urlpatterns = [
    path("shorten/", ShortenLinkView.as_view(), name="shorten_link"),
    path("<str:short_code>/", RedirectView.as_view(), name="redirect"),
    path("shorten/success/<slug:short_code>/", ShortenSuccessView.as_view(), name="shorten_success"),
]
