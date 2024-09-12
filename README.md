# CULTURAMA

**Proyecto Integrador - Prácticas Profesionales 4**  
**Tecnatura en Desarrollo de Software**  
**IFTS N°18, Capital Federal**  
**Autores: Ivana Ebri y Maria Laura Fiege Fava**

## Descripción

CULTURAMA es un proyecto integrador desarrollado para la materia Prácticas Profesionales 4, correspondiente a la Tecnicatura en Desarrollo de Software del IFTS N°18 de Capital Federal. El proyecto fue realizado en grupo por Ivana Ebri y Maria Laura Fiege Fava, y tiene como objetivo aplicar los conocimientos adquiridos durante la carrera en un entorno real de desarrollo de software.

El proyecto está diseñado para abarcar varias etapas del ciclo de vida del software, desde la planificación y el análisis de requisitos, hasta el diseño, desarrollo, pruebas e implementación de una aplicación web. A lo largo de su desarrollo, se busca fomentar el trabajo colaborativo, la aplicación de buenas prácticas de programación, la utilización de herramientas de control de versiones y la integración continua.

## Descripción General

CULTURAMA es una aplicación web desarrollada en Python utilizando Django, diseñada para ofrecer recorridos de interés cultural a los usuarios. El proyecto está orientado a dos tipos de usuarios: administradores y usuarios finales. 

- **Administrador**: Interfaz centrada en el uso en desktop para gestionar puntos de interés y monitorear estadísticas.
- **Usuario final**: Interfaz optimizada para dispositivos móviles, enfocada en proporcionar una experiencia de usuario atractiva y fácil de usar.

## Funcionalidades Principales

1. **Login y Registro de Usuarios**  
   - Formulario de registro e inicio de sesión.
   - Gestión de sesiones para mantener la autenticación de los usuarios.

2. **Selección de Temática y Preferencias**  
   - Los usuarios pueden elegir una temática cultural de su interés (arte, historia, arquitectura, gastronomía, etc.).
   - Posibilidad de seleccionar el número de paradas en el recorrido y otras preferencias (tipo de lugar, distancia máxima, etc.).

3. **Recomendaciones de Puntos de Interés**  
   - Algoritmo que sugiere puntos de interés basados en la temática seleccionada y otras preferencias del usuario.
   - Integración con APIs de mapas para calcular distancias y ordenar los puntos de interés.

4. **Generación de Recorridos**  
   - Presentación de un recorrido sugerido con un mapa interactivo que muestra los puntos de interés seleccionados.
   - Información detallada de cada punto de interés (descripción, horarios, fotos, etc.).

5. **Feedback y Mejora de Recomendaciones**  
   - Los usuarios pueden dejar comentarios y valoraciones sobre los recorridos.
   - El sistema aprende de las valoraciones y preferencias para mejorar futuras recomendaciones.

6. **Panel de Administración**  
   - Gestión y actualización de la base de datos de puntos de interés.
   - CRUD (Crear, Leer, Actualizar, Eliminar) para puntos de interés.
   - Monitoreo de estadísticas de uso y popularidad de los recorridos.
   - Gestión de sugerencias de nuevos sitios de interés proporcionadas por los usuarios.

## Tecnologías Utilizadas

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript (con enfoque mobile-first)
- **Base de Datos**: MariaDB
- **APIs**: Integración con APIs de mapas para generación de recorridos

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/usuario/culturama.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd culturama
    ```

3. Crea un entorno virtual e instálalo:

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

4. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

5. Realiza las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

6. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

7. Accede a la aplicación en tu navegador web:

    ```
    http://127.0.0.1:8000
    ```

## Contribución

1. Haz un fork del proyecto.
2. Crea una rama para tu nueva funcionalidad (`git checkout -b nueva-funcionalidad`).
3. Realiza los cambios necesarios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Empuja tus cambios al repositorio (`git push origin nueva-funcionalidad`).
5. Crea un Pull Request.

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).
