import os
from together import Together

# Set your API key
api_key = "2fa755e41a3980b42218443dfe7b22e77d98712276c1f5583245304cec003c14"

# Initialize Together AI Client
client = Together(api_key=api_key)

# Ask the user for the folder containing the .txt files
folder_path = "New"

# Prompt message to be included with each chunk of text
prompt_message = "After each Question-Answer pair write ======= so it is easy to differentiate, " \
                 "design them in such a way that i can use them to fine tune a model on it and most importantly," \
                 "I want the author's style to be exactly same as if he is answering the questions himself"

# Loop through each .txt file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        print(f"Processing file: {file_path}")

        # Read raw text from the file
        with open(file_path, "r", encoding="utf-8") as file:
            raw_text = file.read()

        # Split the text into chunks of 8000 characters
        chunk_size = 1000
        text_chunks = [raw_text[i:i+chunk_size] for i in range(0, len(raw_text), chunk_size)]

        # Generate question-answer pairs for each chunk
        qa_pairs = []
        total_chunks = len(text_chunks)
        for i, chunk in enumerate(text_chunks):
            print(f"Processing chunk {i+1}/{total_chunks}...")
            response = client.chat.completions.create(
                model="meta-llama/Llama-3-8b-chat-hf",
                messages=[
                    {"role": "user", "content": prompt_message},
                    {"role": "user", "content": chunk}
                ],
            )
            qa_pairs.extend([{"question": response.choices[0].message.content, "answer": ""}])

        # Save question-answer pairs to a file
        qa_pairs_path = os.path.join('Result', f"{os.path.splitext(filename)[0]}_qa_pairs.txt")
        with open(qa_pairs_path, "w", encoding="utf-8") as f:
            for qa_pair in qa_pairs:
                f.write(f"Question: {qa_pair['question']}\n")
                f.write(f"Answer: {qa_pair['answer']}\n\n")

        print("Question-Answer pairs saved to:", qa_pairs_path)
