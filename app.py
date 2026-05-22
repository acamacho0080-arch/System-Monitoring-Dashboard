from flask import Flask, render_template
import psutil
import platform
import datetime

app = Flask(__name__)

@app.route("/")
def dashboard():

    cpu_usage = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()
    memory_usage = memory.percent

    disk = psutil.disk_usage('/')
    disk_usage = disk.percent

    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time

    system_info = {
        "cpu": cpu_usage,
        "memory": memory_usage,
        "disk": disk_usage,
        "uptime": str(uptime).split('.')[0],
        "hostname": platform.node(),
        "os": platform.system() + " " + platform.release()
    }

    return render_template("index.html", system=system_info)

if __name__ == "__main__":
    app.run(debug=True)