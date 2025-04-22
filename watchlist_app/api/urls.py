from django.urls import path,include
# from watchlist_app.api.views import movie_list,movie_detail
from watchlist_app.api.views import WatchDetailAV,WatchListAV,ReviewDetail,ReviewCreate,StreamPlatformListAV,ReviewList

urlpatterns = [
    path("list/", WatchListAV.as_view() ,name='movie_list'),
    path('<int:pk>/',WatchDetailAV.as_view(),name='movie_detail'),
    path('stream/',StreamPlatformListAV.as_view(),name='stream_platform'),
    # path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='stream_detail'),
    path('<int:pk>/review-create/',ReviewCreate.as_view(),name='review_create'),
    path('<int:pk>/review/',ReviewList.as_view(),name='review_list'),
    path('review/<int:pk>',ReviewDetail.as_view(),name='review_detail'),

]
