"""Functions handling API endpoints."""

import database
import models


def getMeasurements():
    measurements = models.Measurement.query.all()
    measurements = map(lambda m: m.to_dict(), measurements)
    return list(measurements)


def createMeasurement(body):
    measurement = models.Measurement.from_dict(**body)
    database.db.session.add(measurement)
    database.db.session.commit()
    return measurement.to_dict()


def getMeasurementById(id):
    measurement = models.Measurement.query.filter_by(id=id).first()
    if measurement is None:
        return ("Measurement not found.", 404)
    return measurement.to_dict()


def updateMeasurementById(body, id):
    measurement = models.Measurement.query.filter_by(id=id).first()
    if measurement is None:
        return ("Measurement not found.", 404)
    measurement.lat = body["lat"]
    measurement.long = body["long"]
    measurement.lat = body["lat"]
    measurement.time = body["time"]
    measurement.variable = body["variable"]
    measurement.value = body["value"]
    measurement.source = body["source_id"]
    measurement.location = body["location_id"]
    database.db.session.commit()
    return 200


def removeMeasurementById(id):
    measurement = models.Measurement.query.filter_by(id=id).delete()
    if not measurement:
        return ("Measurement not found.", 404)
    database.db.session.commit()
    return 200


def getMeasurementSources():
    measurementsources = models.MeasurementSource.query.all()
    measurementsources = map(lambda k: k.to_dict(), measurementsources)
    return list(measurementsources)


def createMeasurementSource(body):
    measurementsource = models.MeasurementSource.from_dict(**body)
    database.db.session.add(measurementsource)
    database.db.session.commit()
    return measurementsource.to_dict()

def getMeasurementSourceById(id):
    measurementsource = models.MeasurementSource.query.filter_by(id=id).first()
    if measurementsource is None:
        return ("MeasurementSource not found.", 404)
    return measurementsource.to_dict()

def updateMeasurementSourceById(body, id):
    measuremntsource = models.MeasurementSource.query.filter_by(id=id).first()
    if measuremntsource is None:
        return ("Source not found.", 404)
    measuremntsource.lat = body["latitude"]
    measuremntsource.long = body["longitude"]
    measuremntsource.code = body["code"]
    measuremntsource.type = body["measurement_type"]
    measuremntsource.name = body["name"]
    database.db.session.commit()
    return 200

def deleteMeasurementSourceById(id):
    measurementsource = models.MeasurementSource.query.filter_by(id=id).delete()
    if not measurementsource:
        return ("MeasurementSource not found.", 404)
    database.db.session.commit()
    return 200


def getLocations():
    locations = models.Location.query.all()
    locations = map(lambda n: n.to_dict(), locations)
    return list(locations)


def createLocation(body):
    location = models.Location.from_dict(**body)
    database.db.session.add(location)
    database.db.session.commit()
    return location.to_dict()

def getLocationById(id):
    location = models.Location.query.filter_by(id=id).first()
    if location is None:
        return ("Location not found.", 404)
    return location.to_dict()

def updateLocationById(body, id):
    location = models.Location.query.filter_by(id=id).first()
    if location is None:
        return ("Location not found.", 404)
    location.lat = body["latitude"]
    location.long = body["longitude"]
    location.name = body["name"]
    location.elevation = body["elevation"]
    location.type = body["type"]
    location.id = body ["id"]
    location.country = body ["country"]
    database.db.session.commit()
    return 200

def deleteLocationById(id):
    location = models.Location.query.filter_by(id=id).delete()
    if not location:
        return ("Location not found.", 404)
    database.db.session.commit()
    return 200


def getWeatherStations():
    weatherstation = models.WeatherStation.query.all()
    weatherstation = map(lambda n: n.to_dict(), weatherstation)
    return list(weatherstation)


def createWeatherStation(body):
    weatherstation = models.WeatherStation.from_dict(**body)
    database.db.session.add(weatherstation)
    database.db.session.commit()
    return weatherstation.to_dict()

def getWeatherStationById(id):
    weatherstation = models.WeatherStation.query.filter_by(id=id).first()
    if weatherstation is None:
        return ("Source not found.", 404)
    return weatherstation.to_dict()

def updateWeatherStationById(body, id):
    weatherstation = models.WeatherStation.query.filter_by(id=id).first()
    if weatherstation is None:
        return ("weatherstation not found.", 404)
    weatherstation.name = body["name"]
    weatherstation.id= body["location_id"]
    weatherstation.type= body["type"]
    weatherstation.capacity = body["capacity"]
    database.db.session.commit()
    return 200

def deleteWeatherStationById(id):
    weatherstation = models.WeatherStation.query.filter_by(id=id).delete()
    if not weatherstation:
        return ("weatherstation not found.", 404)
    database.db.session.commit()
    return 200

def getSources():
    sources = models.Source.query.all()
    sources = map(lambda k: k.to_dict(), sources)
    return list(sources)


def createSource(body):
    source = models.Source.from_dict(**body)
    database.db.session.add(source)
    database.db.session.commit()
    return source.to_dict()

def getSourceById(id):
    source = models.Source.query.filter_by(id=id).first()
    if source is None:
        return ("Source not found.", 404)
    return source.to_dict()

def updateSourceById(body, id):
    source = models.Source.query.filter_by(id=id).first()
    if source is None:
        return ("Source not found.", 404)
    source.code = body["code"]
    source.name = body["name"]
    source.id = body["id"]
    database.db.session.commit()
    return 200

def deleteSourceById(id):
    source = models.Source.query.filter_by(id=id).delete()
    if not source:
        return ("Source not found.", 404)
    database.db.session.commit()
    return 200

def getVariable():
    variable = models.Variable.query.all()
    variable = map(lambda k: k.to_dict(), variable)
    return list(variable)


def createVariable(body):
    variable = models.Variable.from_dict(**body)
    database.db.session.add(variable)
    database.db.session.commit()
    return variable.to_dict()

def getVariableById(id):
    variable = models.Variable.query.filter_by(id=id).first()
    if variable is None:
        return ("Variable not found.", 404)
    return variable.to_dict()

def updateVariableById(body, id):
    variable = models.Variable.query.filter_by(id=id).first()
    if variable is None:
        return ("Variable not found.", 404)
    variable.unit = body["unit"]
    variable.name = body["name"]
    variable.id = body["id"]
    database.db.session.commit()
    return 200

def deleteVariableById(id):
    variable = models.Variable.query.filter_by(id=id).delete()
    if not variable:
        return ("Variable not found.", 404)
    database.db.session.commit()
    return 200
