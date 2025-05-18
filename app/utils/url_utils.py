from urllib.parse import urlencode

def get_api_url(base_url: str, endpoint: str, query_params: dict = None, **kwargs):
    """
    Generate a full API URL dynamically.

    Args:
        base_url (str): Base URL of the service.
        endpoint (str): Endpoint with placeholders like {user_id}.
        query_params (dict, optional): Query parameters to attach (e.g., {"a": 10, "b": 20}).
        **kwargs: Placeholder values for dynamic endpoint paths.

    Returns:
        str: Fully formatted API URL.
    """
    url = base_url+"/"+endpoint.format(**kwargs)  # Replace placeholders
    
    if query_params:  # Append query parameters if present
        url += "?" + urlencode(query_params)

    return url
