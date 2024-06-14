# Product Management System

## Overview
The Product Management System is a Django-based web application designed for managing products with different user roles: Admin, Store Keeper, and Customer. Each role has specific access levels for performing CRUD operations on products. The application includes API key-based authentication, IP-based authentication, and provides API endpoints for querying product data.

## Features
- User roles with distinct access levels: Admin, Store Keeper, Customer
- CRUD operations on products
- API key-based authentication
- IP-based authentication
- JSON API endpoints for fetching product data

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/product-management-system.git
   python -m venv venv
   cd product-management-system
    python manage.py migrate
   python manage.py runserver

Access the application:
Open your web browser and navigate to http://localhost:8000.

## User Roles and Access Levels
Admin:

Can perform all CRUD operations on products.
Has full access to all features of the system.
Store Keeper:

Can create, read, and update products.
Cannot delete products.
Customer:

Can only read product information.

## Authentication
API Key-Based Authentication
Each user is assigned an API key for authentication.

## IP-Based Authentication
Configure the allowed IP addresses in the settings to restrict access.
Only requests from these IP addresses will be processed.

## API Endpoints
Fetch Product Data
Endpoint: api/
Methods: POST
Description: Fetch product data based on product IDs or product name.

## Contact
For any inquiries or issues, please contact Ridhamariyam44@gmail.com .
