from django.conf.urls import url,include
from django.contrib import admin
from restapp import views

admin.autodiscover()

urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.SynonymList.as_view()),
    url(r'^(?P<pk>\d+)/$', views.SynonymDetail.as_view(),name='detail'),
    )
