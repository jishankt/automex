from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import CompanyInfo, TeamMember, ContactSubmission
from .forms import ContactForm
from clients.models import Client

def home(request):
    company_info = CompanyInfo.objects.first()
    team_members = TeamMember.objects.filter(is_active=True)[:4]
    clients = Client.objects.filter(is_active=True)
    
    context = {
        'company_info': company_info,
        'team_members': team_members,
        'clients': clients,
    }
    return render(request, 'home.html', context)

def about(request):
    company_info = CompanyInfo.objects.first()
    team_members = TeamMember.objects.filter(is_active=True)
    
    context = {
        'company_info': company_info,
        'team_members': team_members,
    }
    return render(request, 'about.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save contact submission
            submission = ContactSubmission.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                company=form.cleaned_data['company'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            
            # Send email notification to admin
            try:
                company_info = CompanyInfo.objects.first()
                admin_email = company_info.email if company_info else 'automextechnoogies@gmail.com'
                
                send_mail(
                    f'New Contact Form Submission: {submission.subject}',
                    f'''
                    Name: {submission.name}
                    Email: {submission.email}
                    Phone: {submission.phone}
                    Company: {submission.company}
                    
                    Message:
                    {submission.message}
                    
                    Submitted at: {submission.submitted_at}
                    ''',
                    settings.DEFAULT_FROM_EMAIL,
                    [admin_email],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Failed to send admin email: {e}")
            
            # Send thank you email to client
            try:
                company_name = company_info.name if company_info else "AutoMex"
                company_email = company_info.email if company_info else "automextechnoogies@gmail.com"
                
                send_mail(
                    f'Thank You for Contacting {company_name}',
                    f'''
                    Dear {submission.name},
                    
                    Thank you for reaching out to {company_name}! We have received your message and appreciate you taking the time to contact us.
                    
                    Here's a summary of your inquiry:
                    Subject: {submission.subject}
                    
                    Our team will review your message and get back to you within 24 hours during business days.
                    
                    In the meantime, feel free to explore our services and portfolio on our website.
                    
                    Best regards,
                    {company_name} Team
                    {company_email}
                    Calicut, Palayam
                    
                    ---
                    This is an automated response. Please do not reply to this email.
                    ''',
                    settings.DEFAULT_FROM_EMAIL,
                    [submission.email],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Failed to send thank you email: {e}")
            
            messages.success(request, 'Thank you for your message! We have sent a confirmation email to your inbox.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    company_info = CompanyInfo.objects.first()
    
    context = {
        'form': form,
        'company_info': company_info,
    }
    return render(request, 'contact.html', context)