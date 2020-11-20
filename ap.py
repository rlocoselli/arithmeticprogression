from flask import Flask
import json
import ap_functions

app = Flask(__name__)

@app.route('/lastProgression/<root>/<firstnumber>/<count>')
def lastProgression(root, firstnumber, count) -> int:
    return ap_functions.calculate_last_number_arithmetic_progression(root,firstnumber,count)

@app.route('/sumProgression/<root>/<firstnumber>/<count>')
def sumProgression(root, firstnumber, count) -> int:
    return ap_functions.calculate_sum_number_arithmetic_progression(root,firstnumber,count)

@app.route('/getMembers/<root>/<firstnumber>/<count>')
def getMembers(root, firstnumber, count) -> int:
    return json.dumps(ap_functions.getApMembers(root,firstnumber,count),default=lambda o: o.encode(), indent=4)