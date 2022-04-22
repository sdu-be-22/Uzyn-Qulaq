from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm
from .models import CustomUser

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
class UserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    login_url = 'login'
    template_name = 'user_detail.html'

