from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as lib_views

urlpatterns = [
    path('', lib_views.LibraryView.as_view(), name="home"),
    path('library/', lib_views.LibraryView.as_view(), name="library"),
    path('library/populate', lib_views.LibraryPopulateView.as_view(), name="library-populate"),
    path('users/', lib_views.UsersView.as_view(), name="users"),
]

login_urls = [
    path('login/', lib_views.UserLogin.as_view(), name='login'),
    path('signup/', lib_views.UserSignup.as_view(), name='signup'),
    path('logout/', lib_views.UserLogout.as_view(), name='logout'),
] 

urlpatterns += login_urls