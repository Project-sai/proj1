from django.urls import path
from Employee_attendance import views


urlpatterns = [
    path('emp_report/',views.emp_report,name="individual_report"),
    path('all_empreports/',views.all_emp_reports,name="totaldetailed_report"),
    path('manual/attendance/update/',views.ManualAttendanceUpdate,name='manual_attendance_update'),
    path('manual/attendance/display/',views.ManualAttendanceDisplay,name='manual_attendance_display'),
    path('count_reports/',views.count_reports,name="total_report"),
    path('count_reports/<str:dep>/<str:dt>/',views.demo),
]