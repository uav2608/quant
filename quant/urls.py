from django.conf.urls import include, url
from django.contrib import admin
from stocklist.views import exchange_list
urlpatterns = [
    # Examples:
    # url(r'^$', 'quant.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^read_stock_list$', exchange_list),
]
