from transformers import (
    GPT2LMHeadModel,
    GPT2TokenizerFast,
    DataCollatorForLanguageModeling,
    Trainer,
    TrainingArguments
)
from datasets import load_dataset

dataset = load_dataset(
    "text",
    data_files={"train": "football.txt", "validation": "football.txt"}
)

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

def tokenize(batch):
    return tokenizer(batch["text"], truncation=True, max_length=256)

tokenized = dataset.map(tokenize, batched=True, remove_columns=["text"])

model = GPT2LMHeadModel.from_pretrained("gpt2")

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

args = TrainingArguments(
    output_dir="./finetuned-football-model",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=2,
    save_steps=200,
    logging_steps=50,
    eval_strategy="epoch"
)

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized["train"],
    eval_dataset=tokenized["validation"],
    data_collator=data_collator
)

trainer.train()

trainer.save_model("./finetuned-football-model")
tokenizer.save_pretrained("./finetuned-football-model")
