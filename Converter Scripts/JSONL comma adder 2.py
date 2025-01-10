import json

def format_jsonl(input_file_path, output_file_path):
    # Open the input file
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    # Initialize a list to hold the corrected JSON objects
    corrected_json_objects = []

    # Iterate over each line
    for line in lines:
        # Strip whitespace from the ends
        line = line.strip()
        # If the line is not empty, try to parse it as JSON
        if line:
            try:
                # Parse the line as JSON and append to the list
                json_object = json.loads(line)
                corrected_json_objects.append(json_object)
            except json.JSONDecodeError as e:
                # If there is a JSONDecodeError, it means the line is not a valid JSON object
                # Check if the last character of the previous line is not a comma
                if not corrected_json_objects[-1].rstrip().endswith(','):
                    # If not, append a comma
                    corrected_json_objects[-1] += ','
                # Now try to load the combined line as a JSON object
                corrected_json_objects[-1] = json.loads(corrected_json_objects[-1] + line)

    # Open the output file
    with open(output_file_path, 'w') as file:
        # Write each JSON object to the file on a new line
        for obj in corrected_json_objects:
            file.write(json.dumps(obj) + '\n')

# Example usage:
# format_jsonl('input.jsonl', 'output.jsonl')
format_jsonl("dataset.jsonl", "dataset_new.jsonl")