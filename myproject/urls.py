"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
import myapp.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',myapp.views.index),
    url(r'^droppipe_accessories/$',myapp.views.droppipe_accessories),
    url(r'^manifold_accessories/$',myapp.views.manifold_accessories),
    url(r'^header_accessories/$',myapp.views.header_accessories),
    url(r'^show_price/$',myapp.views.show_price),
    url(r'^manifold_price/$',myapp.views.manifold_price),
    url(r'^header_price/$',myapp.views.header_price),
    url(r'^show_accessories_priceinfo/$',myapp.views.show_accessories_priceinfo),
    url(r'^totalcost/(?P<totalcost_id>[-\w,.*%#!=+@&$()?_^|  /&]+)', myapp.views.download_est_rpt,
        name='download_est_rpt'),

]
