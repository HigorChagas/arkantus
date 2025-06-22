import os

def get_files_info(working_directory, directory=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_target_dir = os.path.abspath(os.path.join(working_directory, directory))

        if not abs_target_dir.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(abs_target_dir):
            return f'Error: "{directory}" is not a directory'
        lines = []
        for file in os.listdir(abs_target_dir):
            full_path = os.path.join(abs_target_dir, file)
            if os.path.isfile(full_path) or os.path.isdir(full_path):
                size = os.path.getsize(full_path)
                is_dir = os.path.isdir(full_path)
                lines.append(f" - {file}: file_size={size} bytes, is_dir={is_dir}")
        
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {str(e)}"