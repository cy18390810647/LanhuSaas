from django.conf.urls import patterns

urlpatterns = patterns(
    'test1.views',
    (r'^test1', 'helloworld'),
)