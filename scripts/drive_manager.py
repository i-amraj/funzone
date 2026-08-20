import os
import sys
from huggingface_hub import hf_hub_download, snapshot_download

# Default paths for Google Colab + Mounted Google Drive
DEFAULT_DRIVE_BASE = "/content/drive/MyDrive/Funzone_AI_Studio"
LOCAL_FALLBACK_BASE = os.path.expanduser("~/raj_work_space/funzone/storage")

def get_base_path():
    """Detect if Google Drive is mounted, otherwise fallback to workspace storage."""
    if os.path.exists("/content/drive/MyDrive"):
        return DEFAULT_DRIVE_BASE
    return LOCAL_FALLBACK_BASE

BASE_PATH = get_base_path()
MODELS_DIR = os.path.join(BASE_PATH, "models")
OUTPUTS_DIR = os.path.join(BASE_PATH, "outputs")

CODE_MODEL_DIR = os.path.join(MODELS_DIR, "code")
IMAGE_MODEL_DIR = os.path.join(MODELS_DIR, "image")
VIDEO_MODEL_DIR = os.path.join(MODELS_DIR, "video")

# Model Repositories Configuration
MODEL_CONFIGS = {
    "code": {
        "repo_id": "bartowski/DeepSeek-R1-Distill-Qwen-14B-GGUF",
        "filename": "DeepSeek-R1-Distill-Qwen-14B-Q4_K_M.gguf",
        "save_dir": CODE_MODEL_DIR
    },
    "image": {
        "repo_id": "stabilityai/stable-diffusion-xl-base-1.0",
        "save_dir": IMAGE_MODEL_DIR
    },
    "video": {
        "repo_id": "Lightricks/LTX-Video",
        "save_dir": VIDEO_MODEL_DIR
    }
}

def setup_directories():
    """Ensure all required Google Drive / Storage directories exist."""
    directories = [
        BASE_PATH, MODELS_DIR, OUTPUTS_DIR,
        CODE_MODEL_DIR, IMAGE_MODEL_DIR, VIDEO_MODEL_DIR,
        os.path.join(OUTPUTS_DIR, "code"),
        os.path.join(OUTPUTS_DIR, "image"),
        os.path.join(OUTPUTS_DIR, "video")
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    print(f"✅ Storage Directory Structure Verified at: {BASE_PATH}")

def download_code_model():
    """Download DeepSeek-R1 / Qwen 2.5 Coder GGUF model directly to Drive."""
    cfg = MODEL_CONFIGS["code"]
    target_path = os.path.join(cfg["save_dir"], cfg["filename"])
    if os.path.exists(target_path):
        print(f"🟢 Code Model already exists at: {target_path}")
        return target_path

    print(f"📥 Downloading Code Model ({cfg['filename']}) to Google Drive...")
    os.makedirs(cfg["save_dir"], exist_ok=True)
    file_path = hf_hub_download(
        repo_id=cfg["repo_id"],
        filename=cfg["filename"],
        local_dir=cfg["save_dir"]
    )
    print(f"✅ Code Model downloaded successfully: {file_path}")
    return file_path

def download_image_model():
    """Download FLUX.1-schnell model weights directly to Drive."""
    cfg = MODEL_CONFIGS["image"]
    if os.path.exists(cfg["save_dir"]) and len(os.listdir(cfg["save_dir"])) > 0:
        print(f"🟢 Image Model (FLUX.1) already exists at: {cfg['save_dir']}")
        return cfg["save_dir"]

    print(f"📥 Downloading Image Model (FLUX.1-schnell) to Google Drive...")
    os.makedirs(cfg["save_dir"], exist_ok=True)
    model_dir = snapshot_download(
        repo_id=cfg["repo_id"],
        local_dir=cfg["save_dir"],
        ignore_patterns=["*.pt", "*.bin"]  # prefers safetensors for speed
    )
    print(f"✅ Image Model downloaded successfully: {model_dir}")
    return model_dir

def download_video_model():
    """Download LTX-Video model weights directly to Drive."""
    cfg = MODEL_CONFIGS["video"]
    if os.path.exists(cfg["save_dir"]) and len(os.listdir(cfg["save_dir"])) > 0:
        print(f"🟢 Video Model (LTX-Video) already exists at: {cfg['save_dir']}")
        return cfg["save_dir"]

    print(f"📥 Downloading Video Model (LTX-Video) to Google Drive...")
    os.makedirs(cfg["save_dir"], exist_ok=True)
    model_dir = snapshot_download(
        repo_id=cfg["repo_id"],
        local_dir=cfg["save_dir"]
    )
    print(f"✅ Video Model downloaded successfully: {model_dir}")
    return model_dir

def download_all_models():
    """Download all 3 engines to Google Drive."""
    setup_directories()
    print("🚀 Starting Automated Model Downloader Pipeline...")
    download_code_model()
    download_image_model()
    download_video_model()
    print("🎉 All 3 AI Models are downloaded & verified in Google Drive!")

if __name__ == "__main__":
    download_all_models()
