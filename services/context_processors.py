from .models import Service

def services_processor(request):
    services = Service.objects.filter(is_active=True).order_by('order')[:6]
    return {
        'services': services,
    }