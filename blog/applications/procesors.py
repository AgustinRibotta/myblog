from applications.home.models import Home

# Procesor para recuperar telefono y correo 

def home_contac(request):
    home = Home.objects.latest('created')
    
    return {
        'phone': home.phone,
        'correo': home.contac_email
    }