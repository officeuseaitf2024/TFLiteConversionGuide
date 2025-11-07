# Convert Hugging Face Model to TFLite using `ai-edge-torch`

Follow the steps below to set up your environment and convert a Hugging Face model to TFLite format.

---

## 🚀 Steps

### **Step 1: Clone the Repository**
Clone the official [ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) GitHub repository:
```bash
git clone https://github.com/google-ai-edge/ai-edge-torch
cd ai-edge-torch
```

---

### **Step 2: Install WSL (for Windows Users)**
If you're using **Windows**, install the Windows Subsystem for Linux (WSL):

1. Open **PowerShell** as Administrator (right-click → *Run as administrator*).  
2. Run the following command:
   ```bash
   wsl --install
   ```
3. Restart your computer when prompted.

---

### **Step 3: Launch WSL**
Open **PowerShell** and launch WSL, navigating directly to your working directory:
```bash
wsl --cd <path-to-working-directory>
```

> Replace `<path-to-working-directory>` with the path where you cloned the repo.

---

### **Step 4: Set Up a Virtual Environment**
Inside WSL, create and activate a virtual environment, then install the dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### **Step 5: Add the Conversion Script**
Place your `conversion_to_tflite.py` file inside the cloned `ai_edge_torch` folder.

Example structure:
```
ai-edge-torch/
├── ai_edge_torch/
├── conversion_to_tflite.py
├── requirements.txt
└── ...
```

---

### **Step 6: Modify the Script**
Open `conversion_to_tflite.py` and update it with the **Hugging Face model repo name** that you want to convert to TFLite.

Example:
```python
HF_MODEL_REPO = "huggingface-username/model-name"
```

Then, run the conversion script:
```bash
python conversion_to_tflite.py
```

---

✅ **You’re all set!**  
This will convert your Hugging Face model to a TensorFlow Lite format using the `ai-edge-torch` toolkit.
