from django.shortcuts import render
from django.views import View

import math

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class CalculateView(View):
    """
    Vista para realizar cálculos de altura máxima utilizando la fórmula de Fresnel
    """

    def get(self, request):
        return render(request, 'calculate.html', {
            'title': 'Calculo de zona de Fresnel',
            'result': None
        })

    def post(self, request):
        try:
            # Obtenemos los valores del formulario
            distance = float(request.POST.get('distance', 0))  # en km
            frequency = float(request.POST.get('frequency', 0))  # en MHz

            if distance <= 0 or frequency <= 0:
                raise ValueError("La distancia y la frecuencia deben ser valores positivos")

            # Cálculo de la altura máxima según la fórmula proporcionada
            max_height = 8.656 * math.sqrt(distance / frequency)

            # Truncar a 2 decimales sin redondear
            truncated_height = math.trunc(max_height * 100) / 100
            result = {
                'max_height': truncated_height,
                'distance': distance,
                'frequency': frequency,
                'message': 'Cálculo realizado con éxito'
            }

        except (ValueError, ZeroDivisionError) as e:
            result = {'error': f"Error en el cálculo: {str(e)}"}

        return render(request, 'calculate.html', {
            'title': 'Calculo de zona de Fresnel',
            'result': result
        })
