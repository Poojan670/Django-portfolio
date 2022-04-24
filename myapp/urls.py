from django.urls import path
from .views import *

app_name = "myapp"

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('portfolio', PortfolioView.as_view(), name="portfolios"),
    path('portfolio/<slug:slug>', PortFolioDetailView.as_view(), name="portfolio"),
    path('blog/', BlogView.as_view(), name="blogs"),
    path('blog/<slug:slug>', BlogDetailView.as_view(), name="blog"),
]
