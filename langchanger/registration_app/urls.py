from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^all/$', views.AllUserView.as_view(), name='all-user'),
    url(r'^main-info/$', views.MainUserInfoView.as_view(), name='user-main-info'),
    url(r'^profile/$', views.ProfileUserView.as_view(), name='user-profile'),

    url(r'^achievement/$', views.AchievementView.as_view(), name='achievements'),
    url(r'^on-hold/$', views.OnHoldUserView.as_view(), name='user-on-hold'),

    url(r'^setting/$', views.SettingUserView.as_view(), name='user-setting'),
    url(r'^delete/$', views.SettingUserView.as_view(), name='user-delete'),

    url(r'^register/$', views.RegisterUserView.as_view(), name='registration'),

]
