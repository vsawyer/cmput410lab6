from django.conf.urls import patterns, include, url
from django.contrib import admin
from main import views
urlpatterns = patterns('',
# Examples:
# url(r'^$', 'bookmarks.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
url(r'^$',views.index, name='index'),
url(r'^tags/$',views.tags, name='tags'),
url(r'^tags/(?P<tag_name>\w+)/$',views.tag, name='tag'),
url(r'^add_link/$',views.add_link, name='add_link'),
) 