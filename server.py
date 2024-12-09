from flask import Flask, request, jsonify
from threading import Thread
import tasks
import library

app = Flask(__name__)

# Globalne zmienne
current_task = None
is_running = False

# Funkcja do zarządzania zadaniem
def manage_task(command, target=None, task=None):
    global current_task, is_running
    is_running = False  # Przerwij bieżące zadanie, jeśli istnieje
    current_task = command

    def task_runner():
        global is_running
        is_running = True
        if command == "ulepszaj":
            tasks.ulepszaj(is_running)
        elif command == "penetruj":
            tasks.penetruj(is_running, target)
        elif command == "zaczaruj":
            tasks.zaczaruj(is_running, task)
        is_running = False

    Thread(target=task_runner).start()

# Endpoint do obsługi rozkazów
@app.route('/execute', methods=['POST'])
def execute():
    data = request.json
    command = data.get("command", "").lower()
    target = data.get("target", "")
    task = data.get("task", "")

    if command in ["ulepszaj", "penetruj", "zaczaruj"]:
        manage_task(command, target, task)
        return jsonify({"status": "success", "message": f"Rozkaz {command} wykonuję na pełnej!"})
    else:
        return jsonify({"status": "error", "message": "Nieznany rozkaz, More!"})

# Endpoint do sprawdzania statusu
@app.route('/status', methods=['GET'])
def status():
    if is_running:
        return jsonify({"status": "running", "current_task": current_task})
    else:
        return jsonify({"status": "idle", "message": "Bandzior nic nie robi, bracie!"})

if __name__ == "__main__":
    app.run(port=5000)
