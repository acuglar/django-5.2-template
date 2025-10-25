from django.http import JsonResponse


def json_error(message, status=400):
    """Retorna resposta JSON padronizada para erros."""
    return JsonResponse({"error": message}, status=status)


def get_client_ip(request):
    """Obtém IP real do cliente, mesmo atrás de proxy."""
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    return x_forwarded_for.split(",")[0] if x_forwarded_for else request.META.get("REMOTE_ADDR")
