from django.urls import re_path
from cards.views import CardCollection, CardRecord, TaskCollection, TaskRecord



urlpatterns = [
    #collction  URL: /api/cards
    re_path(
        r'cards$',
        #with collection url, you can list all the books or create a new book
        CardCollection.as_view(),
        name='card-collection'
    ),
    # record URL: /api/cards/1
    re_path(
        r'cards/(?P<pk>[0-9]+)$',
        CardRecord.as_view(),
        name='card-record'

    ),
    re_path(
        r'tasks$',
        TaskCollection.as_view()
    ),
    re_path(
        r'tasks/(?P<pk>[0-9]+)$',
        TaskRecord.as_view(),
        name='task-record'
    )
    ]
