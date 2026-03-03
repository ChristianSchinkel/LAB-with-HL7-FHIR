"""Request utilities for handling HTTP requests."""
import requests


def make_request(url, method="GET", headers=None, data=None, timeout=10):
    """Make an HTTP request and return the response.

    Args:
        url (str): The URL to which the request is sent.
        method (str): The HTTP method to use (e.g., 'GET', 'POST').
        headers (dict, optional): A dictionary of HTTP headers to send with
        the request. data (dict, optional): A dictionary of data to send in
        the body of the request (for POST requests).
        timeout (int, optional): Timeout in seconds for the request.
        Defaultsto 10.

    Returns:
        requests.Response: The response object returned by
        the requests library.
    """
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, timeout=timeout)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, data=data,
                                     timeout=timeout)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        response.raise_for_status()  # Raise an exception for HTTP errors
        return response
    except requests.RequestException as e:
        print(f"An error occurred while making the request: {e}")
        return None
