import os

def get_file_content(working_directory, file_path):
    try:
        abs_working_file = os.path.abspath(working_directory)
        abs_target_file = os.path.abspath(os.path.join(working_directory, file_path))
        MAX_CHARS = 10000

        if not abs_target_file.startswith(abs_working_file):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            
        if not os.path.isfile(abs_target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(abs_target_file, "r") as f:
            content = f.read(MAX_CHARS + 1)

            if len(content) > MAX_CHARS:
                content = content[:MAX_CHARS] + f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content

    except Exception as e:
        return f"Error: {str(e)}"