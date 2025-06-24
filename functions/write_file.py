import os

def write_file(working_directory, file_path, content):
    abs_working_file = os.path.abspath(working_directory)
    abs_target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_target_file.startswith(abs_working_file):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        if not os.path.exists(abs_target_file):
            f = open(abs_target_file, "x")
        
        with open(abs_target_file, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"