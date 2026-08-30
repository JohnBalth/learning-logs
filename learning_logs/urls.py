from django.urls import path

from . import views


app_name = 'learning_logs'


urlpatterns = [

    path('', views.index, name='index'),

    path('topics/', views.topics, name='topics'),

    path(
        'topics/<int:topic_id>/',
        views.topic,
        name='topic'
    ),

    path(
        'topics/new/',
        views.new_topic,
        name='new_topic'
    ),

    path(
        'topics/<int:topic_id>/edit/',
        views.edit_topic,
        name='edit_topic'
    ),

    path(
        'topics/<int:topic_id>/delete/',
        views.delete_topic,
        name='delete_topic'
    ),

    path(
        'topics/<int:topic_id>/new_entry/',
        views.new_entry,
        name='new_entry'
    ),

    path(
        'entries/<int:entry_id>/edit/',
        views.edit_entry,
        name='edit_entry'
    ),

    path(
        'entries/<int:entry_id>/delete/',
        views.delete_entry,
        name='delete_entry'
    ),

    path(
        'register/',
        views.register,
        name='register'
    ),

]