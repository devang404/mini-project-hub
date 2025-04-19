# 🔔 Alarm Clock – Python Mini Project

A simple yet functional alarm clock built using **Python**, **Tkinter** for GUI, and **Pygame** for playing a custom alarm sound.

---

## 🚀 Features

- Set multiple alarms in HH:MM format
- Delete alarms from the list
- Automatic time checking every second
- Plays alarm sound and shows a pop-up when triggered
- Built-in GUI using Tkinter

---

## 📦 Requirements

Install required libraries using:

```bash
pip install -r requirements.txt
```

> Note: This project uses the `pygame` library for playing the alarm ringtone.

---

## 🎵 Alarm Sound

Place your custom `.mp3` file inside the `assets/` folder and make sure this line in `alarm1.py` points to the correct path:

```python
self.ringtone_path = "assets/alarm_sound.mp3"
```

---

## 🛠️ How to Run

```bash
python alarm1.py
```

---

## 🖼️ GUI Preview

![GUI Screenshot Placeholder](https://via.placeholder.com/500x300.png?text=Alarm+Clock+GUI)

---

## 📁 Folder Structure

```
alarm-clock/
├── alarm1.py
├── assets/
│   └── alarm_sound.mp3
├── requirements.txt
└── README.md
```

---

## 📌 Notes

- Make sure your system time is accurate.
- Alarms trigger based on the **system clock**.
- Keep the app running to trigger alarms.

---

## 📜 License

This project is open-source under the MIT License.