from django.db import models
import string
import random

# Generate a unique room code
def generate_unique_code():
    length = 6
    while True:
        code = "".join(random.choices(string.ascii_uppercase, k=length))  # Generate random ASCII code
        # Check that the generated code is unique
        if Room.objects.filter(code=code).count() == 0:
            break
    return code


# Sample model
class Room(models.Model):
    # Unique room code
    code = models.CharField(max_length=8, default="", unique=True)
    # Room host (can only host 1 room)
    host = models.CharField(max_length=50, unique=True)
    # Permission for guest to pause, required input
    guest_can_pause = models.BooleanField(null=False, default=False)
    # Votes required to skip a song
    votes_to_skip = models.IntegerField(null=False, default=1)
    # Date created (automatically created)
    created_at = models.DateTimeField(auto_now_add=True)

