from rest_framework import serializers
from .models import Run, RunData

class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = ['id', 'description', 'start_time', 'end_time']

class RunDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunData
        fields = ['id', 'run', 'temperature', 'humidity', 'water_level', 'time_stamp', 'kp', 'ki', 'kd', 'output']
