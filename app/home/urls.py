from django.urls import path, re_path
from . import views

urlpatterns = [ 
    path('',views.home, name='home'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('signup/',views.signup, name='signup'),
    path('member/',views.member, name='member'),
    path('add/',views.add, name='add'),
    path('addrec/',views.addrec, name='addrec'),
    path('delete/<uuid:id>/',views.delete, name='delete'),
    path('update/<uuid:id>/',views.update, name='update'),
    

]