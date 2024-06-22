from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the tokenizer and model from the local directory
tokenizer = GPT2Tokenizer.from_pretrained('path_to_save_tokenizer')
model = GPT2LMHeadModel.from_pretrained('path_to_save_model')

# Example usage: Encode input text and generate text
input_text = "How to make noodles in 50 words"
input_ids = tokenizer.encode(input_text, return_tensors='pt')

# Generate text
outputs = model.generate(input_ids, max_length=100, num_return_sequences=1)
print(outputs)

# Decode the generated text
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)

