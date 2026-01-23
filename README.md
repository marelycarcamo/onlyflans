# OnlyFlans 🍮

![Python](https://img.shields.io/badge/python-3.10-blue)
![Django](https://img.shields.io/badge/django-4.2-green)
![Bootstrap](https://img.shields.io/badge/bootstrap-5.3.3-purple)
![Font Awesome](https://img.shields.io/badge/font--awesome-6.5.1-lightgrey)
![License](https://img.shields.io/badge/license-MIT-yellow)

![alt text](web\static\img\admin.png)


## 📌 Descripción
**OnlyFlans** es una aplicación web desarrollada en **Django** que simula una plataforma de venta y gestión de postres.  
El proyecto integra autenticación de usuarios, administración de productos y un frontend estilizado con **Bootstrap**, **Font Awesome** y **Google Fonts**.  
Su propósito es servir como proyecto educativo y práctico en el ámbito de la formación laboral y el desarrollo web.

---

## 🚀 Características principales
- **Perfil administrador**  
  - Acceso al **Django Admin** para gestionar productos, usuarios y formularios de contacto.  
  - CRUD completo de productos (crear, editar, eliminar).  
  ![alt text](web\static\img\inicio.png)

- **Gestión de usuarios logueados**  
  - Sistema de login y registro.  
  - Vista personalizada de productos según el usuario autenticado.  

- **Formularios de contacto**  
  - Contacto de clientes (`ContactForm`).  
  - Contacto de empresas (`ContactoEmpresa`).  
  - Ambos administrados desde el panel de administración.  

- **Frontend dinámico**  
  - Uso de **Bootstrap 5.3.3** para diseño responsivo.  
  - Iconografía con **Font Awesome 6.5.1**.  
  - Tipografía personalizada con **Google Fonts (Quicksand)**.  
  - Plantillas Django con bloques `{% block %}` y componentes reutilizables (`header.html`, `navbar.html`, `footer.html`).  

- **Base de datos SQLite3**  
  - Persistencia de usuarios, productos y mensajes.  
  - Migraciones automáticas con `python manage.py migrate`.  

---

## 🛠️ Tecnologías utilizadas
| Tecnología | Versión | Uso |
|------------|---------|-----|
| **Python** | 3.10+ | Backend con Django |
| **Django** | 4.2 | Framework principal |
| **SQLite3** | nativo | Base de datos |
| **Bootstrap** | 5.3.3 | Estilos y diseño responsivo |
| **Font Awesome** | 6.5.1 | Iconografía |
| **Google Fonts (Quicksand)** | última | Tipografía |
| **jQuery** | 3.7.1 | Interactividad en frontend |

---

## 📂 Estructura del proyecto
onlyflans/
│── manage.py          # Script principal de Django 
│── db.sqlite3         # Base de datos
│── web/               # Aplicación principal 
│   ├── models.py      # Definición de modelos (Flan, Cafe, Dulce, ContactForm, ContactoEmpresa) │   ├── views.py       # Vistas y lógica de negocio
│   ├── forms.py       # Formularios de contacto
│   ├── templates/     # Plantillas HTML (header, navbar, footer, etc.) 
│   ├── static/        # Archivos CSS, JS, imágenes 
│── requirements.txt   # Dependencias del proyecto


---

## 🗄️ Modelos de datos (Django ORM)

### **Flan / Cafe / Dulce**
- `uuid`: Identificador único.  
- `name`: Nombre del producto.  
- `description`: Texto descriptivo.  
- `image_url`: URL de imagen (opcional).  
- `slug`: Slug para URL amigables.  
- `js_private`: Booleano para visibilidad privada.  

### **ContactForm**
- `customer_email`: Email del cliente.  
- `customer_name`: Nombre del cliente.  
- `message`: Mensaje enviado.  

### **ContactoEmpresa**
- `name_empresa`: Nombre de la empresa.  
- `email_empresa`: Email de contacto.  
- `phone_empresa`: Teléfono de contacto.  
- `message_empresa`: Mensaje enviado.  

---

## 🌐 Rutas y Endpoints principales

### Catálogo y productos
- `/` → **index**: lista de flanes públicos.  
- `/coffee/` → **coffee**: lista de cafés.  
- `/delicias/` → **delicias**: lista de dulces.  
- `/welcome/` → **welcome** *(requiere login)*: lista de flanes privados.  

### Información
- `/about/` → **about**: página informativa.  

### Contacto
- `/contacto/` → **contacto**: formulario de clientes.  
- `/contacto_success/` → **contacto_success**: confirmación de envío.  
- `/contacto_empresa/` → **contacto_empresa**: formulario de empresas.  

### Autenticación
- `/login/` → **login**: redirige al login de Django.  
- `/logout/` → **logout**: página de despedida.  

### Redes sociales
- `/facebook/`, `/twitter/`, `/instagram/`: redirecciones a perfiles oficiales.  

---

## ⚙️ Instalación y ejecución
1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/marelycarcamo/onlyflans.git
   cd onlyflans
   ```

2. **Crear entorno virtual**
	```bash
	python -m venv venv
	source venv/bin/activate   # Linux/Mac
	venv\Scripts\activate      # Windows
	```

3. **Instalación de dependencias**
	```bash
	pip install -r requirements.txt
	```

4. **Ejecutar migraciones**
	```bash
	python manage.py migrate
	```

5. **Levantar servidor**
	```bash
	python manage.py runserver
	```

6. **Acceder al navegador**
	```bash
	http://127.0.0.1:8000/
	```

---

## 📖 Uso
- Registrarse o iniciar sesión.
- Explorar catálogo de flanes, cafés y dulces.
- Administrar productos desde el panel de administración.
- Enviar consultas mediante los formularios de contacto.

---

## 🧪 Testing
Ejecutar pruebas con:
	```bash
	python manage.py test
	```
---

## 📌 Roadmap / Futuras mejoras
- Implementar carrito de compras.
- Integrar pasarela de pago.
- Internacionalización (i18n).
- API REST para integraciones externas.
- Despliegue en plataformas como Heroku o Railway.

---

## 🤝 Contribución
1. 	Haz un fork del repositorio.
2. 	Crea una rama para tu feature ().
3. 	Realiza tus cambios y haz commit ().
4. 	Haz push a la rama ().
5. 	Abre un Pull Request.

---

## 📜 Licencia
Este proyecto está bajo la licencia MIT.

---

## 👩‍💻 Autor
Proyecto desarrollado por Marely Cárcamo como práctica de desarrollo web y metodologías de formación laboral.

---


