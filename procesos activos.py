import psutil
import csv
import time
import getpass


legitimate_processes = [
    "System Idle Process", "System", "svchost.exe", "explorer.exe", "python.exe",
    "chrome.exe", "firefox.exe", "code.exe"
]

current_user = getpass.getuser()


output_file = "processes_dataset.csv"


processes = list(psutil.process_iter(['pid', 'name', 'username']))

# Inicializar la medición de CPU
for p in processes:
    try:
        p.cpu_percent(interval=None)  # Preparar medición
    except:
        continue

# Esperar un tiempo para medir correctamente
time.sleep(6)

with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "pid", "name", "username", "cpu_percent", "memory_percent", "classification"])

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    for proc in processes:
        try:
            info = proc.as_dict(attrs=['pid', 'name', 'username'])
            cpu = proc.cpu_percent(interval=None)
            mem = proc.memory_percent()
            
            name = info['name'] or "unknown"
            username = info['username'] or "unknown"

            # Clasificación
            if name in legitimate_processes or username == current_user:
                classification = "Legítimo"
            else:
                classification = "Sospechoso"

            writer.writerow([
                timestamp,
                info['pid'],
                name,
                username,
                cpu,
                mem,
                classification
            ])

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

print(f"Dataset de procesos guardado en: {output_file}")
