# Game of Life with Wormholes

This is a full-stack implementation of Conway's Game of Life extended with wormholes. Users can upload custom input images and view images after 1, 10, 100, or 1000 iterations.

## 🧩 Features
- Wormhole logic using horizontal and vertical tunnels (color-coded pixel pairs)
- Interactive frontend to upload files and select iterations
- PNG image output after the selected number of iterations
- Fully containerized with Docker and served via Nginx

## 🏗️ Project Structure
```
game-of-life-wormholes/
├── frontend/          # Vite + React frontend
├── backend/           # FastAPI + NumPy backend
├── Dockerfile.frontend
├── Dockerfile.backend
├── docker-compose.yml
└── README.md
```

## 🚀 Quick Start
### 1. Clone the repository
```bash
git clone https://github.com/yourusername/game-of-life-wormholes.git
cd game-of-life-wormholes
```

### 2. Build and run containers
```bash
docker-compose up --build
```

- Frontend: http://localhost
- Backend API: http://localhost/api/generate

## 📂 File Upload Expectations
Upload the following:
- `starting_position.png`: binary image (white=alive, black=dead)
- `horizontal_tunnel.png`: color image with wormhole pairs
- `vertical_tunnel.png`: color image with wormhole pairs

All images must be the same dimensions.

## 📸 Output
Returns a PNG image of the game board after the selected number of iterations (1, 10, 100, or 1000).

## 🧪 Testing Locally
You can test locally outside Docker with:
```bash
cd backend
uvicorn main:app --reload --port 8000
```
And serve the React app:
```bash
cd frontend
npm install
npm run dev
```

## 🛠 Tech Stack
- Frontend: React + Vite + Tailwind CSS
- Backend: FastAPI, NumPy, Pillow
- Server: Nginx
- Containerization: Docker, Docker Compose

## 📄 License
MIT License
