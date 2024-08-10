import serial
import time
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ser = serial.Serial('COM9', 115200)
time.sleep(2)

voltage_data = []
current_data = []
power_data = []

def update(frame):
line = ser.readline().decode('utf-8').strip()
if line:
try:
parts = line.split(", ")
voltage = float(parts[0].split(": ")[1])
current = float(parts[1].split(": ")[1])
power = float(parts[2].split(": ")[1])
voltage_data.append(voltage)
current_data.append(current)
power_data.append(power)

plt.cla()
plt.subplot(3, 1, 1)
plt.plot(voltage_data, label='AC Voltage (V)')
plt.xlabel('Time (s)')
plt.ylabel('AC Voltage (V)')
plt.legend(loc='upper right')
plt.subplot(3, 1, 2)
plt.plot(current_data, label='AC Current (A)')
plt.xlabel('Time (s)')
plt.ylabel('AC Current (A)')
plt.legend(loc='upper right')

plt.subplot(3, 1, 3)
plt.plot(power_data, label='Power (W)')
plt.xlabel('Time (s)')
plt.ylabel('Power (W)')
plt.legend(loc='upper right')

plt.tight_layout()
except (ValueError, IndexError):
Pass

ani = FuncAnimation(plt.gcf(), update, interval=1000, cache_frame_data=False)
plt.show()
df = pd.DataFrame({'Voltage (V)': voltage_data, 'Current (A)': current_data, 'Power (W)': power_data})
df.to_excel('voltage_current_power_data_.xlsx', index=False)
df = pd.DataFrame({'Voltage (V)': voltage_data, 'Current (A)': current_data, 'Power (W)': power_data})
df.to_excel('voltage_current_power_data_.xlsx', index=False)