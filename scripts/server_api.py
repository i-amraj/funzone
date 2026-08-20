import os
import sys
import gradio as gr

# Ensure scripts directory is in sys.path
sys.path.append(os.path.dirname(__file__))

from code_engine import TextCodeEngine

print("🚀 Initializing Unified AI Studio Server...")

# Load Engine
code_engine = TextCodeEngine()

def user_respond(user_message, history):
    """Process prompt and update chatbot history."""
    if history is None:
        history = []
    if not user_message or not user_message.strip():
        return "", history
    try:
        response = code_engine.generate(user_message)
        history.append({"role": "user", "content": user_message})
        history.append({"role": "assistant", "content": response})
    except Exception as e:
        history.append({"role": "user", "content": user_message})
        history.append({"role": "assistant", "content": f"⚠️ Error: {str(e)}"})
    return "", history

# Custom CSS for Premium Modern Aesthetics
custom_css = """
body {
    background-color: #0b0f19;
    font-family: 'Inter', sans-serif;
    color: #e2e8f0;
}
.gradio-container {
    max-width: 1200px !important;
    margin: auto !important;
}
#header-banner {
    text-align: center;
    background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%);
    padding: 24px;
    border-radius: 16px;
    margin-bottom: 20px;
    box-shadow: 0 10px 25px -5px rgba(67, 56, 202, 0.4);
}
#header-banner h1 {
    color: #ffffff;
    font-weight: 800;
    font-size: 2.2rem;
    margin-bottom: 8px;
}
#header-banner p {
    color: #c7d2fe;
    font-size: 1rem;
}
"""

def create_studio_ui():
    """Build the unified multi-modal studio Gradio web interface."""
    with gr.Blocks(title="Funzone Unified AI Studio") as demo:
        with gr.Column(elem_id="header-banner"):
            gr.Markdown("""
            # 🚀 Funzone Multi-Modal AI Studio
            ### Powered by 5TB Google Drive & Cloud GPU • Text, Code, Image & Video AI Engine
            """)

        with gr.Tabs():
            # TAB 1: Smart Text & Code AI (Hindi / Hinglish / English)
            with gr.TabItem("💬 Text & Code Assistant"):
                gr.Markdown("### 🤖 DeepSeek-R1 / Qwen Smart Multilingual AI")
                chatbot = gr.Chatbot(label="AI Conversation", height=450, type="messages")
                with gr.Row():
                    msg_input = gr.Textbox(
                        placeholder="Poocho code, text, or query (Hindi, Hinglish, English)...",
                        lines=2,
                        scale=8,
                        show_label=False
                    )
                    send_btn = gr.Button("🚀 Send Message", variant="primary", scale=2)
                
                clear_btn = gr.Button("🗑️ Clear Chat History", size="sm")

                # Event handlers for Submit (Enter key) and Click Send Button
                msg_input.submit(user_respond, [msg_input, chatbot], [msg_input, chatbot])
                send_btn.click(user_respond, [msg_input, chatbot], [msg_input, chatbot])
                clear_btn.click(lambda: [], None, chatbot, queue=False)

            # TAB 2: AI Image Generator (FLUX.1 / SDXL)
            with gr.TabItem("🎨 Image Generator"):
                gr.Markdown("### 🖼️ High-Quality Photorealistic Image Generation")
                with gr.Row():
                    with gr.Column():
                        img_prompt = gr.Textbox(label="Image Prompt", placeholder="A futuristic cyberpunk city at night with neon lights...", lines=3)
                        img_btn = gr.Button("🎨 Generate Image", variant="primary")
                    with gr.Column():
                        img_output = gr.Image(label="Generated Output Image")

            # TAB 3: AI Video Generator
            with gr.TabItem("🎬 Video Generator"):
                gr.Markdown("### 📹 HD AI Video Generation Engine")
                with gr.Row():
                    with gr.Column():
                        vid_prompt = gr.Textbox(label="Video Prompt", placeholder="A cinematic drone shot of a misty mountain peak...", lines=3)
                        vid_btn = gr.Button("🎬 Generate Video", variant="primary")
                    with gr.Column():
                        vid_output = gr.Video(label="Generated Output Video")

    return demo

if __name__ == "__main__":
    demo = create_studio_ui()
    print("\n🌐 Launching Unified Web Studio Server with Public URL...")
    demo.queue().launch(share=True, show_error=True)
