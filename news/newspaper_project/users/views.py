import profile
from re import template
from statistics import mode
from django.urls import reverse, reverse_lazy
from django.views import View
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# from pkg_resources import require
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


class UserListView(ListView):
    model = CustomUser
    template_name = 'user_list.html'


class UserFollowersShowView(ListView):
    def get(self, request, user_id, **kwargs):
        user = CustomUser.objects.get(id=user_id)
        self.object_list = user.followers.all()
        context = {
            'user': user,
            'articles': user.articles.all(),
            'is_follow': request.user.followings.filter(id=user.id).exists(),
            'followings': user.followings.count(),
            'followers': user.followers.count(),
            'object_list': user.followers.all(),
        }
        return render(request, 'user_list.html', context)

class UserFollowingsShowView(ListView):
    def get(self, request, user_id, **kwargs):
        user = CustomUser.objects.get(id=user_id)
        self.object_list = user.followings.all()
        context = {
            'user': user,
            'articles': user.articles.all(),
            'is_follow': request.user.followings.filter(id=user.id).exists(),
            'followings': user.followings.count(),
            'followers': user.followers.count(),
            'object_list': user.followings.all(),
        }
        return render(request, 'user_list.html', context)

class UserDetailWithArticles(LoginRequiredMixin, View):
    def get(self, request, user_id, **kwargs):
        user = CustomUser.objects.get(id=user_id)
        context = {
            'user': user,
            'articles': user.articles.all(),
            'is_follow': request.user.followings.filter(id=user.id).exists(),
            'followings': user.followings.count(),
            'followers': user.followers.count(),
        }
        return render(request, 'user_detail_with_articles.html', context)


class UserFollowView(LoginRequiredMixin, View):
    def post(self, request, user_id: int):
        user = CustomUser.objects.get(id=user_id)
        print(user.username)
        authenticated_user = CustomUser.objects.get(username=request.user.username)
        is_subs = authenticated_user.followings.filter(id=user.id).exists()
    
        if not is_subs:
            authenticated_user.followings.add(user)
            user.followers.add(authenticated_user)

        else:
            authenticated_user.followings.remove(user)
            user.followers.remove(authenticated_user)
            
        return redirect(reverse('user-with-articles', kwargs=dict(user_id=user_id)))
    

# class UserFollowerView(LoginRequiredMixin, View):
#     def get(self, request, user_id, **kwargs):
#         user = CustomUser.objects.get(id=user_id)
#         articles = user.articles.all()
#         return render(request, 'user_detail_with_articles.html', {'user': user, 'articles': articles, 'follows' : user.profile.follows.all()})

