from rest_framework import serializers
from .models import Employee, Attendance


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'employee_id', 'full_name', 'email',
                  'department', 'created_at', 'updated_at']

    def validate_employee_id(self, value):
        if Employee.objects.filter(employee_id=value).exists():
            raise serializers.ValidationError("Employee ID already exists.")
        return value

    def validate_email(self, value):
        if Employee.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value


class AttendanceSerializer(serializers.ModelSerializer):
    employee_id = serializers.CharField(write_only=True)
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)

    class Meta:
        model = Attendance
        fields = ['id', 'employee_id', 'employee_name', 'date', 'status', 'created_at', 'updated_at']

    def validate(self, data):
        employee_id = data.get('employee_id')
        date = data.get('date')

        try:
            employee = Employee.objects.get(employee_id=employee_id)
        except Employee.DoesNotExist:
            raise serializers.ValidationError({"employee_id": "Employee not found."})

        if Attendance.objects.filter(employee=employee, date=date).exists():
            raise serializers.ValidationError("Attendance already marked for this employee on this date.")

        data['employee'] = employee
        return data

    def create(self, validated_data):
        validated_data.pop('employee_id')
        return super().create(validated_data)


class AttendanceSummarySerializer(serializers.Serializer):
    employee_id = serializers.CharField()
    full_name = serializers.CharField()
    total_present_days = serializers.IntegerField()