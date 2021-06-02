import requests


def main():
    response = requests.get("https://api.exchangeratesapi.io/latest")

    if(response.status_code != 200):
        raise Exception("There was an error")

    data = response.json()
    print(data)


if __name__ == "__main__":
    main()
