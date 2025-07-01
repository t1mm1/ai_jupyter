def object_to_dict(obj):
    """
    Recursively converts an object (or a list of objects) with __dict__ attribute into dictionaries.
    Useful for serializing custom objects, e.g. for JSON serialization.

    Args:
        obj: The object or list of objects to convert

    Returns:
        dict, list, or the raw value if not an object
    """
    if isinstance(obj, list):
        # If obj is a list, convert each item in the list recursively
        return [object_to_dict(item) for item in obj]
    elif hasattr(obj, "__dict__"):
        # If obj has attributes (is a custom class), convert each attribute recursively
        return {key: object_to_dict(value) for key, value in obj.__dict__.items()}
    else:
        # If obj is a primitive type (int, str, etc.), just return it as is
        return obj
