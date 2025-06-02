from rest_framework import serializers
from client.models import Profile

# Create your serializers here.
class ProfileModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = [
					'phone_number',
					'profile_picture',
					'location',
					'timestamp',
					'last_modified',
					'verification_status',
					'notification_status',
					'user',
				]
		read_only_fields = fields
