import json

def reformat_jsonl(input_file, output_file):
    
    reformatted_data = []

    
    with open(input_file, 'r') as file:
        
        for line in file:
            
            data = json.loads(line)
            
            reformatted_message = {
                "messages": [
                    {"role": "user", "content": f"{data['context']}\n\n{data['input text']}"},
                    {"role": "model", "content": data['output text']}
                ]
            }
            
            reformatted_data.append(reformatted_message)

    
    with open(output_file, 'w') as file:
        
        json.dump(reformatted_data, file, indent=2)


input_file = 'E:\Stuff\Study\Project_Exhibition_2\AI\Data_Main\JSONL Optimized\dataset copy 3.jsonl'  
output_file = 'E:\Stuff\Study\Project_Exhibition_2\AI\VertexAIData.json'  


reformat_jsonl(input_file, output_file)


print(f"The JSONL data has been reformatted and saved to '{output_file}'.")
