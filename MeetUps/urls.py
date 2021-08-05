# from django.urls import path

# from . import views

# urlpatterns = [
#     path('MeetUps/', views.index, name='all-meetups'), #our-domain.com/MeetUps
#     path('MeetUps/<str:meetup_slug>', views.meetup_detials, name='meetup-detail'), #our-domain.com/meetups/<dynamic-path-segment> 

# ]
from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='all-meetups'), # our-domain.com/meetups
  path('<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
  path('<slug:meetup_slug>', views.meetup_details, name='meetup-detail'), # our-domain.com/meetups/<dynamic-path-segment>
]
