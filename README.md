# AutoStockMint 🪙

AI-powered automation system that generates stock images (via Midjourney), tags them, and uploads to Adobe Stock — fully hands-free.

## Features
- Prompt generation with ChatGPT
- Midjourney image generation (workaround or manual sync)
- Metadata tagging and AI keywording
- Automatic Adobe Stock upload
- GUI interface for workflow control

## Tech Stack
- Python + OpenAI API
- Midjourney (via Discord workaround)
- Adobe Stock Contributor
- Optional: n8n, ffmpeg, Whisper

## Setup
1. Copy `.env.example` to `.env` and fill in your API keys and credentials.
##How to run 

(venv) C:\Users\MasterIT\Downloads\AutoStockMint\backend>uvicorn app:app --relo BE
(venv) PS C:\Users\MasterIT\Downloads\AutoStockMint\frontend> npm start FE
