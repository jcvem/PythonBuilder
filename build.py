import platform
import subprocess
import os
import sys
import venv
import shutil

# --- Windows Build (Fully Dockerized) ---
def build_windows_via_docker():
    print("🚀 Initiating Windows build via Docker...")
    print("Isolating dependencies inside container...")

    subprocess.run(["docker", "build", "-t", "qt-win-builder", "-f", "Dockerfile.windows", "."], check=True)

    current_dir = os.getcwd()
    subprocess.run([
        "docker", "run", "--rm",
        "-v", f"{current_dir}:/src",
        "qt-win-builder",
        "wine", "pyinstaller", "--noconsole", "--onefile", "main.py"
    ], check=True)

    print("✅ Windows executable generated in ./dist/")

# --- macOS Build (Isolated Virtual Environment) ---
def build_macos_isolated():
    print("🚀 Initiating macOS native build...")

    env_dir = os.path.join(os.getcwd(), ".mac_build_env")

    if not os.path.exists(env_dir):
        print(f"Creating isolated build environment at {env_dir}...")
        venv.create(env_dir, with_pip=True)
    else:
        print("Using existing isolated build environment...")

    venv_python = os.path.join(env_dir, "bin", "python")
    venv_pyinstaller = os.path.join(env_dir, "bin", "pyinstaller")

    print("Installing requirements into the isolated environment...")
    subprocess.run([venv_python, "-m", "pip", "install", "-r", "requirements.txt", "pyinstaller"], check=True)

    # 🚨 CHANGED: Removed --onefile and replaced --noconsole with --windowed
    print("Compiling macOS application...")
    subprocess.run([venv_pyinstaller, "--windowed", "main.py"], check=True)

    print("✅ macOS .app bundle generated in ./dist/")

if __name__ == "__main__":
    os_name = platform.system()

    if os_name == "Windows":
        build_windows_via_docker()
    elif os_name == "Darwin":
        build_macos_isolated()
    else:
        print(f"Operating System '{os_name}' not supported by this script.")
