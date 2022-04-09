from django.urls import path
from django.views.generic.base import TemplateView # new
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name = 'signup'),
]