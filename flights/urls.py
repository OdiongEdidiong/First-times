from django.urls import path
from . import views
urlpatterns=[
    path("",views.all_flights,name="flights"),
    path("flight/<int:id>/",views.one,name="flight"),
    path("dura/<int:id>",views.time,name="time"),
    path("add/",views.addflights,name="add"),
    path("addport/",views.addports,name="addports"),
    path("addstud/",views.addstuds,name="addstud")
]