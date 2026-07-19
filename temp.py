from flask import Flask, render_template

app = Flask(__name__)

SENSOR_PATH = "/sys/bus/w1/devices/28-01204b4064b4/w1_slave"

def read_temp():
    try:
        with open(SENSOR_PATH, 'r') as f:
            lines = f.readlines()
        if "YES" in lines[0]:
            temp_str = lines[1].split("t=")[-1]
            temp_c = float(temp_str) / 1000.0
            return temp_c
        else:
            return None
    except FileNotFoundError:
        return None

@app.route('/')
def index():
    # Web Visualization
    temp = read_temp()
    if temp is not None:
        temperature = f"{temp:.2f} °C"
    else:
        temperature = "Unable to read temperature"
    return render_template('web.html', temperature=temperature)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
