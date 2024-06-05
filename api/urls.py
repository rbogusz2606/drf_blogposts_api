from django.urls import path
from . import views

urlpatterns = [
    path("", views.endpoints, name="endpoints"),
    path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path("blogposts/<uuid:pk>/", views.BlogPostRetrieveUpdatesDestroy.as_view(), name="update_delete"),
    path("login/", views.login, name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("signup/", views.signup, name="signup"),
]
