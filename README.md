# ArrayStream

A real-time random array generator with WebSocket support and MongoDB persistence. This application generates random number arrays and broadcasts them to connected clients in real-time while maintaining a historical record in MongoDB.

## Features

- Real-time random array generation using WebSockets
- Configurable array size (minimum 10,000 elements)
- Customizable number range (default: 0-99999)
- MongoDB persistence for historical data
- REST API endpoints for traditional HTTP requests
- Simple and intuitive web interface
- Docker support for easy deployment

## Tech Stack

- Backend:
  - Flask
  - Flask-SocketIO
  - MongoDB
  - NumPy
- Frontend:
  - HTML5
  - CSS3
  - JavaScript
  - Socket.IO client
- Infrastructure:
  - Docker
  - Docker Compose

## Prerequisites

- Docker and Docker Compose
- Git
- Python 3.9+ (for local development)
- Node.js and npm (optional, for frontend development)

## Quick Start with Docker

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/array-stream.git
   cd array-stream
   ```

2. Start the application using Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Access the application:
   - Web Interface: http://localhost:8080
   - API Endpoint: http://localhost:5000/api
   - MongoDB: localhost:27017

## Local Development Setup

### Backend Setup

1. Create and activate a virtual environment:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set environment variables:
   ```bash
   export FLASK_APP=app/__init__.py
   export FLASK_ENV=development
   export MONGO_URI=mongodb://localhost:27017/array_generator
   ```

4. Run the Flask application:
   ```bash
   flask run
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Serve the frontend files using any HTTP server. For example:
   ```bash
   # Using Python
   python -m http.server 8080
   
   # Or using Node.js http-server
   npx http-server -p 8080
   ```

## API Documentation

### REST Endpoints

#### Generate Array
- **POST** `/api/generate`
  ```json
  {
    "size": 10000,
    "range_start": 0,
    "range_end": 99999
  }
  ```

#### Get Array History
- **GET** `/api/history?limit=10`

### WebSocket Events

#### Client to Server
- `generate_array`: Triggers new array generation
  ```json
  {
    "size": 10000,
    "range_start": 0,
    "range_end": 99999
  }
  ```

#### Server to Client
- `new_array`: Receives newly generated array
  ```json
  {
    "array": [...],
    "size": 10000,
    "range_start": 0,
    "range_end": 99999
  }
  ```

## Deployment

### Server Requirements
- 2+ CPU cores
- 4GB+ RAM
- 20GB+ storage
- Docker and Docker Compose installed
- Open ports: 8080 (frontend), 5000 (backend), 27017 (MongoDB)

### Production Deployment Steps

1. Clone the repository on your server:
   ```bash
   git clone https://github.com/yourusername/array-stream.git
   ```

2. Configure environment variables in `docker-compose.yml` or create a `.env` file

3. Build and start the containers:
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

4. (Optional) Set up a reverse proxy (nginx/apache) for SSL termination

## Monitoring and Maintenance

### Logs
```bash
# View logs for all services
docker-compose logs

# View logs for specific service
docker-compose logs backend
```

### Backup MongoDB Data
```bash
# Backup
docker exec -it arraystream_mongodb_1 mongodump --out /backup/

# Restore
docker exec -it arraystream_mongodb_1 mongorestore /backup/
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
