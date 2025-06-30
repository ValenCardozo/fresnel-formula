# Calculadora de Zona de Fresnel

Aplicación web desarrollada en Django para calcular la altura máxima de la Zona de Fresnel entre dos puntos según la distancia y frecuencia.

## Descripción

Esta aplicación permite realizar cálculos de altura máxima utilizando la fórmula de Fresnel: 
```
Altura máxima (m) = 8.656 * √(distancia (km) / frecuencia (MHz))
```

La Zona de Fresnel es crucial para el diseño y planificación de enlaces de comunicación inalámbrica, asegurando una transmisión óptima de señales.

## Requisitos

- Python 3.8 o superior
- Django 4.2 o superior
- Navegador web moderno con soporte para JavaScript y Local Storage

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/tuusuario/fresnel-formula.git
cd fresnel-formula
```

2. Crea un entorno virtual (opcional pero recomendado):
```bash
# En macOS/Linux
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install django
```

## Configuración

1. Aplica las migraciones de la base de datos:
```bash
cd calculate_with_fresnel
python manage.py migrate
```

2. Crea un superusuario (opcional):
```bash
python manage.py createsuperuser
```

## Ejecución

Para iniciar el servidor de desarrollo:

```bash
cd calculate_with_fresnel
python manage.py runserver
```

La aplicación estará disponible en: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Características

- Cálculo de altura máxima de la Zona de Fresnel
- Almacenamiento de historial de cálculos en el navegador (Local Storage)
- Explicación detallada de la importancia y usos de la Zona de Fresnel
- Interfaz responsiva adaptada a diferentes dispositivos

## Estructura del proyecto

- `app/views.py`: Contiene la lógica para los cálculos de la Zona de Fresnel
- `app/templates/`: Plantillas HTML para la interfaz de usuario
- `app/urls.py`: Configuración de las rutas URL
