from django.conf.urls import url
from randf import views
from rest_framework.routers import SimpleRouter
#
# router = SimpleRouter(trailing_slash=True)
# router.register(r'register_user', views.RegisterUser)
# router.register(r'login_user', views.LoginUser)
# router.register(r'cc_details', views.CCDetails)
#
# router = SimpleRouter(trailing_slash=True)
# router.register(r'movie', views.MovieRating)

urlpatterns = [

    url(r'^movie/$', views.MovieRating.as_view()),
    url(r'^movie/', views.MovieRating.as_view()),
    url(r'^user/', views.User.as_view()),
    # url(r'^register_user/(?P<email>\d+)/$', views.RegisterUser.as_view()),
    #url(r'^login_user/$', views.LoginUser.as_view()),
    #url(r'^cc_details/$', views.CCDetails.as_view()),
    #url(r'^cc_details/$', views.CCDetails.as_view()),
    #url(r'^login/$', views.home,),
]

