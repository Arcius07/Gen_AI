# 📘 GPT-2 Fine-Tuning — Football Dataset

This project demonstrates how to fine-tune GPT-2 on a custom text dataset using Hugging Face Transformers.

The model is trained on football.txt, a curated list of football facts including game rules, famous players, and major tournaments.
```
📂 Project Structure
├── finetune.py          # Main training script
├── football.txt         # Dataset (general football facts)
└── README.md            # Documentation
```
# 🧠 Dataset Details

The dataset football.txt contains short descriptive lines about:

Core Rules: objectives, field, match duration, team structure

Key Players: Messi, Ronaldo, legendary football icons

Major Competitions: FIFA World Cup, UEFA Champions League

Gameplay Elements: tactics, formations, VAR, goalkeeping

# 📦 Installation
```
1️⃣ Create a virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

2️⃣ Install dependencies
pip install transformers datasets torch
```

# ▶️ Running the Fine-Tuner
```
Make sure football.txt is in the same directory as finetune.py.

Run:

python finetune.py
```

The fine-tuned model will be saved to:
```
./finetuned-football-model
```
# ✨ Using the Trained Model
```
Create a new file (run_model.py) or use a notebook:

from transformers import GPT2LMHeadModel, GPT2TokenizerFast

model = GPT2LMHeadModel.from_pretrained("./finetuned-football-model")
tokenizer = GPT2TokenizerFast.from_pretrained("./finetuned-football-model")

prompt = "The FIFA World Cup is"
inputs = tokenizer(prompt, return_tensors="pt")

output = model.generate(
    inputs["input_ids"],
    max_length=50,
    do_sample=True,
    temperature=0.7,
    top_k=50
)

print("-" * 20)
print(tokenizer.decode(output[0], skip_special_tokens=True))
print("-" * 20)
```
# 🎯 Why This Project?

Minimal Code: Uses Hugging Face Trainer API for simplicity

Custom Data: Demonstrates local .txt dataset loading

Beginner-Friendly: Perfect introduction to LLM fine-tuning

Reusable: You can swap in any dataset (sports, tech, books, etc.)

# 💡 Optional Tip for Better Results

Since football.txt is very small (≈15 lines):

num_train_epochs = 10


gives better learning than the default 3 epochs.
