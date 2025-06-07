import model_loader
import pipeline
from PIL import Image
from transformers import CLIPTokenizer
import torch
import gradio as gr

# Device setup
DEVICE = "cpu"
ALLOW_CUDA = True
ALLOW_MPS = False

if torch.cuda.is_available() and ALLOW_CUDA:
    DEVICE = "cuda"
elif (hasattr(torch, "has_mps") and torch.has_mps) or torch.backends.mps.is_available() and ALLOW_MPS:
    DEVICE = "mps"
print(f"🖥️ Using device: {DEVICE}")

# Load tokenizer and model
tokenizer = CLIPTokenizer("../data/vocab.json", merges_file="../data/merges.txt")
model_file = "../data/v1-5-pruned-emaonly.ckpt"
models = model_loader.preload_models_from_standard_weights(model_file, DEVICE)

# ---------- Image Generation Function ----------
def generate_image(prompt, cfg_scale=8, sampler="ddpm", steps=40, strength=0.9):
    uncond_prompt = ""
    do_cfg = True
    input_image = None  # Optional image input
    seed = 42

    output_image = pipeline.generate(
        prompt=prompt,
        uncond_prompt=uncond_prompt,
        input_image=input_image,
        strength=strength,
        do_cfg=do_cfg,
        cfg_scale=cfg_scale,
        sampler_name=sampler,
        n_inference_steps=steps,
        seed=seed,
        models=models,
        device=DEVICE,
        idle_device="cpu",
        tokenizer=tokenizer,
    )
    return Image.fromarray(output_image)

# ---------- Placeholder Functions ----------
def coming_soon(*args, **kwargs):
    return "🚧 Feature coming soon! Stay tuned."

# ---------- UI Setup ----------
with gr.Blocks(title="SynthiVerse.AI") as demo:
    gr.Markdown(
        """
        <h1 style='text-align: center;'>🧠 SynthiVerse.AI</h1>
        <h3 style='text-align: center;'>Text-to-Image • Text-to-Audio • Text-to-Video</h3>
        <p style='text-align: center;'>Explore multimodal generative creativity. Only Text-to-Image is currently available. Audio and Video support coming soon!</p>
        <hr>
        """
    )

    with gr.Tab("🎨 Text to Image"):
        with gr.Row():
            with gr.Column():
                prompt = gr.Textbox(label="Prompt", placeholder="e.g. a dragon flying through a neon cyberpunk city")
                cfg = gr.Slider(1, 14, value=8, step=1, label="CFG Scale")
                sampler = gr.Radio(choices=["ddpm", "plms"], value="ddpm", label="Sampler")
                steps = gr.Slider(10, 100, value=40, step=5, label="Sampling Steps")
                strength = gr.Slider(0.1, 1.0, value=0.9, step=0.1, label="Image Strength")
                generate_btn = gr.Button("Generate Image")

            with gr.Column():
                output_image = gr.Image(type="pil", label="Generated Image", interactive=False)

        generate_btn.click(fn=generate_image, inputs=[prompt, cfg, sampler, steps, strength], outputs=output_image)

    with gr.Tab("🔊 Text to Audio"):
        gr.Markdown("🚧 **Coming soon!** Text-to-Audio synthesis is under development.")

    with gr.Tab("🎥 Text to Video"):
        gr.Markdown("🚧 **Coming soon!** Text-to-Video synthesis is under development.")

    gr.Markdown("<hr><p style='text-align: center;'>© 2025 SynthiVerse.AI • All rights reserved.</p>")

# ---------- Launch ----------
demo.launch()
