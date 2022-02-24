from django.urls import path
from . import views
app_name = "blog"

urlpatterns = [
    path('', views.home, name = "bloghome"),
    path('readingpost/<int:num>', views.readingpost, name = "readingpost"),
    path('comments', views.comments, name = "comment"),
    path('updatecomment', views.updatecomment, name = "updatecomment"),
    path('deletecomment/<int:num>/<int:pnum>', views.deletecomment, name = "deletecomment")
]