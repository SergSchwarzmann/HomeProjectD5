from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, PostSearch, ProfileUpdate


urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_ceate'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('profile/<int:pk>/edit', ProfileUpdate.as_view(), name='profile_update'),
]