from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^login_user/$', views.login_user, name='login_user'),

	# url(r'^register/$', views.register_user, name='register_user'),
	url(r'^login/$', auth_views.login, {'template_name': 'user_info/login.html'},name='login'),
    # url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'products/products.html'}, name='logout'),
    url(r'^admin/', admin.site.urls),
]