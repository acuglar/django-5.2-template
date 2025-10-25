from django.conf import settings


def global_context(request):
    """
    Injeta variáveis globais disponíveis em todos os templates.
    """
    return {
        # Config related
        'DEBUG': settings.DEBUG,
        'LANGUAGE_CODE': settings.LANGUAGE_CODE,

        # Request related
        'CURRENT_PATH': request.path,
        'CLIENT_IP': request.META.get('REMOTE_ADDR', 'unknown'),
        'IS_AUTHENTICATED': request.user.is_authenticated,
        'USERNAME': request.user.username if request.user.is_authenticated else 'Guest',
        'USER_ID': request.user.id if request.user.is_authenticated else None,
        'USER_ROLE': request.user.groups.first().name if request.user.is_authenticated and request.user.groups.exists() else 'Anonymous',
        'IS_STAFF': request.user.is_staff if request.user.is_authenticated else False,
        'IS_SUPERUSER': request.user.is_superuser if request.user.is_authenticated else False,
        'QUERY_PARAMS': request.GET.dict(),

        # Client related
        'USER_AGENT': request.META.get('HTTP_USER_AGENT', 'unknown'),
        'REFERRER': request.META.get('HTTP_REFERER', 'unknown'),
        'HOST': request.META.get('HTTP_HOST', 'unknown'),
        'STATIC_URL': settings.STATIC_URL,
        'MEDIA_URL': settings.MEDIA_URL,

        'SESSION_ID': request.session.session_key,
    }
