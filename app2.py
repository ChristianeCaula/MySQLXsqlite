
# import necessary libraries
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

import pandas as pd

from flask_sqlalchemy import SQLAlchemy

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

app = Flask(__name__)


# conn = 'mysql://root:Kansas@2018@127.0.0.1/FRL_Project2_db'
# app.config['SQLALCHEMY_DATABASE_URI'] = conn
# db = SQLAlchemy(app)

##########SQLITE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/UFO_ALL_data.sqlite"
db = SQLAlchemy(app)
engine = create_engine("sqlite:///db/UFO_ALL_data.sqlite")


# data = pd.read_sql("SELECT distinct State FROM mil_base", conn)
# data = pd.read_sql("SELECT * FROM mil_base where State = 'Virginia'", conn)
# print(data)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/states")
def test():

    # df = pd.DataFrame(data, columns=['State', 'Longitude', 'Latitude'])
    data = pd.read_sql("SELECT distinct State FROM ufo_all_data", conn)
    df = pd.DataFrame(data, columns=['State'])
    # print(df)
    state_list = df['State'].tolist()
    # Format the data for Plotly
#     plot_trace = {
#         "x": df["State"].values.tolist()
#         # "type": "bar"
#    }
    # return jsonify(plot_trace)
    return jsonify(state_list)

    
@app.route("/states/<state>")

def state_metadata(state):
    """Return the MetaData for a chosen state."""
    
    # print(state)

    # results = pd.read_sql("SELECT State, Sightings_Total, Military_Bases, Marijuana FROM ufo_all_data where State = '"+ state+"'", conn)
    # results = pd.read_sql(f"SELECT State, Sightings_Total, Military_Bases, Marijuana FROM ufo_all_data where State = '{state}'", conn)
    
    results = db.session.query(ufo_all_data.State, ufo_all_data.Sightings_Total, ufo_all_data.Military_Bases, ufo_all_data.Marijuana).\
        limit(10).statement
    
    # Create a dictionary entry for each row of metadata information
    # print(type(results))
    
    # sql = ('SELECT State, Sightings_Total, Military_Bases, Marijuana FROM ufo_all_data where State = state')
    # results = db.engine.execute(sql)
    # print(results)
    state_metadata = results.to_dict('records')
    json_metatada = state_metadata[0]
    print(results)
    # for result in results.iterrows:
    #     print(result)

        # state_metadata["State"] = result[0]
        # state_metadata["Sightings_Total"] = result[1]
        # state_metadata["Military_Bases"] = result[2]
        # state_metadata["Marijuana"] = result[3]

    # print(state_metadata)
    
    return jsonify(json_metatada)

@app.route("/months/<state>")
def state_months(state):

    # df = pd.DataFrame(data, columns=['State', 'Longitude', 'Latitude'])
    results = pd.read_sql("SELECT January, February, March, April, May, June, July, August, September, October, November, December FROM ufo_all_data where State = '"+ state+"'", conn)

    state_months = results.to_dict('records')
    print(state_months)
    print(state_months[0])
    
    months_name_list = []
    months_value_list = []

    for month_name in state_months[0]:
        months_name_list.append(month_name)

    for month_value in state_months[0].values():
        months_value_list.append(str(month_value))

    print(months_value_list)
    print(months_name_list)
        # print(month)

    trace = {
        "x": months_name_list,
        "y": months_value_list,
        # "x": str(months_value_list),
        # "y": months_name_list,
        "type": "bar"
    }
    return jsonify(trace)

    # json_months = state_months[0]
    # return jsonify(str(state_months[0]))

@app.route("/months_pie/<state>")
def state_months_pie(state):

    # df = pd.DataFrame(data, columns=['State', 'Longitude', 'Latitude'])
    results = pd.read_sql("SELECT January, February, March, April, May, June, July, August, September, October, November, December FROM ufo_all_data where State = '"+ state+"'", conn)

    state_months = results.to_dict('records')
    print(state_months)
    print(state_months[0])
    
    months_name_list = []
    months_value_list = []

    for month_name in state_months[0]:
        months_name_list.append(month_name)

    for month_value in state_months[0].values():
        months_value_list.append(str(month_value))

    print(months_value_list)
    print(months_name_list)
        # print(month)

    trace = {
        "values": months_value_list,
        "labels": months_name_list,
        "type": "pie"
    }
    return jsonify(trace)

if __name__ == "__main__":
    # app.run(port=5001)
    app.run(debug=True)

