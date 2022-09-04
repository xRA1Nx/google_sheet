from django.urls import path

from .views import SheetDataListView

urlpatterns = [
    path('', SheetDataListView.as_view(), name="data")
]
