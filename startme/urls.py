from django.urls import path

from . import views
from django.conf import settings 
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home,name='home'),
    path('index', views.index, name='index'),
    # path('login', views.login_view, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('profile', views.profile, name='profile'),
    path('profilepage', views.profilepage, name='profilepage'),
    path('all_users', views.all_users, name='alluser'),
    path('hehe', views.hehe, name='hehe'),
    path('signupp', views.signupp, name='signupp'),
    path('test2', views.test2, name='test2'),
    path('hahe', views.hahe, name='hahe'),
    # path('allfree', views.allfree, name='allfree'),
    # path('userid/<int:pk>/',views.viewprofile, name='viewprofile'),
    path('userid/<int:id>/',views.viewprofile, name='viewprofile'),
    path('viewer', views.viewer, name='viewer')

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)