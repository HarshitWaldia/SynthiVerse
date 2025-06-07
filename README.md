# 🧠 SynthiVerse.AI

**A Multimodal Generative AI System — Bringing together text-to-image, text-to-audio, and text-to-video generation in one powerful interface.**

[![Made with Gradio](https://img.shields.io/badge/Made%20with-Gradio-orange)](https://gradio.app/)
[![Python Version](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![SynthiVerse Banner](assets/banner.png)

## 🚀 Overview

**SynthiVerse.AI** is a creative synthesis platform powered by state-of-the-art generative models. This project aims to democratize access to multimodal AI tools by combining them into a single, easy-to-use application.

It provides a unified Gradio interface for users to generate:

-   🎨 **Images** from text prompts using a from-scratch implementation of Stable Diffusion.
-   🔊 **Audio** from text prompts using Suno's Bark model.
-   🎥 **Video** from text prompts (coming soon!).

### How It Works: The Stable Diffusion Core

The text-to-image module is a from-scratch implementation of Stable Diffusion v1.5. This approach breaks down the model into its core components for educational and experimental purposes:

1.  **CLIP Text Encoder**: Converts the input text prompt into a numerical representation (embedding).
2.  **Variational Autoencoder (VAE)**: Encodes images into a compressed latent space and decodes latents back into images.
3.  **U-Net Denoising Model**: The heart of the diffusion process, which iteratively removes noise from a latent representation, guided by the text embedding.
4.  **Scheduler**: Manages the noise schedule and timesteps during the denoising process.

The code is heavily commented to explain each step, making it an ideal resource for learning.

This project aims to democratize access to multimodal AI tools by combining them into a single, easy-to-use application.

## 🛠️ Key Features

-   ✔️ **Intuitive Interface**: A clean, multi-tab Gradio UI for seamless navigation between generation modes.
-   ✔️ **Text-to-Image**: Generate high-quality images with configurable parameters like CFG scale, samplers, steps, and seed.
-   ✔️ **Text-to-Audio**: Create realistic speech, music, and sound effects from text using pre-trained Bark models.
-   🚧 **Text-to-Video**: A placeholder tab is included, ready for future integration of a video synthesis model.
-   🖥️ **Smart Device Selection**: Automatically detects and utilizes the best available device (`CUDA`, `MPS`, or `CPU`).
-   📦 **Modular Codebase**: The project is structured with clear separation of concerns (models, pipelines, UI), making it easy to extend and maintain.

---

## 📸 Sample Output

| Text Prompt                               | Generated Image                          |
| :---------------------------------------- | :--------------------------------------- |
| `a cyberpunk astronaut walking on Mars`   | ![Example Image](assets/sample_image.webp) |
| `a monkey playing with a balloon`         | ![Example Image](assets/output.png)       |

---
## ✨ Application in Action

Here’s a look at the SynthiVerse.AI interface and the results it can produce.

### 🎨 Text-to-Image Generation

The interface provides full control over the image generation process, including steps, guidance scale, seed, and sampler.

**Interface Screenshot:**
**Prompt:** `A  cyberpunk astronaut walking on Mars`

![Text-to-Image UI](assets/IMG2.png)

### 🔊 Text-to-Audio Generation

The audio tab uses the Bark model to generate speech, music, and sound effects from a single text prompt.

**Interface Screenshot:**
**Prompt:** `"Hello and welcome to SynthiVerse.AI — your gateway to AI-generated creativity."
"The future of artificial intelligence is not just smart, it's imaginative."
"In 2050, humans and machines will collaborate to create entirely new worlds."`

![Text-to-Audio UI](assets/IMG4.png)

**Result:**

https://github.com/user-attachments/assets/8f1273b2-4495-4e08-abc9-0c1afd03f16e



---

## 📁 Project Structure

```text
SynthiVerse.AI/
├──Documentation
├──References
├── assets/
│   └── sample_image.png
│  └── output.png
├── Text-2-Image/
│   ├── stable_diffusion/
│   │   ├── model_loader.py
│   │   └── Setup1.py
│   │   └── pipeline.py
│   └── data/
│       ├── vocab.json
│       └── model.ckpt 
│       └── merges.txt
├── Text-2-Audio/
│   └── bark/
│       └──audioapp.py
│       └── ...
│
├── requirements.txt    # Project dependencies
└── README.md
```

---

## ⚙️ Setup and Installation

Follow these steps to get SynthiVerse.AI running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SynthiVerse.AI.git
cd SynthiVerse.AI
```

### 2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage dependencies.

**Using `conda`:**
```bash
conda create -n synthiverse python=3.10
conda activate synthiverse
```
**Or using `venv`:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### 3. Install Dependencies

Install all the required Python packages using pip.
```bash
pip install -r requirements.txt
```

### 4. Download Model Weights

-   **Stable Diffusion**: Download the required `.ckpt` or `.safetensors` model file and place it in the `Text-2-Image/data/` directory.
-   **Bark**: No manual download needed. The required models will be downloaded automatically by the library on the first run and cached.

### 5. Run the Application

Launch the Gradio interface by running the main setup script.
```bash
cd SynthiVerse.AI/Text-2-Image/Stable_diffusion/python Setup1.py
cd SynthiVerse.AI/Text-2-Audio/bark/python audioapp.py
```
Open your web browser and navigate to the local URL provided in the terminal (e.g., `http://127.0.0.1:7860`).

---

## 📝 To-Do List

-   [ ] Integrate a Text-to-Video synthesis module.
-   [ ] Add Image-to-Image and Inpainting support in the Image tab.
-   [ ] Implement custom voice cloning and multilingual support in the Audio tab (Bark).
-   [ ] Add support for more image samplers and upscaling models.
-   [ ] Deploy a live demo on Hugging Face Spaces or Streamlit Cloud.

## 📄 License

This project is intended for educational and demonstration purposes. It utilizes open-source models that are subject to their own licenses (e.g., CreativeML Open RAIL-M for Stable Diffusion). Always check the original model licenses before using them for commercial purposes.

This repository's code is licensed under the [MIT License](LICENSE).

## ✨ Acknowledgements and Credits

This project stands on the shoulders of giants. A huge thanks to the teams, individuals, and contributors who made this possible.

### Core Technologies
-   **Stable Diffusion**: [CompVis](https://github.com/CompVis/stable-diffusion), Runway, and Stability AI.
-   **Bark Model**: [Suno AI](https://github.com/suno-ai/bark).
-   **UI Framework**: [Gradio](https://gradio.app/) by Hugging Face.

### Educational Resources & Code References
-   **Umar Jamil**: For the excellent [YouTube tutorial](https://youtu.be/ZBKpAp_6TGI?si=87XErzq_P5K6Yj_d) on coding Stable Diffusion from scratch.
-   **Hugging Face Diffusers**: [huggingface/diffusers](https://github.com/huggingface/diffusers/) for reference implementations.
-   **Divam Gupta's TF Implementation**: [divamgupta/stable-diffusion-tensorflow](https://github.com/divamgupta/stable-diffusion-tensorflow).
-   **Kjsman's PyTorch Implementation**: [kjsman/stable-diffusion-pytorch](https://github.com/kjsman/stable-diffusion-pytorch).

### Contributors
-   A special thanks to **Shivam Sah** for integrating the Text-to-Audio functionality.
    -   **LinkedIn**: [Shivam Sah](https://www.linkedin.com/in/shivam-sah-a56b85239/)

## 🙌 How to Contribute

Contributions are welcome! If you have suggestions for improvements or want to add new features, please follow these steps:

1.  Fork the repository.
2.  Create a new feature branch (`git checkout -b feature/YourAmazingFeature`).
3.  Commit your changes (`git commit -m 'Add YourAmazingFeature'`).
4.  Push to the branch (`git push origin feature/YourAmazingFeature`).
5.  Open a Pull Request.

Please open an issue first to discuss any major changes you would like to make.

## 📬 Contact

**Harshit Waldia**

-   **Email**: `harshitwaldia112@gmail.com`
-   **LinkedIn**: [linkedin.com/in/harshit-waldia](https://www.linkedin.com/in/harshit-waldia/)
-   **GitHub**: [@HarshitWaldia](https://github.com/HarshitWaldia)

<br>
<p align="center">
  🧠 “SynthiVerse — where your words shape creativity.” 🧠
</p>
