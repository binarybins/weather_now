from weather_now.accuweather import get_weather

def test_weather():
    assert len(get_weather()) == 2
