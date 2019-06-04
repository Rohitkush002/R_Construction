from django.urls import path
from . import views as sides_view

urlpatterns = [
    path('side/', sides_view.side, name='side'),
    path('work/', sides_view.work, name='work'),
    path('sidelist/', sides_view.sidelist, name='sideList'),
    path('workList/', sides_view.workList, name='workList'),
    path('workingSide/<str:id>/', sides_view.workingSide, name='workingSide'),
    path('sideincharge/', sides_view.sideincharge, name='sideincharge'),
    path('delete/<int:id>', sides_view.delete, name='delete_side'),
    path('update/<int:id>', sides_view.update, name='update_side'),
    path('deletework/<int:id>', sides_view.deleteWork, name='delete_work'),

]
