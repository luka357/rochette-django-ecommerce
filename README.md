# ROCHETTE — Watch E-Commerce Platform

A full-stack e-commerce web application for browsing and purchasing watches, built with Django REST Framework on the backend and vanilla JavaScript on the frontend.

## Features

- 🔐 JWT-based user authentication (registration & login)
- 🛒 Shopping cart (stored in the browser with localStorage)
- 🔍 Product filtering by category and sorting by price or name
- 📄 Contact form saved to the database
- 📚 OpenAPI schema and Swagger UI through drf-spectacular
- 🌐 CORS configuration for frontend-backend communication

## Tech Stack

**Backend:** Python, Django, Django REST Framework, Simple JWT, django-filter  
**Frontend:** JavaScript, HTML, SCSS  
**Database:** SQLite  
**API Docs:** drf-spectacular (Swagger UI)

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

3. Create a `.env` file in the project root
```
   DJANGO_SECRET_KEY=your-secret-key-here
```

4. Run migrations
```bash
   python manage.py migrate
```

5. Start the development server
```bash
   python manage.py runserver
```

6. Open the frontend: serve the `luka/` folder (for example with VS Code Live Server) and open `index.html`. The frontend expects the API at `http://127.0.0.1:8000`.

## API Endpoints

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `POST` | `/api/register/` | — | Register a new user |
| `POST` | `/api/token/` | — | Get a JWT access and refresh token pair |
| `POST` | `/api/token/refresh/` | — | Refresh the access token |
| `GET` / `POST` | `/api/watches/` | — | List or create watches (`?category=<id>`, `?ordering=price`) |
| `GET` / `PUT` / `PATCH` / `DELETE` | `/api/watches/<id>/` | JWT | Watch detail, update or delete |
| `GET` / `POST` | `/api/categories/` | — | List or create categories |
| `POST` | `/api/contact/` | — | Send a contact message |
| `GET` | `/api/schema/swagger-ui/` | — | Interactive API docs |

## Project Structure

- `core/` — Django project settings, DRF, JWT, Swagger, CORS configuration
- `watches/` — Main app: watch and category models, contact messages, registration, filtering and sorting
- `luka/` — Frontend (HTML, SCSS, vanilla JS): shop, cart, login and register pages, contact form

## Author

**Luka Julakidze**  
[LinkedIn](https://www.linkedin.com/in/luka-julakidze) · [GitHub](https://github.com/luka357)
