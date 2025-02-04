from rest_framework import serializers
from cards.models import Card, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    # A read-only field means its value is included in the serialized output, but it cannot be
    # modified when creating or updating a Customer object via the API.
    # value for the owner field should come from the email attribute of the related owner object instead of id (user-friendly).
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Card
       # fields = '__all__'
        fields = ['id', 'tasks', 'title', 'description', 'status_text', 'status', 'owner']
        extra_kwargs = {
            'status': {
                'write_only': True
            }
        }

    tasks = TaskSerializer(
        many=True,
        read_only=True
    )
    status_text = serializers.SerializerMethodField()
    def get_status_text(self, instance):
        return (instance.get_status_display())



