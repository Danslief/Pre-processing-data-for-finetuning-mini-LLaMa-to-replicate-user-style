import re

def remove_line_from_file(input_file, output_file):
    # Read file content
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Remove specific line
    text = re.sub(r'question: here are the questionanswer pairs based on the text:', '', text)
    text = re.sub(r'let me know if youd like me to add more questionanswer pairs or make any changes', '', text)
    text = re.sub(r'answer: ', '', text)
    text = re.sub(r'please let me know if youd like me to generate more questionanswer pairs', '', text)
    text = re.sub(r'question: here are the questionanswer pairs with the authors style:', '', text)
    text = re.sub(r'question: heres the first questionanswer pair:', '', text)
    text = re.sub(r'please let me know if this meets your requirements', '', text)
    text = re.sub(r'question: here are the questionanswer pairs:', '', text)
    text = re.sub(r'question: heres a questionanswer pair based on the text:', '', text)
    text = re.sub(r'question: here are the questionanswer pairs in the style of the author answering the questions themselves:', '', text)
    text = re.sub(r'let me know if youd like me to add more questions or modify the existing ones', '', text)
    text = re.sub(r'question: here is the answer:', '', text)
    text = re.sub(r'question: here are the questions and answers in the style you requested:', '', text)
    text = re.sub(r'question: here are the first two questionanswer pairs:', '', text)
    text = re.sub(r'question: here are the questions and answers:', '', text)
    text = re.sub(r'let me know if youd like me to add more questionanswer pairs', '', text)
    text = re.sub(r'question: here are the questions and answers formatted as you requested:', '', text)
    text = re.sub(r'question: here is the qa pair with the requested format:', '', text)
    text = re.sub(r'question: here are the questionanswer pairs to finetune a model on the given code:', '', text)


    # Write modified content back to the file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

input_file = "Finaltest1.txt"
output_file = "Finaltest2.txt"
remove_line_from_file(input_file, output_file)
print("Specified line removed from the file and saved to:", output_file)