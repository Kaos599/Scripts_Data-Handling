import json

def restructure_jsonl_to_json(input_file_path, output_file_path):
    # Initialize an empty list to hold the messages
    messages = []

    # Open the input JSONL file and read the lines
    with open(input_file_path, 'r') as file:
        for line in file:
            # Convert each line from JSONL to a dictionary
            message = json.loads(line.strip())
            # Append the dictionary to the messages list
            messages.append(message)

    # Create a new dictionary with the 'messages' key
    reformatted_data = {'messages': messages}

    # Write the reformatted data to the output JSON file
    with open(output_file_path, 'w') as file:
        json.dump(reformatted_data, file, indent=4)

# Example usage:
restructure_jsonl_to_json("E:\Stuff\Study\Project_Exhibition_2\AI\Data_Main\JSONL Optimized\dataset copy 2.jsonl", "E:\Stuff\Study\Project_Exhibition_2\AI\VertexAIData.json")

# Note: Replace 'input_data.jsonl' with the path to your input JSONL file,
# and 'output_data.json' with the desired path for the output JSON file.
