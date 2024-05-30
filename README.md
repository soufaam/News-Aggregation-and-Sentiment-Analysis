 News Aggregation and Sentiment Analysis API

## General Overview
This project provides a backend service for aggregating news articles from various sources and performing sentiment analysis on these articles using Google Cloud Natural Language API. The service includes user authentication to secure access to the API and offers endpoints to fetch general news, top headlines, and user-specific data.

## API Overview

### User Authentication
The API supports user registration, login, and logout functionalities to ensure secure access to the service.

#### Register
- **Endpoint**: `/register`
- **Method**: `POST`
- **Description**: Register a new user.
- **Request Body**:
  ```json
  {
      "username": "your_username",
      "password": "your_password"
  }
- **Response**:
```json
    {
    "msg": "User created successfully."
    }
```
- #### Login
- **Endpoint**: `/login`
- **Method**: `POST`
- **Description**: `Login an existing user`.
- **Request Body**:
```json
    {
    "username": "your_username",
    "password": "your_password"
    }
```
#### Response:
```json
    {
    "access_token": "your_jwt_access_token"
    }
```    
#### Logout
**Endpoint**: `/logout`
**Method**: `DELETE`
**Description**: Logout a logged-in user.
**Request Header**:
**Authorization**: Bearer <your_jwt_access_token>
**Response**:
```json
    {
    "msg": "Successfully logged out."
    }
```
#### News Endpoints
The API provides endpoints to fetch news articles and their sentiment analysis.

**General** News
**Endpoint**: `/news`
**Method**: `GET`, `POST`
**Description**: Fetch general news articles with sentiment analysis.
**Request Header**:
**Authorization**: Bearer <your_jwt_access_token>

#### Response:
```json
    [
    {
        "title": "Article title",
        "description": "Article description",
        "content": "Article content",
        "sentiment_score": -0.1,
        "sentiment_magnitude": 0.1
    },
    ...
    ]   
```
#### Top News
**Endpoint**: `/topnews`
**Method**: `GET`, `POST`
**Description**: Fetch top headlines with sentiment analysis.
**Request Header**:
**Authorization**: Bearer <your_jwt_access_token>
**Response**:
```json
    [
        {
        "title": "Top headline title",
        "description": "Top headline description",
        "content": "Top headline content",
        "sentiment_score": 0.3,
        "sentiment_magnitude": 0.5
    },
    ...
    ]
```
#### Requirements
See requirement file

#### Third-Party Services
***NewsAPI***: Used to fetch news articles from various sources.
***Google Cloud Natural Language API***: Used to perform sentiment analysis on news articles.
***MongoDB***: Used to store news articles and their sentiment analysis results.
#### Setup and Installation
**Clone the repository**:
```bash
git clone https://github.com/your_username/news-aggregation-sentiment-analysis.git
cd news-aggregation-sentiment-analysis
Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:


pip install -r requirements.txt
Set up environment variables:
```
Create a .env file in the root directory with the following content:

```conf
MONGO_URI=your_mongodb_uri
NEWSAPI_KEY=your_newsapi_key
GOOGLE_APPLICATION_CREDENTIALS=path_to_your_google_cloud_credentials_json
JWT_SECRET_KEY=your_jwt_secret_key
...
```
#### Run the application:
```bash
    flask run
```
Access the API:
The API will be accessible at http://127.0.0.1:5000/.
