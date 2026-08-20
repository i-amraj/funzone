import os
import sys

# Import path helper from drive_manager
sys.path.append(os.path.dirname(__file__))
import drive_manager

try:
    from llama_cpp import Llama
    LLAMA_AVAILABLE = True
except ImportError:
    LLAMA_AVAILABLE = False
    print("⚠️ llama-cpp-python not installed locally. Will load on Colab GPU.")

DEFAULT_SYSTEM_PROMPT = """You are an ultra-smart AI Assistant capable of expert coding, complex problem solving, and clear communication in English, Hinglish, and Hindi.
- Always provide clean, efficient, bug-free code snippets with proper comments.
- Speak naturally and conversationally in the user's preferred language (Hinglish/Hindi/English).
- Be concise, direct, and helpful."""

class TextCodeEngine:
    def __init__(self, model_path=None, n_gpu_layers=-1, n_ctx=4096):
        """Initialize and load the Text & Code LLM Model."""
        if model_path is None:
            model_path = os.path.join(
                drive_manager.CODE_MODEL_DIR, 
                drive_manager.MODEL_CONFIGS["code"]["filename"]
            )
        self.model_path = model_path
        self.n_gpu_layers = n_gpu_layers
        self.n_ctx = n_ctx
        self.llm = None

    def load_model(self):
        """Load GGUF model into GPU VRAM."""
        if not LLAMA_AVAILABLE:
            raise RuntimeError("llama-cpp-python package is required to load the model.")

        if not os.path.exists(self.model_path):
            print(f"📥 Model file not found locally. Initiating download to Drive...")
            self.model_path = drive_manager.download_code_model()

        print(f"🚀 Loading Text & Code Model from: {self.model_path}")
        self.llm = Llama(
            model_path=self.model_path,
            n_gpu_layers=self.n_gpu_layers,
            n_ctx=self.n_ctx,
            verbose=False
        )
        print("✅ Text & Code Model loaded into VRAM successfully!")

    def generate(self, prompt, system_prompt=DEFAULT_SYSTEM_PROMPT, max_tokens=2048, temperature=0.7):
        """Generate full response for Text, Code, Hindi, or Hinglish prompts."""
        if self.llm is None:
            self.load_model()

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]

        response = self.llm.create_chat_completion(
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature
        )

        return response["choices"][0]["message"]["content"]

    def generate_stream(self, prompt, system_prompt=DEFAULT_SYSTEM_PROMPT, max_tokens=2048, temperature=0.7):
        """Generate live streaming response (prints word-by-word instantly)."""
        if self.llm is None:
            self.load_model()

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]

        stream = self.llm.create_chat_completion(
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            stream=True
        )

        full_text = ""
        for chunk in stream:
            if "content" in chunk["choices"][0]["delta"]:
                token = chunk["choices"][0]["delta"]["content"]
                full_text += token
                print(token, end="", flush=True)
        return full_text

# Quick Test helper if script is executed directly
if __name__ == "__main__":
    print("🤖 Text, Code & Hinglish Engine Initialized.")
    print("Model Path:", os.path.join(drive_manager.CODE_MODEL_DIR, drive_manager.MODEL_CONFIGS["code"]["filename"]))
