# Neuro-Vision-AI

## Overview
**Neuro Vision AI** is an advanced deep learning-based system designed for **brain tumor detection** using **MRI-scanned images in JPG format**. This project leverages state-of-the-art **Computer Vision and 3D Visualization** techniques to not only detect tumors but also provide a **Brain Chop 3D demo**, offering a comprehensive visualization of the **entire skull and brain**.

## Features
- **Brain Tumor Detection**: Uses deep learning models to accurately identify tumors from MRI scans.
- **3D Brain Visualization**: Generates an interactive 3D demo of the skull and brain using **Brain Chop technology**.
- **High Accuracy & Efficiency**: Implements CNN-based models for precise tumor classification.
- **Scalability & Robustness**: Supports diverse MRI scan datasets and handles various input resolutions.
- **User-Friendly Interface**: Provides an intuitive dashboard for doctors and researchers.

## Technologies Used
- **CNN (Convolutional Neural Networks)** – For tumor classification.
- **OpenCV & TensorFlow/Keras** – For image processing and deep learning.
- **Matplotlib & Seaborn** – For visualization and exploratory data analysis.
- **VTK (Visualization Toolkit)** – For 3D modeling and rendering of the skull and brain.
- **Streamlit** – For interactive UI development.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Meghana230211/Neuro-Vision-AI.git
   cd NeuroVisionAI
   ```
2. Create a virtual environment:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   streamlit run app.py
   ```

## Usage
1. Upload **MRI scan images (JPG format)**.
2. The system detects and classifies tumors.
3. View a **3D demo of the brain and skull**.
4. Analyze tumor size, location, and growth rate.

## Future Enhancements
- **Real-time MRI Scan Processing**
- **Integration with Medical Databases**
- **Enhanced 3D Reconstruction with AI-driven Insights**

## Contributors
- **Meghana M**
- **Syed Anis Al Rehaman**

For any inquiries or contributions, feel free to submit a pull request or open an issue.

