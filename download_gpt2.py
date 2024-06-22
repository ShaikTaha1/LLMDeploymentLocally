from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Choose the model you want to download. Options include: 'gpt2', 'gpt2-medium', 'gpt2-large', 'gpt2-xl'
model_name = 'gpt2'

# Load the tokenizer
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Load the model
model = GPT2LMHeadModel.from_pretrained(model_name)

# Save the model and tokenizer to a local directory
model.save_pretrained('path_to_save_model')
tokenizer.save_pretrained('path_to_save_tokenizer')
