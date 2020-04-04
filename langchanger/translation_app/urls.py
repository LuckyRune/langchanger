from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^main/$', views.MainPageView.as_view(), name='main-page'),
    url(r'^all-origin/$', views.AllOriginView.as_view(), name='all-origin'),
    url(r'^origin/$', views.OneOriginView.as_view()),
    url(r'^origin-translation/$', views.TranslationByLanguageView.as_view()),
    url(r'^read-origin/$', views.ReadOriginView.as_view()),
    url(r'^read-translation/$', views.ReadTranslationView.as_view()),
    url(r'^make-translation/$', views.MakeTranslationView.as_view()),
    url(r'^all-version/$', views.AllVersionView.as_view()),
    url(r'^version-differences/$', views.DifferencesVersionView.as_view()),
    url(r'^comment-origin/$', views.OriginCommentView.as_view()),
]
