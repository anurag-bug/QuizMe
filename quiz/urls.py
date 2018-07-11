from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout
urlpatterns = [

    url(r'^(?P<id>\d+)/api/$',views.apiResponse,name='api_response'),
    url(r'^(?P<id>\d+)/results/$',views.showResponse),
    url(r'^login/$',login,{'template_name':'quiz/login.html'}),
    url(r'^signup/$',views.signup),
    url(r'^response/(?P<quiz_id>\d+)/$',views.recordResponse),
    url(r'^create/$',views.createQuiz),

]