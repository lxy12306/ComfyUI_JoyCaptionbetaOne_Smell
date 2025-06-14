import torch
import json
import os
import logging

def is_bf16_supported(device):
    # ...existing code...
    return (
        torch.cuda.is_available() and
        torch.cuda.get_device_capability(device)[0] >= 8
    )

def read_json_file(dir_name, file_name):
    # ...existing code...
    encodings = ['utf-8', 'utf-8-sig', 'latin1', 'cp1252', 'gbk']
    file_path = os.path.join(dir_name, file_name)
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                content = f.read()
                data = json.loads(content)
                return data
        except Exception:
            continue
    logging.error(f"Error: Failed to load {file_path} with any supported encoding")
    return {}

def read_json_value(file_path, key, expected_type=None):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            value = data.get(key, None)
            if expected_type is not None and not isinstance(value, expected_type):
                return None
            return value
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON from the file: {file_path}")
        print(f"具体错误信息: {e}")
        return None
