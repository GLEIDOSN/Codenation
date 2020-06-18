from api.models import Event

event = Event.objects.get(level="CRITICAL")
