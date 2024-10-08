import os
import json
import yaml

def dynamic_dirname(path, depth):
    """
    Recursively traverses the directory path to the specified depth.

    Args:
        path (str): The starting path.
        depth (int): The desired depth to traverse.

    Returns:
        str: The directory path at the specified depth.
    """

    if depth == 0:
        return path

    parent_dir = os.path.dirname(path)
    return dynamic_dirname(parent_dir, depth - 1)


def ignore_warning():
    """
    Ignores all warnings during execution.

    This function is useful for suppressing warnings that may not be relevant
    or for cases where you want to focus on specific errors.
    """
    import warnings
    warnings.filterwarnings("ignore")


def read_yaml(file_path: str) -> dict:
    """
    Reads and parses a YAML file into a Python dictionary.

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        dict: The parsed YAML data as a dictionary.

    Raises:
        FileNotFoundError: If the specified file is not found.
        yaml.YAMLError: If there's an error parsing the YAML file.
    """
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {file_path}")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML: {e}")


# ===== JSON OPERATION ===== 
def json_to_str(payload: dict) -> str:
    """
    Converts a Python dictionary to a JSON string.

    Args:
        payload (dict): The dictionary to be converted.

    Returns:
        str: The JSON representation of the dictionary.
    """
    return json.dumps(payload)


def str_to_json(payload: str) -> dict:
    """
    Converts a JSON string to a Python dictionary.

    Args:
        payload (str): The JSON string to be converted.

    Returns:
        dict: The parsed JSON data as a dictionary.

    Raises:
        ValueError: If the input string is not a valid JSON.
    """
    try:
        return json.loads(payload)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON string: {e}")


def append_data_to_json(data, filepath):
    """
    Appends data to a JSON file in a specified directory. Handles creation.

    Args:
        data: The data to be appended (must be JSON serializable, typically a dictionary or a list).
        filename: The name of the JSON file (e.g., "my_data.json").
        directory: The directory where the file should be saved.
    
    Returns:
        True if the file was appended successfully, False otherwise. Raises exceptions for serious issues.
    """
    if not isinstance(data, dict) and not isinstance(data, list):
        raise TypeError("Data must be a dictionary or a list.")

    try:
        with open(filepath, 'a+') as f:
            try:
                file_data = json.load(f)
            except json.JSONDecodeError:
                file_data = []  # Handle empty or corrupted files
            
            file_data.append(data)
            json.dump(file_data, f, indent=4)
            f.truncate()
        print('Done')

    except (IOError, OSError) as e:
        print(f"Error appending to file {filepath}: {e}")
    except TypeError as e:
        print(f"Error serializing data to JSON: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def append_data_to_text(data, filepath):
    """
    Appends data to a text file in a specified directory. Handles creation.

    Args:
        data: The data to be appended (must be a string).
        filepath: The path to the text file (e.g., "/path/to/my_data.txt").
    
    Returns:
        True if the file was appended successfully, False otherwise. Raises exceptions for serious issues.
    """
    if not isinstance(data, str):
        raise TypeError("Data must be a string.")

    try:
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(filepath, 'a+') as f:
            f.write(data + "\n")  # Append data with a newline character
        print('Done')

    except (IOError, OSError) as e:
        print(f"Error appending to file {filepath}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


