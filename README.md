# AYUSH Vatika - Tree Information System

A Django REST API backend for the AYUSH Vatika project, developed for Smart India Hackathon (SIH). This system provides comprehensive information about medicinal trees and plants used in traditional Indian medicine systems (Ayurveda, Yoga & Naturopathy, Unani, Siddha and Homoeopathy).

## 🌿 Project Overview

AYUSH Vatika is a digital platform that catalogs medicinal trees and plants, providing detailed information about their botanical properties, medicinal uses, and regional availability. Users can explore, bookmark, and take notes on various trees for educational and research purposes.

## ✨ Features

- **Tree Database**: Comprehensive catalog of medicinal trees with botanical and common names
- **Detailed Information**: Habitat, region, type, and medicinal use information for each tree
- **Media Support**: Image and video content for better understanding
- **User Management**: Custom user authentication with JWT tokens
- **Bookmarking System**: Users can bookmark trees for quick access
- **Notes System**: Personal note-taking functionality for each tree
- **Location Tracking**: User coordinate storage for location-based features
- **Admin Dashboard**: Comprehensive admin interface for content management

## 🛠️ Technology Stack

- **Backend Framework**: Django 5.0.6
- **API Framework**: Django REST Framework 3.15.1
- **Authentication**: JWT (Simple JWT)
- **Database**: PostgreSQL (with dj-database-url)
- **File Storage**: AWS S3 (django-storages)
- **Image Processing**: Pillow
- **CORS Handling**: django-cors-headers
- **Static Files**: WhiteNoise
- **Deployment**: Gunicorn

## 📁 Project Structure

```
SIH_Backend/
├── SIH_Backend/          # Main project configuration
│   ├── settings.py       # Django settings
│   ├── urls.py          # Main URL configuration
│   ├── wsgi.py          # WSGI configuration
│   └── asgi.py          # ASGI configuration
├── users/               # User management app
│   ├── models.py        # Custom user model
│   ├── views.py         # User API views
│   ├── serializers.py   # User serializers
│   └── urls.py          # User URL patterns
├── trees/               # Tree information app
│   ├── models.py        # Tree model
│   ├── views.py         # Tree API views
│   ├── serializers.py   # Tree serializers
│   └── urls.py          # Tree URL patterns
├── notes/               # Notes management app
│   ├── models.py        # Note model
│   ├── views.py         # Notes API views
│   ├── serializers.py   # Notes serializers
│   └── urls.py          # Notes URL patterns
├── utils/               # Utility functions
│   └── utils.py         # Helper utilities
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL
- AWS S3 bucket (for media storage)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd SIH
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=postgresql://username:password@localhost:5432/database_name
   AWS_ACCESS_KEY_ID=your-aws-access-key
   AWS_SECRET_ACCESS_KEY=your-aws-secret-key
   ```

5. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/`

## 📚 API Endpoints

### Authentication
- `POST /users/register/` - User registration
- `POST /users/login/` - User login
- `POST /users/token/refresh/` - Refresh JWT token

### Trees
- `GET /trees/` - List all trees
- `GET /trees/{id}/` - Get specific tree details
- `POST /trees/` - Create new tree (admin only)
- `PUT /trees/{id}/` - Update tree (admin only)
- `DELETE /trees/{id}/` - Delete tree (admin only)

### Notes
- `GET /notes/` - List user's notes
- `POST /notes/` - Create new note
- `PUT /notes/{id}/` - Update note
- `DELETE /notes/{id}/` - Delete note

### User Management
- `GET /users/profile/` - Get user profile
- `PUT /users/profile/` - Update user profile
- `POST /users/bookmark/` - Bookmark/unbookmark tree

## 🔧 Configuration

### Database Configuration
The project uses PostgreSQL as the primary database. Configure the `DATABASE_URL` in your environment variables.

### AWS S3 Configuration
Media files (images and videos) are stored in AWS S3. Configure the following:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- Bucket name: `ayushvatika`
- Region: `ap-south-1`

### JWT Configuration
- Access token lifetime: 10 minutes
- Refresh token lifetime: 1 day
- Automatic token rotation enabled

## 🌍 Deployment

The application is configured for production deployment with:
- WhiteNoise for static file serving
- Gunicorn as WSGI server
- PostgreSQL database
- AWS S3 for media storage
- CORS enabled for frontend integration

### Environment Variables for Production
```env
SECRET_KEY=your-production-secret-key
DATABASE_URL=your-production-database-url
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
DEBUG=False
```

## 👥 Team

**HackMonks Team** - Smart India Hackathon 2024

## 📄 License

This project is developed for Smart India Hackathon 2024.


## 📞 Support

For support and queries, please contact the HackMonks team.

---

**Note**: This project is part of Smart India Hackathon 2024 and focuses on promoting traditional Indian medicine systems through digital innovation.