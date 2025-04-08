import requests

def get_comments(subfeddit, limit=25, start_time=None, end_time=None):
    base_url = f"http://localhost:5000/api/comments/{subfeddit}"
    params = {"limit": limit}
    if start_time:
        params["start_time"] = start_time
    if end_time:
        params["end_time"] = end_time

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return []
