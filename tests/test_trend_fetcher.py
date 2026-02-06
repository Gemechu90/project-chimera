from skills.trend_fetcher.skill import fetch_trends

def test_trends():
    data = fetch_trends()
    assert "trends" in data
