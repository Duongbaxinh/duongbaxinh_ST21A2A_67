from django.urls import path 
from . import views
urlpatterns = [ 
    path('',views.signupPage),
    path('homepage',views.homePage),
    path('signup',views.signup),
    path('sigin',views.sigin),
    path('login', views.loginPage),
    path('playmusic',views.musicPage),
    path('posts/<int:pk>/', views.postDetail, name='post_detail'),
    # path('home', views.blogPage),
    # path('login',views.loginPage),
    
    
]

