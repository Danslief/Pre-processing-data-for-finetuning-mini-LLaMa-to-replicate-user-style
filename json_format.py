import re
import json

def extract_qa_pairs(file_path):
    qa_pairs = []
    current_pair = {'instruction': '', 'input': '', 'output': ''}

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('q'):
                if current_pair['instruction'] or current_pair['output']:
                    qa_pairs.append(current_pair)
                    current_pair = {'instruction': '', 'input': '', 'output': ''}
                question = re.sub(r'^q\d+:\s*', '', line)
                current_pair['instruction'] = question
            elif line.startswith('a'):
                answer = re.sub(r'^a\d+:\s*', '', line)
                current_pair['output'] = answer
            else:
                if current_pair['output']:
                    current_pair['output'] += ' ' + line
                else:
                    current_pair['instruction'] += ' ' + line

        if current_pair['instruction'] or current_pair['output']:
            qa_pairs.append(current_pair)

    return qa_pairs

def save_to_json(qa_pairs, output_file):
    with open(output_file, 'w') as file:
        json.dump(qa_pairs, file, indent=4)

# Example usage
qa_pairs = extract_qa_pairs('Finaltest2.txt')
save_to_json(qa_pairs, 'output1.json')