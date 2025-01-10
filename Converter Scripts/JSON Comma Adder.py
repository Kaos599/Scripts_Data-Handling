import json

def format_jsonl(input_file_path, output_file_path):
    
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    
    corrected_json_objects = []

    
    for line in lines:
        
        line = line.strip()
        
        if line:
            try:
                
                json_object = json.loads(line)
                corrected_json_objects.append(json_object)
            except json.JSONDecodeError as e:
                
                
                corrected_json_objects[-1] = json.loads(corrected_json_objects[-1] + ',' + line)

    
    with open(output_file_path, 'w') as file:
        
        for obj in corrected_json_objects:
            file.write(json.dumps(obj) + '\\n')



