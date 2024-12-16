from django.utils import timezone

def current_day(request):
    return {
        'today': timezone.now().date()
    }
