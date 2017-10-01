from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'email_registration.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include("pages.urls", namespace="pages")),
    url(r'^accounts/', include("accounts.urls", namespace="accounts")),
    url(r'^registration/', include('registration.backends.default.urls')),
]
