from flask import Flask
app = Flask(__name__)

@app.route('/lastProgression/<root>/<firstnumber>/<count>')
def calculate_last_number_arithmetic_progression(root, firstnumber, count) -> int:
    return str(int(firstnumber) + (int(count)-1)*int(root))

@app.route('/sumProgression/<root>/<firstnumber>/<count>')
def calculate_sum_number_arithmetic_progression(root, firstnumber, count) -> int:
    x = int(firstnumber)
    mySum = x;
    i = 1;
    while i < int(count):
        x = x + int(root)
        i = i + 1
        mySum = mySum + x
    
    return str(mySum)