from django.shortcuts import render


def error_400(request, exception):
    """View that returns a 400 error template."""

    data = {'exception': exception,
            'error_type': 400,
            'mensaje': '¡Algo ha salido mal!',
            'url_img': None
            }
    return render(request, 'errores/error_response.html', data)


def error_403(request, exception):
    """View that returns a 403 error template."""

    data = {'exception': exception,
            'error_type': 403,
            'mensaje': 'Parece que no puedes acceder a esto, aún... Intenta registrate primero',
            'url_img': None
            }
    return render(request, 'errores/error_response.html', data)


def error_404(request, exception):
    """View that returns a 404 error template."""

    data = {'exception': exception,
            'error_type': 404,
            'mensaje': 'Parece que no teníamos todo lo que buscabas :(',
            'url_img': None
            }
    return render(request, 'errores/error_response.html', data)


def error_500(request):
    """View that returns a 500 error template."""

    data = {'error_type': 500,
            'mensaje': 'Nos estamos tomando un tiempo para resolver las cosas, no te preocupes, no eres tú, somos nosotros',
            'url_img': None
            }
    return render(request, 'errores/error_response.html', data)
