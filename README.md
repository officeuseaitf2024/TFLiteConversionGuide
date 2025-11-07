Step 1: clone the github repo https://github.com/google-ai-edge/ai-edge-torch
Step 2: install wsl(is using windows OS): You can now install everything you need to run WSL with a single command. Open PowerShell in administrator mode by right-clicking and selecting "Run as administrator", enter the wsl --install command, then restart your machine.
Step 3:launch wsl from wowershell using wsl --cd <path to working directory>:
Step 4:Create a virtual environment and istall as per requirements.txt in the ai_edge_torch
Step 5: place the conversion_to_tflite.py file inside the ai_edge_torch folder
Step 6: modify the conversion_to_tflite.py as per your requirement by placing the name of the HuggingFace Repo that needs to be converted
