# ROCHETTE — Watch E-Commerce Platform

A full-stack e-commerce web application for browsing and purchasing watches, built with Django REST Framework on the backend and vanilla JavaScript on the frontend.

## Features

- 🔐 JWT-based user authentication (registration & login)
- 🛒 Shopping cart functionality
- 🔍 Product filtering by category and sorting
- 📄 Contact form
- 📚 API documentation via Swagger
- 🌐 CORS configuration for frontend-backend communication

## Tech Stack

**Backend:** Python, Django, Django REST Framework, Simple JWT  
**Frontend:** JavaScript, HTML, SCSS  
**Database:** SQLite  
**API Docs:** Swagger (drf-yasg)

## Getting Started

1. Clone the repository
```bash
   git clone https://github.com/luka357/rochette-django-ecommerce.git
   cd rochette-django-ecommerce
```

2. Install dependencies
```bash
   pip install -r requirements.txt
```

3. Run migrations
```bash
   python manage.py migrate
```

4. Start the development server
```bash
   python manage.py runserver
```

## Project Structure

- `core/` — Django project settings, DRF, JWT, Swagger, CORS configuration
- `watches/` — Main app: products, categories, filtering, sorting
- `luka/` — User registration, authentication, cart, contact form

## Author

**Luka Julakidze**  
[LinkedIn](https://www.linkedin.com/in/luka-julakidze) · [GitHub](https://github.com/luka357)
