import requests


def get_yearly_sessions_data(url: str, year: str) -> requests.Response:
    response = requests.get(url=url, params={"year": year})

    return response
