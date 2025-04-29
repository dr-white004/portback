from django.urls import path
from .views import RegisterView, UserProfileListCreateView, UserProfileDetailView, PortfolioListCreateView, PortfolioDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('userprofiles/', UserProfileListCreateView.as_view(), name='userprofiles'),
    path('userprofiles/<int:pk>/', UserProfileDetailView.as_view(), name='userprofile-detail'),
    path('portfolios/', PortfolioListCreateView.as_view(), name='portfolios'),
    path('portfolios/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio-detail'),
]
