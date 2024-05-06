from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.my_hanlder, name='index'),

    # <str:person_name>
    # path("hello", hello_handler, name="hello")
    # http://localhost:8000/polls/hello -> "polls:hello"

    path("test", views.show_questions, name='question'),

    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),

    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),

    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('abc', views.render_sugar, name="abc")
]
