from django.conf.urls import url
from college import views

urlpatterns = [


    url(r'^hello$', views.hello , name='hello'),
    url(r'^hello_world$', views.hello_world , name='hello_world'),
    url(r'^myform$', views.myForm , name='myform'),
    url(r'^create$', views.create , name='create'),
    url(r'^test$', views.getData , name='test'),
    url(r'^change_password$', views.changePassword , name='change_password'),
    url(r'^download_excel$', views.downloadAsExcel , name='download_excel'),

    url(r'^index$', views.index , name='index'),
    url(r'^paramredi$', views.paramRedi , name='paramredi'),
    url(r'^update/(?P<pk>[0-9]+)$', views.update , name='update'),
    url(r'^delete/(?P<pk>[0-9]+)$', views.delete , name='delete'),
    url(r'^view/(?P<dk>[0-9]+)$', views.view , name='view'),

    url(r'^ajax_example$', views.ajaxExample,name='ajax_example'),
    url(r'^profile$', views.profile_form,name='profile'),
    url(r'^create_emp$', views.createEmp,name='create_emp'),
    url(r'^update_emp/(?P<pk>[0-9]+)$', views.updateEmp,name='update_emp'),
    url(r'^index_emp$', views.indexEmp, name='index_emp'),
    #url(r'^view_emp$', views.indexStudent, name='view_emp'),

    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^register$', views.signUp, name='signUp'),
    url(r'^login$', views.signIn, name='signIn'),

    url(r'^create_student$', views.createStudent , name='create_student'),
    url(r'^index_student$', views.indexStudent , name='index_student'),
    url(r'^update_student/(?P<pk>[0-9]+)$', views.updateStudent , name='update_student'),
    url(r'^delete_student/(?P<pk>[0-9]+)$', views.deleteStudent , name='delete_student')
]
