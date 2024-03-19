from music import views
from django.urls import path
urlpatterns=[
    path('login/',views.loginPage,name="login"),
    path('music/',views.music),
    path('search/',views.search,name='search'),
    path('songs/',views.songs,name='songs'),
    path('songs/<int:id>',views.songposts,name="songs"),
    path('songs/<int:id>',views.songfront,name="songs"),
    path('allsong/<int:id>',views.allsong,name="songs"),
    path('recome/<int:id>',views.recome,name="songs"),
    path('loginverify/',views.login_view,name="login"),
    path('signUp/',views.signup,name="signup"),
    path('registration/',views.userregistration,name="registration"),
    path('contact/',views.contact,name='contact'),
    path('contactus/',views.contactus,name='contactus'),
    path('about/',views.about,name='about'),
    path('logout/',views.logout_view,name='logout'),
    # path('viewemployee/',views.viewEmployee,name="employee")
]