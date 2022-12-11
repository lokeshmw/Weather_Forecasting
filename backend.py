import requests
Api_key = "141710af2113bab9f55ef73e1bcd33d5"


def get_data(place, f_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={Api_key}"
    response = requests.get(url=url)
    data = response.json()
    filtered_data = data["list"]
    values = 8 * int(f_days)
    filtered_data = filtered_data[:values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", f_days=3))
