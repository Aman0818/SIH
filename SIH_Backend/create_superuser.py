from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username='<your-username>').exists():
    User.objects.create_superuser('<your-username>', '<your-email>', '<your-password>')
