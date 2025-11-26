from .models import CompanyInfo

def company_info(request):
    company_info = CompanyInfo.objects.first()
    return {
        'company_info': company_info,
    }