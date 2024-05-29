import os
from together import Together

# Set your API key
api_key = "17401395fbc5c6305d31ed8e4b88262473efb2fdbf3d4c1352d54dfa83ee1653"

# Initialize Together AI Client
client = Together(api_key=api_key)

# Read raw text from file
raw_text_path = ("C:/Users/mhamz/PycharmProjects/LLaMA-Factory/processed.txt")
with open(raw_text_path, "r", encoding="utf-8") as file:
    raw_text = file.read()

# Split the text into chunks of 8000 characters
chunk_size = 8000
text_chunks = [raw_text[i:i+chunk_size] for i in range(0, len(raw_text), chunk_size)]

# Generate question-answer pairs for each chunk
qa_pairs = []
total_chunks = len(text_chunks)
for i, chunk in enumerate(text_chunks):
    print(f"Processing chunk {i+1}/{total_chunks}...")
    response = client.chat.completions.create(
        model="meta-llama/Llama-3-8b-chat-hf",
        messages=[{"role": "user", "content": chunk}],
    )
    qa_pairs.extend([{"question": response.choices[0].message.content, "answer": ""}])

# Save question-answer pairs to a file
qa_pairs_path = "C:/Users/mhamz/PycharmProjects/LLaMA-Factory/qa_pairs.txt"
with open(qa_pairs_path, "w", encoding="utf-8") as f:
    for qa_pair in qa_pairs:
        f.write(f"Question: {qa_pair['question']}\n")
        f.write(f"Answer: {qa_pair['answer']}\n\n")

print("Question-Answer pairs saved to:", qa_pairs_path)