from django.urls import path
from .views import (
    EmployeeListCreateView,
    EmployeeDeleteView,
    AttendanceCreateView,
    AttendanceListView,
    AttendanceSummaryView,
    DashboardSummaryView,
)

urlpatterns = [
    # Employees
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:id>/', EmployeeDeleteView.as_view(), name='employee-delete'),

    # Attendance
    path('attendance/', AttendanceCreateView.as_view(), name='attendance-create'),
    path('attendance/list/', AttendanceListView.as_view(), name='attendance-list'),

    # Bonus
    path('attendance/summary/', AttendanceSummaryView.as_view(), name='attendance-summary'),
    path('dashboard/summary/', DashboardSummaryView.as_view(), name='dashboard-summary'),
]
