from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^all/$', views.AllUserView.as_view(), name='all-user'),
    url(r'^main-info/$', views.MainUserInfoView.as_view(), name='user-main-info'),
    url(r'^profile/$', views.ProfileUserView.as_view(), name='user-profile'),
    url(r'^search/$', views.AllUserView.as_view(), name='search-user'),

    url(r'^achievement/$', views.AchievementView.as_view(), name='achievements'),

    url(r'^on-hold/$', views.OnHoldUserView.as_view(), name='user-on-hold'),
    url(r'^on-hold/add/$', views.ChangeOnHoldUserView.as_view(), name='add-on-hold'),
    url(r'^on-hold/delete/$', views.ChangeOnHoldUserView.as_view(), name='delete-on-hold'),

    url(r'^setting/$', views.SettingUserView.as_view(), name='user-setting'),
    url(r'^delete/$', views.SettingUserView.as_view(), name='user-delete'),

    url(r'^register/$', views.RegisterUserView.as_view(), name='registration'),

    url(r'^banned/$', views.BanUserView.as_view(), name='banned-user'),
    url(r'^ban/$', views.BanUserView.as_view(), name='ban-user'),
    url(r'^unban/$', views.BanUserView.as_view(), name='unban-user'),
    url(r'^ip-ban/$', views.BanUserIPView.as_view(), name='ip-ban-user'),

    url(r'^test/$', views.TestView.as_view(), name='test'),
]
