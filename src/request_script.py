import requests


def main() -> None:
    """
    Main function to send a request to the web app.
    """
    base_url = "http://localhost:12345"

    print("Welcome to the Request Script!")
    print("Available endpoints:")
    print("1. Homepage (GET /)")
    print("2. Another endpoint (GET /another)")
    option = int(input("Enter the option: ").strip())

    url: str
    if option == 1:
        url = f"{base_url}/"
    elif option == 2:
        url = f"{base_url}/async_test"
    else:
        print("Invalid option selected.")
        return

    try:
        response = requests.get(url, timeout=5)
        print("Response Status Code:", response.status_code)
        print("Response Headers:", response.headers)
        print("Response Text:", response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
