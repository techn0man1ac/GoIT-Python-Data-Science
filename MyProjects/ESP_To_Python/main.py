import requests

def main():
    esp8266_ip = "192.168.0.110"  # IP-адреса ESP8266
    url = f"http://{esp8266_ip}/inline"  # URL для отримання даних

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text
            with open("MyProjects/ESP_To_Python/data.txt", "a") as file:  # Відкриття файлу для додавання даних
                file.write(data + "\n")  # Запис даних на новому рядку
            print(f"Дані {data} успішно додано до файлу data.txt")
        else:
            print(f"Помилка: {response.status_code}")
    except Exception as e:
        print(f"Помилка під час виконання запиту: {e}")

if __name__ == "__main__":
    main()
