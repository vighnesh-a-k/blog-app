from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views


urlpatterns = [
    path("",views.home,name="home"),
    
    path('post/<uuid:post_id>/', views.post_detail, name='post_detail'),
    path("login/",views.user_login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("post/create/",views.create_article,name="create"),
    path('logout/', views.user_logout, name='logout'),
    path('post/delete/<uuid:post_id>/', views.delete_post, name='post_delete'),
    path('post/edit/<uuid:post_id>/', views.edit_post, name='post_edit'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    