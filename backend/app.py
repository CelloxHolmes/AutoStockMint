from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# สำหรับให้ Electron เรียกข้าม origin ได้
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AutoStockMint Backend is running ✅"}

@app.post("/generate_prompt")
def generate_prompt():
    return {"message": "ยังไม่เชื่อม GPT"}

@app.post("/generate_image")
def generate_image():
    return {"message": "ยังไม่เชื่อม Discord bot"}

@app.post("/add_metadata")
def add_metadata():
    return {"message": "ยังไม่เชื่อม AI keyword"}

@app.post("/upload")
def upload():
    return {"message": "ยังไม่เชื่อม Adobe Stock"}
