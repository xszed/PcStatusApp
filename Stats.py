import platform
import psutil
import matplotlib.pyplot as plt
import time

my_system = platform.uname()
System.Title("PC Status")

def get_cpu_temp():
    try:
        temps = psutil.sensors_temperatures()
        if 'coretemp' in temps:
            return temps['coretemp'][0].current
    except:
        return None

def Main():

    cpu_temps = []
    cpu_usage = []
    time_stamps = []

    plt.ion()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    for i in range(60):
        usage = psutil.cpu_percent(interval=1)
        cpu_usage.append(usage)

        temp = get_cpu_temp()
        cpu_temps.append(temp if temp is not None else 0)

        time_stamps.append(i)

        ax1.clear()
        ax2.clear()

        ax1.plot(time_stamps, cpu_usage, label="CPU Usage (%)")
        ax1.set_xlabel("Time (s)")
        ax1.set_ylabel("CPU Usage (%)")
        ax1.set_title("CPU Usage Over Time")
        ax1.grid(True)

        ax2.plot(time_stamps, cpu_temps, label="CPU Temperature", color='r')
        ax2.set_xlabel("Time (In Seconds)")
        ax2.set_ylabel("Temperature")
        ax2.set_title("Temperature Over Time")
        ax2.grid(True)

        plt.pause(1)

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    Main()
