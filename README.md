# Proyecto Final: Python aplicado a sitios web con Django
Para el proyecto final del curso "Python" en Coderhouse, se plantea el diseño de un sitio web mediante la utilización del framework Django. 

## Finalidad
Diseñar un sitio web orientado a la gestión de un panel de control y administracion para un emprendimiento personal. 
La utilidad del sitio es almacenar una variedad de productos en una base datos, de manera que se pueda estandarizar el proceso de consulta y cotización de proyectos. Además, contar con usuarios para los miembros del equipo, cuyos privilegios se verán asignados según el rol que ocupan en el emprendimiento.

## Objetivos
### Consigna de la pre-entrega
Crear una web en Django, utilizando:
- Herencia de plantillas
- Modelo de, por lo menos, 3 clases
- Un formulario para ingresar datos a cada clase
- Un formulario de búsqueda en la base de datos
### Consigna para la entrega final
Se debe incorporar al sitio las siguientes funcionalidades:
- Login/Auth: Usuarios y permisos
- Mejorar el modelo del sitio, acorde a los requisitos mínimos y obligatorios. Adaptando el ejemplo de un Blog a éste sitio, el modelo estará formado por:
- - Datos básicos: marca y modelo; tipo de producto y descripción
- - Precio
- - Fecha de creación
- - Imagen del producto
- Para crear, editar o borrar los productos y/o imágenes, se debe estar registrado como **Administrador**
- Definir la ruta `/about/` y un acceso visible a ella, en la que se muestre el apartado "Acerca de mí".
- Definir la ruta `/products/` y un acceso visible a ella, en la cual se listen todos los productos de la base de datos con una mínima información, según que clase de producto sea.
- - El título de cada clase de producto será un acceso a la ruta `/products/<product_class>/` para filtrar los productos por clase.
- - Cada producto mostrará una información mínima y tendrá un botón `**Detalles**` que permitirá acceder a todos sus datos en la ruta `/products/<product_class>/<product_id>`
- Si no existe determinada página/sitio, botones que no responden o no existen productos, redireccionar a un sitio que lo indique.


## Implementación
El diseño HTML del cual se produce la herencia en las distintas páginas del sitio se ubica en el directorio `/proyectocoder-django/templates/index.html`, y tiene origen en `https://startbootstrap.com/`.
 
Algunas de las características del proyecto:
- Sitio responsive
- CRUD support mediante 2 mecanismos diferentes: 
- - Vistas basadas en funciones: todas las vistas del CRUD en `views.py` se diseñan en torno a las instrucciones que es necesario ejecutar. Esto requiere utilizar formularios previamente establecidos en `forms.py` 
- - Utilizando las Django Generic Views para cada operación del CRUD:
- - - de `django.views.generic.edit`: CreateView, UpdateView, DeleteView
- - - de `django.views.generic.list`: ListView
- - - de `django.views.generic.detail`: DetailView


![Logo](https://wedomotic.netlify.app/Images/logos/fondo.png)