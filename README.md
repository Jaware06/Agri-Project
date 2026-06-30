# KisanSetu
Website made for Farmers.


# KisanSetu

## Overview

KisanSetu is a web-based agricultural information platform designed to assist farmers by providing crop details, disease information, fertilizer recommendations, market prices, and modern farming techniques in one place. The system helps farmers make informed decisions using a simple and user-friendly web interface.

---

## Features

- User registration and login system
- Crop information and recommendations
- Plant disease details and symptoms
- Fertilizer recommendations
- Agricultural market price tracking
- Modern farming techniques and guidance
- MongoDB database integration

---

## Tech Stack

### Backend
- Python
- Flask
- PyMongo
- Python Dotenv

### Frontend
- HTML
- CSS
- JavaScript
- Jinja2 Templates

### Database
- MongoDB Atlas

---

## Project Structure

```text
KisanSetu/
│
├── app.py
├── crop.py
├── disease.py
├── fertilizer.py
├── market.py
├── farming.py
├── requirements.txt
├── .env
├── templates/
├── static/
└── README.md
```

---

## Installation and Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd KisanSetu
```

---

### 2. Create virtual environment
```bash
python -m venv venv
```

---

### 3. Activate virtual environment

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```env
MONGO_URI=your_mongodb_connection_string
DB_NAME=kisansetu
SECRET_KEY=your_secret_key
```

---

## MongoDB Setup

1. Create a free cluster in MongoDB Atlas  
2. Create a database user with username and password  
3. Allow IP access (0.0.0.0/0 for development)  
4. Copy connection string and add it to `.env`

---

## Run the Project

```bash
python app.py
```

Then open in browser:

```
http://127.0.0.1:5000
```

---

## Database Collections

- users
- crops
- diseases
- fertilizers
- market_prices
- farming_techniques

---

## Future Improvements

- AI-based crop recommendation system
- Weather forecasting integration
- Multi-language support
- Mobile application version
- Government scheme information system
- Real-time market API integration

---

## Developer
  
B.Tech Computer Engineering Student

This project is developed to support digital agriculture and help farmers access important agricultural information easily.