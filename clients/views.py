from django.shortcuts import render
from django.http import HttpResponse
import os
from .models import Client, Testimonial

def client_list(request):
    clients = Client.objects.filter(is_active=True).order_by('order')
    testimonials = Testimonial.objects.filter(is_approved=True, is_featured=True)
    
    context = {
        'clients': clients,
        'testimonials': testimonials,
    }
    return render(request, 'clients/client_list.html', context)

def debug_clients(request):
    """Debug view to check client logos"""
    clients = Client.objects.filter(is_active=True)
    output = []
    
    output.append("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Client Logo Debug</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            img { max-width: 200px; border: 2px solid red; margin: 10px; }
            .error { color: red; font-weight: bold; }
            .success { color: green; font-weight: bold; }
            .client { border: 1px solid #ccc; padding: 15px; margin: 10px 0; }
            .file-info { background: #f5f5f5; padding: 10px; margin: 5px 0; }
        </style>
    </head>
    <body>
        <h1>Client Logo Debug</h1>
    """)
    
    for client in clients:
        output.append(f"<div class='client'>")
        output.append(f"<h2>{client.name}</h2>")
        
        if client.logo:
            output.append(f"<div class='file-info'>")
            output.append(f"<p><strong>Logo field:</strong> {client.logo}</p>")
            output.append(f"<p><strong>Logo URL:</strong> {client.logo.url}</p>")
            output.append(f"<p><strong>File path:</strong> {client.logo.path}</p>")
            
            if os.path.exists(client.logo.path):
                file_size = os.path.getsize(client.logo.path)
                output.append(f'<p class="success">✓ File exists on disk ({file_size} bytes)</p>')
                output.append(f'<img src="{client.logo.url}" alt="{client.name}">')
            else:
                output.append(f'<p class="error">✗ File NOT FOUND on disk!</p>')
                # Check if file exists with different case
                directory = os.path.dirname(client.logo.path)
                if os.path.exists(directory):
                    files = os.listdir(directory)
                    output.append(f"<p>Files in directory: {', '.join(files)}</p>")
            output.append("</div>")
        else:
            output.append("<p class='error'>No logo assigned to this client</p>")
        
        output.append("</div><hr>")
    
    output.append("</body></html>")
    return HttpResponse(''.join(output))