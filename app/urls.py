from django.urls import path
from . import views
from django.conf import settings  
from django.conf.urls.static import static 

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.intro, name='intro'),
    # path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    # path('logout', views.logout_view, name='logout'),
    path('openwhen/', views.openwhen, name='openwhen'),
    path('letter/<int:letter_id>', views.letter, name='letter'),
    path('timeline/', views.timeline, name='timeline'),
    path('happybirthday/', views.hbd, name='hbd'),
    path('gallery/', views.gallery, name='gallery'),
    path('surprise/', views.surprise, name='surprise'),
    path('reveal_gift/', views.reveal_gift, name='reveal_gift'),
 
]


  
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  