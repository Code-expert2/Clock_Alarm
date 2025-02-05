# Import Required Libraries
from tkinter import *
import datetime
import time
from threading import Thread
import pygame
import os
from pydub import AudioSegment
from pydub.generators import Sine

# Initialize the mixer for pygame
pygame.mixer.init()

# Create and export the beep sound if not exists
def create_alarm_sound():
    beep = Sine(440).to_audio_segment(duration=1000)  # 1000ms = 1 second
    beep.export("/home/talha/Desktop/project 1/alarm.mp3", format="mp3")
    print("Alarm sound created!")

# Function to Play Sound
def play_sound():
    sound_file = "/home/talha/Desktop/project 1/alarm.mp3"
    
    # Check if the sound file exists
    if os.path.exists(sound_file):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    else:
        print(f"Error: Sound file '{sound_file}' not found!")

# Function for Threading
def Threading():
    t1 = Thread(target=alarm)
    t1.start()

# Alarm Function
def alarm():
    while True:
        # Get the alarm time from user input
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        # Wait for one second
        time.sleep(1)

        # Get the current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current Time: {current_time} | Alarm Time: {set_alarm_time}")

        # Check if the current time matches the alarm time
        if current_time == set_alarm_time:
            print("⏰ Time to Wake Up!")
            play_sound()
            break  # Stop checking after the alarm rings

# Check if the sound file exists; if not, create it
if not os.path.exists("/home/talha/Desktop/project 1/alarm.mp3"):
    create_alarm_sound()

# Create GUI Window
root = Tk()
root.title("Alarm Clock")
root.geometry("400x200")

# Add Labels
Label(root, text="Alarm Clock", font=("Helvetica", 20, "bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica", 15, "bold")).pack()

# Create Frame for Input
frame = Frame(root)
frame.pack()

# Hour Dropdown
hour = StringVar(root)
hours = tuple(f"{i:02d}" for i in range(24))  # Generates '00' to '23'
hour.set(hours[0])
OptionMenu(frame, hour, *hours).pack(side=LEFT)

# Minute Dropdown
minute = StringVar(root)
minutes = tuple(f"{i:02d}" for i in range(60))  # Generates '00' to '59'
minute.set(minutes[0])
OptionMenu(frame, minute, *minutes).pack(side=LEFT)

# Second Dropdown
second = StringVar(root)
seconds = tuple(f"{i:02d}" for i in range(60))  # Generates '00' to '59'
second.set(seconds[0])
OptionMenu(frame, second, *seconds).pack(side=LEFT)

# Set Alarm Button
Button(root, text="Set Alarm", font=("Helvetica", 15), command=Threading).pack(pady=20)

# Run Tkinter Main Loop
root.mainloop()