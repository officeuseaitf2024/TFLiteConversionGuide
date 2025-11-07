# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ai-edge-torch", "ai_edge_torch"))

# from ai_edge_torch.generative.examples.gemma3 import gemma3
# from ai_edge_torch.generative.utilities import converter
# from ai_edge_torch.generative.utilities.export_config import ExportConfig
# from ai_edge_torch.generative.layers import kv_cache

# # pytorch_model = gemma3.build_model_270m("PATH_TO_HF_MODEL")

# # If you are using Gemma 3 1B
# pytorch_model = gemma3.build_model_1b("E:/gemma3-270m/gemma-3-1b-it")

# export_config = ExportConfig()
# export_config.kvcache_layout = kv_cache.KV_LAYOUT_TRANSPOSED
# export_config.mask_as_input = True

# converter.convert_to_tflite(
#     pytorch_model,
#     output_path="E:/gemma3-270m/gemma-3-1b-it-tflite",
#     output_name_prefix="my-gemma3",
#     prefill_seq_len=2048,
#     kv_cache_max_len=4096,
#     quantize="dynamic_int8",
#     export_config=export_config,
# )

import torch
import ai_edge_torch
import tensorflow as tf
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

HF_TOKEN = ""

model = AutoModelForSequenceClassification.from_pretrained(
    "AI-ML-Research/wallet-v5_two_class-balanced-two-class-dataset",
    token=HF_TOKEN
)
tokenizer = AutoTokenizer.from_pretrained(
    "AI-ML-Research/wallet-v5_two_class-balanced-two-class-dataset",
    token=HF_TOKEN
)


# Create pipeline (don’t call it yet)
nlp = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Define wrapper
class MyModelWrapper(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m = nlp.model  # or you can use self.m = nlp.model
    def forward(self, input_ids, attention_mask=None):
        outputs = self.m(input_ids=input_ids, attention_mask=attention_mask)
        return outputs.logits

# Example text
text = "London is the capital of England."

# Tokenize to get dummy sample inputs
tokens = tokenizer(text, return_tensors="pt", padding="max_length", max_length=512, truncation=True)
sample_inputs = (tokens["input_ids"], tokens["attention_mask"])

# Convert to TFLite
edge_model = ai_edge_torch.convert(MyModelWrapper().eval(), sample_inputs)
edge_model.export("model_v5.tflite")