import psutil
for proc in psutil.process_iter():
    try:
        print(proc.name())
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
