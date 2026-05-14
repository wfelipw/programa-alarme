import time
from datetime import datetime

# Defina o horário do alarme
alarme = "14:30"

print(f"Alarme definido para {alarme}")

while True:
    agora = datetime.now().strftime("%H:%M")

    if agora == alarme:
        print("⏰ Alarme tocando!")

        # Som no Windows
        import winsound
        winsound.Beep(1000, 2000)

        break

    time.sleep(1)