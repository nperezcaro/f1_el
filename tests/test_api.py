from hypothesis import given, settings, strategies as st
from src.extract import get_yearly_sessions_data

URL = "https://api.openf1.org/v1/sessions"


def test_get_yearly_sessions_data():
    response = get_yearly_sessions_data(url=URL, year="2024")

    assert (
        response.status_code == 200
    ), f"⛔ Expected status code 200, got {response.status_code} instead."

    json_response = response.json()
    assert isinstance(json_response, list), "⛔ Reponse must be a list of dicts."
    assert "year" in json_response[0], "⛔ Reponse JSON does not contain year."


@settings(deadline=1000, max_examples=2)
@given(year=st.sampled_from(["2023", "2024"]))
def test_get_yearly_sessions_data_with_parameter(year):
    response = get_yearly_sessions_data(url=URL, year=year)
    # Ensure the API gracefully handles various query inputs
    assert (
        response.status_code == 200
    ), f"⛔ Query: {year} expected status code 200, got {response.status_code} instead."
