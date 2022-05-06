from django.urls import path
from django.views.generic.base import TemplateView # new
from .views import SignUpView, UserDetailView, UserListView, UserDetailWithArticles, UserFollowView, UserFollowersShowView, UserFollowingsShowView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('<int:user_id>/followers/', UserFollowersShowView.as_view(), name='user_followers_show'),
    path('<int:user_id>/followings/', UserFollowingsShowView.as_view(), name='user_followings_show'),
    path('signup/', SignUpView.as_view(), name = 'signup'),
    path('<int:user_id>/articles/', UserDetailWithArticles.as_view(), name='user-with-articles'),
    path('<int:user_id>/follow/', UserFollowView.as_view(), name='follow-user'),
]