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

## Teck Stack

- Backend
  - Flask
  - Flask-SocketIO
  - MongoDB
  - NumPy

- Frontend
  - HTML5
  - CSS3
  - JavaScript
  - Socket.IO client

- Infrastructure
  - Docker
  - Docker Compose


## Prerequisites

- Docker and Docker Compose
- Git
- Python 3.12+ (for local development)
- Node.js and npm (optional, for frontend development)

## Quick Start with Docker


