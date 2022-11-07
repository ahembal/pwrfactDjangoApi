from rest_framework import serializers

from .models import Experiment, Record

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)

class ExperimentIdSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    experiment_number = serializers.CharField(read_only=True)
    # owner = UserPublicSerializer(source='user_id', read_only=True)


class RecordSerializer(serializers.ModelSerializer):
    # experiment_id = ExperimentIdSerializer(source='experiment_id')
    experiment_detail = ExperimentIdSerializer(source='experiment_id', read_only=True)
    measurement_order = serializers.IntegerField()
    resistance = serializers.FloatField()
    voltage = serializers.FloatField()
    temp = serializers.FloatField()

    class Meta:
        model = Record
        fields = [
            'experiment_detail',
            'experiment_id',
            'pk',
            'measurement_order',
            'resistance',
            'voltage',
            'temp',
        ]
        read_only_fields = ()

class ExperimentSerializer(serializers.ModelSerializer):
    user_detail = UserPublicSerializer(read_only=True)
    # records = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    experiment_number = serializers.CharField()
    experiment_date = serializers.DateField()
    sample_name = serializers.CharField()
    powder_comp = serializers.CharField()
    synthesis_method = serializers.CharField()
    polymer = serializers.CharField()
    substrate = serializers.CharField()
    deposition = serializers.CharField()
    nanoparticle_percentage = serializers.IntegerField()
    polymer_percentage =serializers.IntegerField()
    linker_composite = serializers.CharField()
    linker_percentage = serializers.IntegerField()
    geometry = serializers.CharField()
    thickness = serializers.IntegerField()
    comments = serializers.CharField(allow_null=True)



    class Meta:
        model = Experiment
        fields = [
            'user_detail',
            # 'records',
            'user_id',
            'pk',
            'experiment_number',
            'experiment_date',
            'sample_name',
            'powder_comp',
            'synthesis_method',
            'polymer',
            'substrate',
            'deposition',
            'nanoparticle_percentage',
            'polymer_percentage',
            'linker_composite',
            'linker_percentage',
            'geometry',
            'thickness',
            'comments',


        ]

