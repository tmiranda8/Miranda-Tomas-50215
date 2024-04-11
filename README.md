# Proyecto Final: Python aplicado a sitios web con Django
Para el proyecto final del curso "Python" en Coderhouse se plantea el desarrollo de un sitio web con el framework Django. 

## We Domotic CRM
La propuesta es desarrollar un sitio web orientado a la gestión de proyectos mediante un panel de control y administracion de datos, basados en la lógica de sistemas CRM (Customer Relationship Management).

Las funcionalidades del sitio giran en torno gestionar listas de productos y clientes en una base datos. 
El objetivo es simplificar el proceso de consulta y cotización de proyectos para los miembros del equipo, que tendrán usuarios estándar.

El proceso de carga y/o edición estará limitada a usuarios con privilegios, que deben ser creados únicamente con superuser.

## Objetivos
El objetivo de la entrega y sus requisitos estan orientados al desarrollo de un sitio web estilo blog, incluyendo admin, perfiles, registro, publicaciones y formularios. 
Los requisitos base serán parte de los criterios de evaluación para aprobar el proyecto, en caso de querer cambiar de blog a otra temática.
### Requisitos base
- Video explicativo de 10 min máximo.
- Herencia de templates.
- `.gitignore` 
- `requirements.txt`
- Vistas:
    - Inicio/homepage
    - Acerca de mi/about
    - Listado de objetos del modelo principal. Cada objeto mostrará solo algunos de sus datos y mediante botones permite acceder a detalles.
        - Detalle de determinado objeto
        - Editar determinado objeto.
        - Crear objeto
        - Eliminar objeto
    - Autenticación:
        - Login
        - Logout
        - Sign up
        - Profile
        - Edit profile
        - Reset password
- Modelo principal (mínimo):
    - 2 Charfield
    - 1 Richtext
    - 1 Imagefield
    - 1 Datefield
- Características mínimas:
    - 2 vistas class-based.
    - Registrar todos los modelos en el Django admin.
    - App para el manejo de usuario/autenticación
    - Un mixin `LoginRequiredMixin` y un decorador `@login_required`
    - Datos de usuario que deben visualizarse en Profile
        - Nombre y Apellido
        - Email
        - Usuario
        - Avatar
        - Biografia/link/fecha de cumpleaños/etc
    - App de mensajería con todo lo necesario para que los usuarios puedan comunicarse entre sí por mensajes.

### Implementación
La herencia HTML se aloja en `./templates/index.html`. El diseño esta basado en la lógica del siguiente proyecto: `https://startbootstrap.github.io/startbootstrap-sb-admin-2/index.html`.

![Logo](https://wedomotic.netlify.app/Images/logos/fondo.png)