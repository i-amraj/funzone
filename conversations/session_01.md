# Session 01: All-in-One Free AI Studio Setup (Coding + Image + Video + Automation)

**Date & Time:** 2026-08-20 18:12 IST  
**Workspace:** `/home/ubuntu_16gb/raj_work_space/funzone`  
**GitHub Repository:** `https://github.com/i-amraj/funzone` (Branch: `main`)

---

## 🎯 Project Objective
Build a 100% Free, Automated 3-in-1 AI Engine powered by Google Colab GPU + 5TB Google Drive storage for persistent model management and remote web access.

### Core Capabilities:
1. 💻 **Code Generation & Chat:** DeepSeek-R1-14B / Qwen 2.5 (Hindi, Hinglish, English support)
2. 🎨 **Image Generation:** FLUX.1 / SDXL (HD Photorealistic Image Gen)
3. 🎬 **Video Generation:** LTX-Video / CogVideoX (Prompt to MP4 Video Clip)
4. ⚙️ **Automation API & Web UI:** Public web access via Gradio HTTPS link anywhere on Mobile/PC

---

## 📋 Step-by-Step Execution Plan & Status

- [x] **Step 0: Create `plan.md` (Single Source of Truth Blueprint)** *(Completed)*
- [x] **Step 1: Setup Conversation Logging & Folder Structure** *(Completed)*
- [x] **Step 2: Create Master Colab Notebook (`notebooks/ai_studio_master.ipynb`)** *(Completed)*
- [x] **Step 3: Setup Google Drive Storage & Model Downloader (`scripts/drive_manager.py`)** *(Completed)*
  - 📥 **DeepSeek-R1-Distill-Qwen-14B (8.99 GB GGUF model)** downloaded 100% successfully into 5TB Google Drive!
- [x] **Step 4: Implement Text, Code & Hinglish LLM Engine (`scripts/code_engine.py`)** *(Completed)*
  - Added CUDA GPU VRAM loading & Live Streaming (`generate_stream`).
- [x] **Step 4.5: Deployment Guide (`DEPLOYMENT_GUIDE.md`)** *(Completed)*
- [x] **Step 5: GitHub Live Code Auto-Sync Integration** *(Completed)*
  - Repository linked: `https://github.com/i-amraj/funzone.git`
  - Automated 1-line sync in Colab: `!cd /content/drive/MyDrive/Funzone_AI_Studio/funzone && git pull origin main`
- [x] **Step 6: Build Unified Web App UI Server (`scripts/server_api.py`)** *(Completed)*
  - Custom modern dark UI with Tabbed Chatbot, Image Generator, and Video Generator.
  - Live Public HTTPS Gradio Link generation (`share=True`).

---

## 💬 Decision & Milestone Log

1. **Architecture:** Zero local PC hardware strain. 100% GPU processing on Google Colab, persistent 9GB+ model storage on 5TB Google Drive.
2. **Multilingual AI:** System prompt fine-tuned for expert Python coding, Hindi, and Hinglish natural language understanding.
3. **Automated Live Sync:** Connected local workspace to GitHub (`i-amraj/funzone`) so any code modification made by AI assistant automatically pushes and syncs to Google Drive with zero manual file uploads.
4. **Unified Web Studio:** Built `scripts/server_api.py` so the user can interact via a clean web app URL on phone or PC without interacting with code cells.

---

## 🚀 How to Launch Studio Anytime (1-Line Command):

Run this single cell in Google Colab:

```bash
!cd /content/drive/MyDrive/Funzone_AI_Studio/funzone && git pull origin main && python scripts/server_api.py
```
