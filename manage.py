#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management import call_command

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dynamic_choices.settings')

    # Auto-create superuser (only runs when AUTO_CREATE_SUPERUSER=true)
    if os.environ.get("AUTO_CREATE_SUPERUSER") == "true":
        try:
            call_command(
                "createsuperuser",
                username=os.environ["DJANGO_SUPERUSER_USERNAME"],
                email=os.environ["DJANGO_SUPERUSER_EMAIL"],
                interactive=False
            )
        except Exception:
            # Superuser already exists OR creation failed silently
            pass

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
