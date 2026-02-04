from rest_framework import generics, views, status
from rest_framework.response import Response
from django.db.models import Count
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from .models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerializer, AttendanceSummarySerializer


# ===========================
# Employee APIs
# ===========================

@extend_schema(
    summary="List all employees",
    description="Retrieve a list of all employees.",
    responses={200: EmployeeSerializer(many=True)}
)
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @extend_schema(
        summary="Create a new employee",
        description="Add a new employee with unique employee ID and email.",
        responses={201: EmployeeSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


@extend_schema(
    summary="Delete an employee",
    description="Delete an employee by internal ID.",
)
class EmployeeDeleteView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'


# ===========================
# Attendance APIs
# ===========================

@extend_schema(
    summary="Mark attendance",
    description="Mark attendance for an employee on a specific date with status Present or Absent.",
    responses={201: AttendanceSerializer}
)
class AttendanceCreateView(generics.CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


@extend_schema(
    summary="List attendance records",
    description="Retrieve attendance records. You can filter by employee_id and/or date.",
    parameters=[
        OpenApiParameter(name='employee_id', description='Employee ID to filter', required=False, type=str),
        OpenApiParameter(name='date', description='Filter by date (YYYY-MM-DD)', required=False, type=str),
    ],
    responses={200: AttendanceSerializer(many=True)}
)
class AttendanceListView(generics.ListAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        queryset = Attendance.objects.all().order_by('-date')

        employee_id = self.request.query_params.get('employee_id')
        date = self.request.query_params.get('date')

        if employee_id:
            queryset = queryset.filter(employee__employee_id=employee_id)

        if date:
            queryset = queryset.filter(date=date)

        return queryset


# ===========================
# Attendance Summary API
# ===========================

@extend_schema(
    summary="Get total present days per employee",
    description="Returns total number of days each employee was marked Present.",
    responses={200: AttendanceSummarySerializer(many=True)}
)
class AttendanceSummaryView(views.APIView):
    def get(self, request):
        data = (
            Attendance.objects
            .filter(status='Present')
            .values('employee__employee_id', 'employee__full_name')
            .annotate(total_present_days=Count('id'))
            .order_by('-total_present_days')
        )

        formatted_data = [
            {
                "employee_id": item["employee__employee_id"],
                "full_name": item["employee__full_name"],
                "total_present_days": item["total_present_days"],
            }
            for item in data
        ]

        return Response(formatted_data, status=status.HTTP_200_OK)


# ===========================
# Dashboard Summary API
# ===========================

@extend_schema(
    summary="Get dashboard summary",
    description="Returns dashboard summary including total employees, attendance records, and optionally total present today.",
    parameters=[
        OpenApiParameter(name='date', description='Optional date to calculate total present for that day (YYYY-MM-DD)', required=False, type=str),
    ],
    responses={
        200: OpenApiExample(
            'Dashboard Summary',
            value={
                "total_employees": 10,
                "total_attendance_records": 250,
                "total_present_today": 8
            }
        )
    }
)
class DashboardSummaryView(views.APIView):
    def get(self, request):
        date = request.query_params.get('date')

        total_employees = Employee.objects.count()
        total_attendance_records = Attendance.objects.count()

        if date:
            total_present_today = Attendance.objects.filter(status='Present', date=date).count()
        else:
            total_present_today = None

        return Response({
            "total_employees": total_employees,
            "total_attendance_records": total_attendance_records,
            "total_present_today": total_present_today,
        }, status=status.HTTP_200_OK)
