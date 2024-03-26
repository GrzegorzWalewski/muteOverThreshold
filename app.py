import sounddevice as sd
import numpy as np
import tkinter as tk
import os
import sys
from tkinter import ttk
import threading
from pynput.keyboard import Key, Controller

muted = False

def get_image_path(filename):
    if getattr(sys, 'frozen', False):
        # Running in a bundle (e.g. PyInstaller)
        bundle_dir = sys._MEIPASS
    else:
        # Running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(bundle_dir, filename)

def change_mute():
    global muted
    muted = not muted
    keyboard = Controller()
    keyboard.press(Key.pause)
    keyboard.release(Key.pause)
    
def list_audio_devices():
    devices = sd.query_devices()
    return [device['name'] for device in devices]

def create_gui():
    window = tk.Tk()
    window.tk.call('tk', 'scaling', 3)
    window.title("MuteOverThreshold")
    icon_path = get_image_path('icon.ico')
    window.iconbitmap(icon_path)
    window.geometry("500x800")
    window.configure(bg="#1f1f1f")
    window.resizable(False, False)

    icon_path = get_image_path("icon_mini.png")
    icon = tk.PhotoImage(file=icon_path)
    icon_label = tk.Label(window, image=icon, bg="#1f1f1f")
    icon_label.pack()

    threshold_label = tk.Label(window, text="RMS Threshold", bg="#1f1f1f", fg="#44e3f8", pady=10)
    threshold_label.pack()
    threshold_input = tk.Entry(window, bg="#1f1f1f", fg="#44e3f8")
    threshold_input.config(bg="#1f1f1f")
    threshold_input.insert(0, "0.07")
    threshold_input.pack()

    device_combo = tk.StringVar(window)
    device_combo.set(list_audio_devices()[2])  # Default selected device

    label_device = tk.Label(window, text="Select Audio Device:", bg="#1f1f1f", fg="#44e3f8", pady=10)
    label_device.pack()

    combo_device = tk.OptionMenu(window, device_combo, *list_audio_devices())
    combo_device.config(bg="#1f1f1f", fg="#44e3f8", highlightthickness=0)
    combo_device.pack()

    label_rms = tk.Label(window, text="Current RMS Value:", bg="#1f1f1f", fg="#44e3f8", pady=10)
    label_rms.pack()

    rms_value = tk.Label(window, text="", bg="#1f1f1f", fg="#44e3f8", pady=10)
    rms_value.pack()

    label_mute = tk.Label(window, text="Microphone Status:", bg="#1f1f1f", fg="#44e3f8", pady=10)
    label_mute.pack()
    canvas = tk.Canvas(window, width=100, height=100, bg="#1f1f1f", highlightthickness=0)
    canvas.pack()

    def start_monitoring():
        canvas.create_oval(25, 25, 75, 75, fill="green")
        monitoring.set(True)
        threshold_input.configure(state='readonly')
        selected_device = device_combo.get()
        def monitor():
            nonlocal selected_device
            print(f"Checking {selected_device} with threshold {threshold_input.get()}")
            
            rms_values = rms_generator(device_name=selected_device)
            for rms_val in rms_values:
                if not monitoring.get():
                    break
                rms_value.config(text=round(rms_val, 2))

                if rms_val > float(threshold_input.get()):
                    if not muted:
                        print(f"Too loud! Muting {rms_val:.2f}")
                        canvas.delete("all")
                        canvas.create_oval(25, 25, 75, 75, fill="red")
                        change_mute()
                else:
                    if muted:
                        print(f"Back to normal. Unmuting {rms_val:.2f}")
                        canvas.delete("all")
                        canvas.create_oval(25, 25, 75, 75, fill="green")
                        change_mute()
        threading.Thread(target=monitor).start()

    def stop_monitoring():
        monitoring.set(False)
        threshold_input.configure(state='normal')
        rms_value.config(text="-")
        if muted:
            change_mute()
            canvas.create_oval(25, 25, 75, 75, fill="green")

    def stop_program():
        stop_monitoring()
        window.destroy()
        exit()

    style = ttk.Style()
    style.configure('Custom.TFrame', background="#1f1f1f")

    center_frame = ttk.Frame(window, style='Custom.TFrame')
    center_frame.pack(pady=10)

    start_button = tk.Button(center_frame, text="START", command=start_monitoring, bg="#1f1f1f", fg="green", padx=50)
    start_button.grid(row=0, column=0, padx=5, pady=5)

    stop_button = tk.Button(center_frame, text="STOP", command=stop_monitoring, bg="#1f1f1f", fg="red", padx=50)
    stop_button.grid(row=0, column=1, padx=5, pady=5)

    exit_button = tk.Button(window, text="EXIT", command=stop_program, bg="#1f1f1f", fg="#44e3f8", pady=10, padx=50)
    exit_button.pack(side="top", pady=10)

    monitoring = tk.BooleanVar()
    monitoring.set(True)

    rms_value.config(text="-")
    canvas.create_oval(25, 25, 75, 75, fill="green")

    window.mainloop()

def rms_generator(device_name):
    stream = sd.InputStream(device=device_name, channels=1, samplerate=44100)
    stream.start()

    try:
        while True:
            audio_data, _ = stream.read(1024)
            rms_value = np.sqrt(np.mean(audio_data**2))
            print(f"RMS value: {rms_value:.2f}")
            yield rms_value
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    finally:
        stream.stop()

if __name__ == "__main__":
    create_gui()