
from django.urls import path
from.import views
urlpatterns = [
   path('',views.homepage),
   path('count/',views.count,name="count"),
   #acceptting challeneges:
   path('about/',views.about,name='about'),
]
