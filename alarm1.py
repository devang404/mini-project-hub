import tkinter as tk
from tkinter import messagebox
import datetime
import pygame
import threading


class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("ALARM CLOCK")
        self.alarms = []
        self.triggered_alarms = []  # List to track triggered alarms
        self.alarm_active = False  # Initialize alarm state
        self.ringtone_path = r"C:/Users/Devang/Desktop/rock paper scissor/aud-20210213-wa0007-52714-1-52897.mp3"
        pygame.mixer.init()

        tk.Label(root, text="Set Alarm Time (HH:MM)").grid(row=0, column=0, padx=10, pady=5)
        self.alarm_entry = tk.Entry(root)
        self.alarm_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(root, text="Set Alarm", command=self.add_alarm).grid(row=0, column=2, padx=10, pady=5)
        self.alarms_listbox = tk.Listbox(root, width=50, height=10)
        self.alarms_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

        tk.Button(root, text="Delete Alarm", command=self.delete_alarm).grid(row=2, column=0, columnspan=3, padx=10, pady=5)
        self.check_alarms()

    def add_alarm(self):
        alarm_time_str = self.alarm_entry.get().strip()
        try:
            alarm_time = datetime.datetime.strptime(alarm_time_str, '%H:%M').time()
            self.alarms.append(alarm_time)
            self.alarms_listbox.insert(tk.END, alarm_time.strftime('%H:%M'))
            self.alarm_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid time in HH:MM format.")

    def delete_alarm(self):
        selected_index = self.alarms_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.alarms[index]
            self.alarms_listbox.delete(index)

    def play_alarm_sound(self):
        try:
            pygame.mixer.music.load(self.ringtone_path)
            pygame.mixer.music.play(loops=-1)
            self.alarm_active = True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to play alarm sound: {e}")

    def stop_alarm_sound(self):
        pygame.mixer.music.stop()
        self.alarm_active = False

    def show_alarm_message(self, alarm_time):
        message = f"Alarm at {alarm_time.strftime('%H:%M')}!\nClick OK to stop."
        response = messagebox.showinfo("Alarm", message)
        if response == "ok":
            self.stop_alarm_sound()

    def trigger_alarm(self, alarm_time):
        """Triggers the alarm with sound and message."""
        threading.Thread(target=self.play_alarm_sound).start()  # Play sound immediately
        self.show_alarm_message(alarm_time)  # Show notification
        self.triggered_alarms.append(alarm_time)  # Add to triggered list

    def check_alarms(self):
        """Continuously checks if the alarm time is reached."""
        now = datetime.datetime.now().time()
        for alarm_time in self.alarms:
            if (
                now.hour == alarm_time.hour
                and now.minute == alarm_time.minute
                and now.second == 0
                and alarm_time not in self.triggered_alarms
            ):
                threading.Thread(target=self.trigger_alarm, args=(alarm_time,)).start()
                break

        # Reset triggered alarms list after a minute
        if now.second == 59:
            self.triggered_alarms = []

        self.root.after(1000, self.check_alarms)  # Check every second


if __name__ == "__main__":
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()
