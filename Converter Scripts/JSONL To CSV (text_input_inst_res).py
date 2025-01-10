import csv
import json

# Function to convert the format
def convert_format(input_query, instruction, response):
    return {
        "text": f"{instruction} Write a response that appropriately completes the request.\n\n### Human:\n{input_query}\n### Assistant:\n{response}"
    }

# Read the CSV file and process each row
def process_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile, \
         open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = ['text']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in reader:
            formatted_data = convert_format(row['input_query'], row['instruction'], row['response'])
            writer.writerow({'text': json.dumps(formatted_data)})

# Replace 'your_input.csv' and 'your_output.csv' with your actual file names
process_csv('E:\Stuff\Study\Project_Exhibition_2\AI\Data_Main\JSONL Vertex AI Main\convertjson (1) (1).jsonl', 'train_v3.csv')
