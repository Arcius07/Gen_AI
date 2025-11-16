🏆 GPT-2 Pretraining on Custom Football Dataset

This project demonstrates how to pre-train a GPT-2 style language model from scratch using a custom dataset (football.txt).
It covers dataset loading, tokenization, training, saving, and text generation — providing a complete minimal pretraining pipeline using Hugging Face Transformers.

🚀 Project Overview

Large Language Models like GPT-2 go through two major phases:

1️⃣ Pre-Training

The model learns:

Grammar

Vocabulary

Sentence structure

General world knowledge

During this phase, the model is trained in an unsupervised manner on large amounts of raw text.

2️⃣ Fine-Tuning (Optional)

The pre-trained model is later adapted for specific tasks like:

Question answering

Chatbots

Summarization

Classification

This repo focuses fully on pre-training.

📂 Dataset

The dataset is a simple text file:

/content/football.txt


You can replace it with any .txt dataset to train on your own domain.

🛠️ Tech Stack

Python

Hugging Face Transformers

Datasets

Accelerate

PyTorch

📌 Installation

Install dependencies:

pip install datasets transformers tokenizers accelerate

📄 Code Workflow
1. Load Dataset
from datasets import load_dataset
data = load_dataset('text', data_files='/content/football.txt')

2. Tokenize
from transformers import GPT2TokenizerFast
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

3. Prepare Model Config
from transformers import GPT2Config
config = GPT2Config(
    vocab_size=tokenizer.vocab_size,
    bos_token_id=tokenizer.bos_token_id,
    eos_token_id=tokenizer.eos_token_id,
    n_layer=6,
    n_head=6,
    n_embd=384
)

4. Train
from transformers import Trainer, TrainingArguments
training_args = TrainingArguments(
    output_dir="./gpt2-football",
    num_train_epochs=50,
    per_device_train_batch_size=4,
    learning_rate=5e-6
)

5. Generate Text
from transformers import pipeline
prompt = "Which team have the most world cups"
text_generator = pipeline("text-generation", model="./gpt2-football")
print(text_generator(prompt)[0]["generated_text"])

🧠 Model Details

6 Transformer layers

6 attention heads

384 embedding dimension

Trained for 50 epochs

Custom domain-specific dataset (football)

This setup is lightweight and ideal for educational purposes.

🎯 Results

After training, the model is capable of generating domain-specific football-related text:

“Which team have the most world cups… generated continuation here”

📦 Saving the Model
new_model.save_pretrained("./gpt2-football")
tokenizer.save_pretrained("./gpt2-football")


You can now reuse the model locally or push it to Hugging Face Hub.
