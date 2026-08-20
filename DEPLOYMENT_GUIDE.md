# 🚀 DEPLOYMENT GUIDE: Launching Your AI Studio on Google Colab & 5TB Drive

Follow these exact 3 simple steps to launch your **Smart Text, Coding & Hinglish AI Studio** for FREE with zero local PC strain!

---

## 📍 STEP 1: Upload Project Files to Google Drive (1 Minute)

1. Open your browser and go to your **5TB Google Drive**: [drive.google.com](https://drive.google.com)
2. Click **+ New** ➔ **New folder**, and name it: `Funzone_AI_Studio`
3. Open the `Funzone_AI_Studio` folder in Google Drive.
4. Upload these two items from your local computer (`/home/ubuntu_16gb/raj_work_space/funzone`):
   - 📄 `notebooks/ai_studio_master.ipynb`
   - 📁 `scripts/` (Folder containing `drive_manager.py` and `code_engine.py`)

---

## 📍 STEP 2: Open Master Notebook in Google Colab

1. In Google Drive, **Right-Click** on `ai_studio_master.ipynb`.
2. Select **Open with** ➔ **Google Colaboratory**.
3. In the top menu of Google Colab, go to:
   - **Runtime** ➔ **Change runtime type**
   - Select **T4 GPU** (or **A100 GPU** if using Colab Pro)
   - Click **Save**.

---

## 📍 STEP 3: Click "Run All" (Automatic Execution)

1. Press `Ctrl + F9` or click **Runtime** ➔ **Run all** in Colab.
2. In **Cell 2**, a Google Authorization pop-up will appear:
   - Click **"Connect to Google Drive"**.
   - Select your 5TB Google Account.
3. Sit back and watch! Google Colab will automatically:
   - ✅ Mount your 5TB Google Drive.
   - ✅ Auto-download `DeepSeek-R1-14B` / `Qwen-2.5` model to Drive (~40 sec).
   - ✅ Load the model into GPU VRAM.
   - ✅ Generate a **Public Web UI & API Link** for your mobile & browser!

---

## 🔄 AUTOMATIC LIVE CODE SYNC (0 Manual Work)

Every time Antigravity AI updates any script or adds a feature, it automatically pushes to:
👉 **[https://github.com/i-amraj/funzone](https://github.com/i-amraj/funzone)**

In Google Colab, simply run this 1-line cell to pull the latest code directly into your 5TB Google Drive:

```bash
!cd /content/drive/MyDrive/Funzone_AI_Studio/funzone && git pull
```

