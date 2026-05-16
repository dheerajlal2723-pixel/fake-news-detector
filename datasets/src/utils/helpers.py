def log_message(message):
    print(f"[LOG] {message}")

def load_config(config_file):
    import json
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config