#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import os
import sys
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pneumonia_website.settings")
    
    # Get the PORT from the environment variable provided by Render
    port = os.environ.get('PORT', '8000')
    
    # Start the Django development server with the correct host and port
    execute_from_command_line([sys.argv[0], 'runserver', f'0.0.0.0:{port}'])

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pneumonia_website.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
