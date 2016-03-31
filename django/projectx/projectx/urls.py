from django.conf.urls import include, url
from django.contrib import admin
from arcadia import views
from projectx.views import index
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', 'projectx.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$',views.test),
    url(r'^mytest/$',views.mytest),
    url(r'^streamin/$',views.DataIn),
    #url(r'^temprequest/$',views.TempRequest),
    url(r'^humrequest/$',views.HumRequest),
    url(r'^co1request/$',views.CO1Request),
    url(r'^tempnow/$',views.TempNow),
    #url(r'^temprequests/$',views.TempRequests),
    url(r'^temprequest/$',views.TempRequestss),
    url(r'^morequest/$',views.MoRequest),


    
]
