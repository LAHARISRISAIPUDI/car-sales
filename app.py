from flask import Flask, render_template,jsonify,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods = ['GET','POST'])
def predict():
    if request.method=="POST":
        make = request.form.get("make")
        model = request.form.get("model")
        year = request.form.get("year")
        fuelType = request.form.get("fuelType")
        engineHP = request.form.get("engineHP")
        engineCylinders = request.form.get("engineCylinders")
        transmission = request.form.get("transmission")
        drivenWheels=request.form.get("drivenWheels")
        doors=request.form.get("doors")
        vehicleSize=request.form.get("vehicleSize")
        vehicleStyle=request.form.get("vehicleStyle")
        highwayMPG=request.form.get("highwayMPG")
        cityMPG=request.form.get("cityMPG")
        popularity=request.form.get("popularity")
        print(make,model,year,fuelType,engineHP,engineCylinders,transmission,drivenWheels,doors,vehicleSize,vehicleStyle,highwayMPG,cityMPG,popularity)
        return jsonify({"status":"data fetched sucessfully"})
    else:
        return render_template('predict.html')
    
    

if  __name__=='__main__':
    app.run(host="0.0.0.0")
