# AI Multimodal Agent

# Youtube Demo Link
Project Introduction: https://youtu.be/qEP2bq18aLM
Project Demo: https://youtu.be/HDCtZQQM1D4

## Overview
I have built an **AI Multimode Agent** that consists of three features:

1. **Text Mode**: Interact with the AI using text.
2. **Voice Mode**: Communicate with the AI through voice commands.
3. **Build Mode**: Get step-by-step guidance to create projects.

## Technologies Used
The project is developed using the following technologies:

- **Python**
  - `streamlit`
  - `speechrecognition`
  - `pyttsx3`
  - `threading`
  - `groq`
  - `lama3.2`

## Installation and Setup
Follow these steps to run the project on your local system:

### 1. Clone the Repository
```bash
git clone <repository_url>
cd ai-multimodal-agent
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Set Up Groq API Key
Obtain a Groq API key and set it as an environment variable:

- **Windows (PowerShell):**
  ```powershell
  $env:GROQ_API_KEY="your_api_key_here"
  ```
- **Mac/Linux:**
  ```bash
  export GROQ_API_KEY="your_api_key_here"
  ```

### 6. Run the Application
```bash
streamlit run app.py
```

## Project Versions
The project has multiple versions:

- **v1.0**: Basic structure.
- **v1.1**: Voice-activated + text-based.
- **v1.2**: Integrated both speech and text.
- **v2.0**: Final version with all features.

## License
This project is open-source and free to use.

---

Feel free to update the repository URL, API key instructions, or any other details based on your specific setup!
