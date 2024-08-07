import requests
from django.shortcuts import render, redirect
from django.urls import reverse
from reservas.models import Reserva

# Configura tus credenciales
WEBPAY_API_KEY = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"
WEBPAY_COMMERCE_CODE = "597055555532"
WEBPAY_ENV = 'TEST'

# Endpoints de la API de Webpay
WEBPAY_BASE_URL = 'https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions' if WEBPAY_ENV == 'TEST' else 'https://webpay3g.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions'

def iniciar_pago(request, reserva_id):
    if request.method == 'POST':
        try:
            reserva = Reserva.objects.get(pk=reserva_id)

            buy_order = "ordenCompra12345678"  # Debe ser único por transacción
            session_id = "sesion1234557545"  # Debe ser único por sesión
            amount = reserva.monto  # Monto de la transacción
            return_url = request.build_absolute_uri(reverse('confirmar_pago'))  # URL absoluta correcta

            headers = {
                'Tbk-Api-Key-Id': WEBPAY_COMMERCE_CODE,
                'Tbk-Api-Key-Secret': WEBPAY_API_KEY,
                'Content-Type': 'application/json',
            }

            data = {
                "buy_order": buy_order,
                "session_id": session_id,
                "amount": amount,
                "return_url": return_url
            }

            response = requests.post(WEBPAY_BASE_URL, headers=headers, json=data)
            response_data = response.json()

            if response.status_code == 200:
                return redirect(response_data['url'] + '?token_ws=' + response_data['token'])
            else:
                return render(request, 'error.html', {'message': response_data.get('error_message', 'Error al iniciar la transacción'), 'reserva_id': reserva_id})
        except Reserva.DoesNotExist:
            return render(request, 'error.html', {'message': 'Reserva no encontrada', 'reserva_id': reserva_id})
        except Exception as e:
            return render(request, 'error.html', {'message': str(e), 'reserva_id': reserva_id})
    else:
        return render(request, 'pago.html', {'reserva_id': reserva_id})

def confirmar_pago(request):
    token = request.GET.get('token_ws')

    if not token:
        return render(request, 'error.html', {'message': 'Token no recibido.', 'reserva_id': request.GET.get('reserva_id', '')})

    headers = {
        'Tbk-Api-Key-Id': WEBPAY_COMMERCE_CODE,
        'Tbk-Api-Key-Secret': WEBPAY_API_KEY,
        'Content-Type': 'application/json',
    }

    response = requests.put(f"{WEBPAY_BASE_URL}/{token}", headers=headers)
    response_data = response.json()

    reserva_id = request.GET.get('reserva_id', '')

    if response.status_code == 200 and response_data.get('status') == 'AUTHORIZED':
        return render(request, 'exito.html', {'response': response_data, 'reserva_id': reserva_id})
    else:
        return render(request, 'error.html', {'message': response_data.get('error_message', 'Error al confirmar la transacción'), 'reserva_id': reserva_id})
