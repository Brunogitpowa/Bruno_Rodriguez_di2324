import subprocess
import sys
import os

def main():
    # Iniciar el script de inicio de sesión
    ruta_a_login = os.path.join(os.path.dirname(
        __file__), "login.py")
    resultado_login = subprocess.run(["python", ruta_a_login])

if __name__ == "__main__":
    main()
