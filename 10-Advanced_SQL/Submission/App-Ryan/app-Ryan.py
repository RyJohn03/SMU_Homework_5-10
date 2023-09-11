# Import the dependencies.
import numpy as np
import pandas as pd
import sqlalchemy
import json
from sqlalchemy import create_engine, text
from flask import Flask, jsonify
from sqlalchemy.ext.automap import automap_base

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"""<h1>Welcome to the Hawaii Climate Analysis API</h1><br/>
        <h2>Available Routes:</h2><br/>
        <a href="/api/v1.0/precipitation">Precipitation</a><br/>
        <a href="/api/v1.0/stations">Station</a><br/>
        <a href="/api/v1.0/tobs">TOBS</a><br/>
        <a href="/api/v1.0/2016-08-23">Start</a><br/>
        <a href="/api/v1.0/2016-08-23/2016-09-23">Start / End</a><br/>"""
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Get precipitation"""
    query = text("""
                SELECT
                    date,
                    station,
                    prcp
                FROM
                    measurement
                Where
                    date >= '2016-08-23';
            """)
    df = pd.read_sql(query, engine)
    data = json.loads(df.to_json(orient="records"))
    return(data)

@app.route("/api/v1.0/stations")
def stations():
    """Get stations"""
    query = text("""
                SELECT
                    station,
                    count(*) as num_obs
                FROM
                    measurement
                Group By
                    station
                Order By
                    num_obs desc;
            """)

    df = pd.read_sql(query, engine)
    data = json.loads(df.to_json(orient="records"))
    return(data)

@app.route("/api/v1.0/tobs")
def temperature():
    """Get tobs"""
    query = text("""
                SELECT
                    station,
                    date,
                    tobs as temperature
                FROM
                    measurement
                Where
                 station = 'USC00519281'
                 and date >= '2016-08-23'
                Order By 
                 date asc;
            """)

    df = pd.read_sql(query, engine)
    data = json.loads(df.to_json(orient="records"))
    return(data)

@app.route("/api/v1.0/<start>")
def temperature_start(start):
    """Get stations"""
    query = text(f"""
                SELECT
                    station,
                    min(tobs) as tmin, 
                    avg(tobs) as tmean,
                    max(tobs) as tmax
                FROM
                    measurement
                Where
                 date >= '{start}';
            """)

    df = pd.read_sql(query, engine)
    data = json.loads(df.to_json(orient="records"))
    return(data)

@app.route("/api/v1.0/<start>/<end>")
def temperature_start_end(start, end):
    """Get stations"""
    query = text(f"""
                SELECT
                    station,
                    min(tobs) as tmin, 
                    avg(tobs) as tmean,
                    max(tobs) as tmax
                FROM
                    measurement
                Where
                 date >= '{start}'
                 and date <= '{end}';
            """)

    df = pd.read_sql(query, engine)
    data = json.loads(df.to_json(orient="records"))
    return(data)

# Run the website
if __name__ == '__main__':
    app.run(debug=True)