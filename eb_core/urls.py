from django.urls import path

from . import views

urlpatterns = [
    path("", views.Index_View.as_view(), name="index"),
    path("group_sighting/", views.Group_Sighting_List.as_view(), name="group sighting list"),
    path("group_sighting/create/", views.Group_Sighting_Create.as_view(), name="group sighting create"),
    path("group_sighting/<int:pk>/", views.Group_Sighting_View.as_view(), name="group sighting view"),
    path(
        "group_sighting/earthranger_sighting/",
        views.EarthRanger_Sighting_List.as_view(),
        name="earthranger sighting list",
    ),
    path(
        "group_sighting/earthranger_sighting/create/",
        views.EarthRanger_Sighting_Create.as_view(),
        name="earthranger sighting create",
    ),
    path(
        "group_sighting/earthranger_sighting/<int:earthranger_serial>/",
        views.EarthRanger_Sighting_View.as_view(),
        name="earthranger sighting view",
    ),
    path("subgroup_sighting/", views.Subgroup_Sighting_List.as_view(), name="subgroup sighting list"),
    path("subgroup_sighting/<int:pk>/", views.Subgroup_Sighting_View.as_view(), name="subgroup sighting view"),
    path("individual_sighting/", views.Individual_Sighting_List.as_view(), name="individual sighting list"),
    path(
        "individual_sighting/individual/<int:pk>/",
        views.Individual_Sighting_Individual_List.as_view(),
        name="individual sighting list individual",
    ),
    path("individual_sighting/queue/", views.Individual_Sighting_Queue.as_view(), name="individual sighting queue"),
    path(
        "individual_sighting/expert_queue/",
        views.Individual_Sighting_Expert_Queue.as_view(),
        name="individual sighting expert queue",
    ),
    path(
        "individual_sighting/unidentified/",
        views.Individual_Sighting_Unidentified_List.as_view(),
        name="individual sighting unidentified list",
    ),
    path("individual_sighting/<int:pk>/", views.Individual_Sighting_View.as_view(), name="individual sighting view"),
    path("individual/", views.Individual_List.as_view(), name="individual list"),
    path("individual/create/", views.Individual_Create.as_view(), name="individual create"),
    path("individual/combine/", views.Individual_Combine.as_view(), name="individual combine"),
    path("individual/<int:pk>/", views.Individual_View.as_view(), name="individual view"),
    path("search/", views.Search_View.as_view(), name="search"),
    path("stats/", views.Stats_View.as_view(), name="stats"),
    path("view_media/<path:name>/", views.Media_View.as_view(), name="view media"),
    path("ebuser_create/", views.EBUser_Create.as_view(), name="ebuser create"),
]
