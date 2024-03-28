from django.urls import path
from .views import UserMemberListCreateView, UserMemberDetailView

urlpatterns = [
    path('members/', UserMemberListCreateView.as_view(), name='userMember-list-create'),
    path('members/<int:pk>/', UserMemberDetailView.as_view(), name='userMember-detail'),
]
