from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^format-type/list/$', views.FormatTypeListView.as_view()),
    url(r'^genre/list/$', views.GenreListView.as_view()),
    url(r'^language/list/$', views.LanguageListView.as_view()),

    url(r'^main/$', views.MainPageView.as_view(), name='main-page'),
    url(r'^origin/all/$', views.AllOriginView.as_view(), name='all-origin'),
    url(r'^origin/$', views.OneOriginView.as_view()),
    url(r'^origin/translation/$', views.TranslationByLanguageView.as_view()),
    url(r'^origin/read/$', views.ReadOriginView.as_view()),
    url(r'^origin/search/$', views.SearchOriginView.as_view(), name='search-origin'),

    url(r'^translation/read/$', views.ReadTranslationView.as_view()),
    url(r'^translation/add/$', views.MakeTranslationView.as_view()),
    url(r'^translation/add-version/$', views.MakeTranslationView.as_view()),
    url(r'^translation/delete/$', views.MakeTranslationView.as_view()),

    url(r'^version/all/$', views.AllVersionView.as_view()),
    url(r'^version/delete/$', views.DeleteVersionView.as_view()),
    url(r'^version/differences/$', views.DifferencesVersionView.as_view()),

    url(r'^comment-origin/$', views.OriginCommentView.as_view()),
    url(r'^comment-origin/add/$', views.CreateCommentOriginView.as_view()),
    url(r'^comment-origin/delete/$', views.ChangeCommentOriginView.as_view()),

    url(r'^rate/add/$', views.MakeRateView.as_view()),
    url(r'^rate/delete/$', views.MakeRateView.as_view()),
]
