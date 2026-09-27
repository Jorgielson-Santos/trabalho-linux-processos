import threading
import time
import os

def tarefa():
    while True:
        soma = sum(i * i for i in range(100000))
        time.sleep(1)

print ("processo iniciado")
print ("PID:", os.getpid())

thread1 = threading.Thread(target=tarefa)
thread2 = threading.Thread(target=tarefa)

thread1.start()
thread2.start()

while True:
    time.sleep(1)

