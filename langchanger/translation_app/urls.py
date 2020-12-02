from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^genre/list/$', views.GenreListView.as_view()),
    url(r'^language/list/$', views.LanguageListView.as_view()),

    url(r'^main/$', views.MainPageView.as_view(), name='main-page'),
    url(r'^origin/all/$', views.AllOriginView.as_view(), name='all-origin'),
    url(r'^origin/$', views.OneOriginView.as_view()),
    url(r'^origin/read/$', views.ReadOriginView.as_view()),
    url(r'^origin/search/$', views.SearchOriginView.as_view(), name='search-origin'),

    url(r'^comment-origin/$', views.OriginCommentView.as_view()),
    url(r'^comment-origin/add/$', views.CreateCommentOriginView.as_view()),
    url(r'^comment-origin/delete/$', views.ChangeCommentOriginView.as_view()),

    # statistic
    url(r'^statistic/comment-origin/', views.OriginCommentStatistic.as_view()),
]
