#📘 Fine-Tuning GPT-2 Using LoRA (Low-Rank Adaptation)

This project demonstrates how to fine-tune a GPT-2 language model using LoRA (Low-Rank Adaptation) — a lightweight technique that trains only a small percentage of model parameters while keeping the full model frozen.

LoRA makes training faster, cheaper, and more accessible, even on limited hardware like Google Colab.

#🚀 Project Overview

In this example, I fine-tuned GPT-2 on a small custom dataset (football.txt) using the PEFT (Parameter-Efficient Fine-Tuning) library.
The goal was to learn how LoRA works and apply it to a real dataset.
```bash
📂 Project Structure
├── football.txt          # Training data
├── lora_fine_tuning.ipynb # Notebook with training code
└── Lora_football/        # Saved LoRA checkpoint
```
#🧠 Key Concepts Learned
##✔️ What is LoRA?

A method to fine-tune large language models by training only rank-decomposed matrices inside attention layers.

##✔️ Why LoRA?

Reduces trainable parameters by 99%+

Faster training

Lower GPU/VRAM usage

Works with small datasets

##✔️ How LoRA is applied in GPT-2

Only the attention layers (c_attn) are updated while the base model stays frozen.

#🛠️ Tech Stack

Python

HuggingFace Transformers

PEFT (LoRA)

Datasets

Google Colab GPU

#🔧 Installation
```bash
pip install transformers datasets peft accelerate
```
#📘 Training Code (Core Section)
🔹 Load Dataset
```bash
from datasets import load_dataset
datasets = load_dataset("text", data_files="football.txt")
```
🔹 Load Tokenizer & Model
```bash
from transformers import GPT2Tokenizer, GPT2LMHeadModel
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token
```
🔹 Apply LoRA
```bash
from peft import LoraConfig, get_peft_model

lora_config = LoraConfig(
    r=8,
    lora_alpha=64,
    target_modules=["c_attn"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

peft_model = get_peft_model(model, lora_config)
peft_model.print_trainable_parameters()
```
🔹 Train the Model
```bash
from transformers import TrainingArguments, Trainer

training_args = TrainingArguments(
    output_dir="./Lora_football",
    num_train_epochs=5,
    per_device_train_batch_size=4,
    save_steps=500,
)

trainer = Trainer(
    model=peft_model,
    args=training_args,
    train_dataset=tokenized_dataset["train"]
)

trainer.train()
```
📤 Saving the LoRA Model
```bash
peft_model.save_pretrained("./Lora_football")
```
🔍 Generating Text
```bash
from transformers import pipeline
generator = pipeline("text-generation", model="./Lora_football", tokenizer=tokenizer)

print(generator("When was the world cup", max_length=100, do_sample=True)[0]['generated_text'])
``
#📈 Results

Even with a tiny dataset, the LoRA model adapted and produced football-related completions.
More data = better results, but this was a perfect hands-on introduction to LoRA fine-tuning.

#🎯 What I Learned

How GPT-2 tokenization, attention layers, and LM training work

How LoRA reduces training cost

How to build a custom dataset for language modeling

How to train and evaluate a PEFT model

#⭐ Future Improvements

Use a larger football dataset

Evaluate model using perplexity

Convert LoRA + GPT-2 into a chatbot

Push the model to HuggingFace Hub

#🙌 Acknowledgements

Thanks to HuggingFace for providing open-source tools that make model fine-tuning accessible to everyone.
