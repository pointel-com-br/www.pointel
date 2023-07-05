def clean_file_name(name: str) -> str: 
    name = name.replace("\"", "")
    name = name.replace("\\", "")
    name = name.replace("/", "")
    name = name.replace("|", "")
    name = name.replace(":", "")
    name = name.replace("*", "")
    name = name.replace("<", "")
    name = name.replace(">", "")
    name = name.replace("?", "")
    return name