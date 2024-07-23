import importlib.util
import subprocess
import sys
import time

def install_and_import(package):
    if importlib.util.find_spec(package) is None:
        print("*"*75)
        print(f"{package} kütüphanesi bulunamadı, kurulum başlatılıyor...")
        print("*"*75)
        time.sleep(0.5)
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    else:
        print(f"[Hazır] >> {package}")

install_and_import("random")