import requests
import threading
import tkinter as tk

esp8266_ip = "192.168.0.110"  # IP-адреса ESP8266
url = f"http://{esp8266_ip}/inline"  # URL для отримання даних
is_polling = False  # Змінна для визначення, чи виконується опитування ESP
cycles = 0  # Лічильник циклів опитування

def start_polling():
    global is_polling, cycles
    is_polling = True
    threading.Thread(target=poll_esp).start()

def stop_polling():
    global is_polling
    is_polling = False

def poll_esp():
    global cycles
    while is_polling:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.text
                with open("MyProjects/ESP_To_Python/data.txt", "a") as file:  # Відкриття файлу для додавання даних
                    file.write(data + "\n")  # Запис даних на новому рядку
                    print(f"Дані {data} успішно додано до файлу data.txt {cycles} разів")
                response_label.config(text=data)
                cycles += 1
                cycle_label.config(text=f"Лічильник циклів: {cycles}")
            else:
                response_label.config(text=f"Помилка: {response.status_code}")
        except Exception as e:
            response_label.config(text=f"Помилка під час виконання запиту: {e}")

def main():
    global response_label, cycle_label

    root = tk.Tk()
    root.title("ESP8266 GUI")
    root.geometry("400x200")

    start_button = tk.Button(root, text="Почати опитування", command=start_polling)
    start_button.pack(pady=10)

    stop_button = tk.Button(root, text="Зупинити опитування", command=stop_polling)
    stop_button.pack(pady=10)

    response_label = tk.Label(root, text="", wraplength=380, justify="center")
    response_label.pack(fill="both", expand=True, padx=10, pady=10)

    cycle_label = tk.Label(root, text="Лічильник циклів: 0")
    cycle_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
