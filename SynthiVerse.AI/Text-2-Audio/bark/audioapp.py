import os
import gradio as gr
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

os.environ["SUNO_OFFLOAD_CPU"] = "True"
os.environ["SUNO_USE_SMALL_MODELS"] = "True"

# Preload models once at startup
preload_models()

def get_next_filename(base_dir=".", prefix="output", ext=".wav"):
    existing_files = [f for f in os.listdir(base_dir) if f.startswith(prefix) and f.endswith(ext)]
    indices = []
    for f in existing_files:
        try:
            num = int(f[len(prefix)+1:-len(ext)])  # output_1.wav -> 1
            indices.append(num)
        except ValueError:
            pass
    next_index = max(indices) + 1 if indices else 1
    return os.path.join(base_dir, f"{prefix}_{next_index}{ext}")

def text_to_audio(text):
    if not text.strip():
        return None, "Please enter some text!"
    
    audio_array = generate_audio(text)
    filename = get_next_filename()
    write_wav(filename, SAMPLE_RATE, audio_array)
    
    # Return the audio file path to play and confirmation message
    return filename, f"Audio saved as {filename}"

with gr.Blocks(title="Text-to-Audio") as demo:
    gr.Markdown("# 🎤 Text to Audio")
    
    text_input = gr.Textbox(label="Enter text here", lines=4, placeholder="Type something...")
    audio_output = gr.Audio(label="Generated Audio", type="filepath")
    status = gr.Textbox(label="Status", interactive=False)

    generate_btn = gr.Button("Generate Audio")
    generate_btn.click(fn=text_to_audio, inputs=text_input, outputs=[audio_output, status])

if __name__ == "__main__":
    demo.launch()
