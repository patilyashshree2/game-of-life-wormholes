from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
from fastapi.staticfiles import StaticFiles
from services.simulation_service import SimulationService
from utils.file_utils import save_image
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return "<h2>Game of Life backend is live!</h2><a href='/docs'>API Docs</a>"


# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["https://game-of-life-wormholes-frontend.onrender.com"],
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create temporary output directory
os.makedirs("temp", exist_ok=True)
# Mount the /temp URL to serve files from ./temp
app.mount("/temp", StaticFiles(directory="temp"), name="temp")


@app.post("/api/generate")
async def generate(
    starting_position: UploadFile = File(...),
    horizontal_tunnel: UploadFile = File(...),
    vertical_tunnel: UploadFile = File(...)
):
    try:
        # Run simulation and get iteration results
        service = SimulationService()
        results = await service.run_all_iterations(
            starting_position, horizontal_tunnel, vertical_tunnel,
            iterations=[1, 10, 100, 1000]
        )

        # Save each result as image
        output = {}
        for i, result_array in results.items():
            filename = f"temp/{i}.png"
            save_image(result_array, filename)
            output[str(i)] = filename

        return JSONResponse(output)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})