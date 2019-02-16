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

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../db/UFO_ALL_data.sqlite"
db = SQLAlchemy(app)

engine = create_engine("sqlite:///../db/UFO_ALL_data.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare (engine, reflect=True)

# Create our database model
class UFO_ALL_data(db.Model):
    __tablename__ = 'UFO_ALL_data'

    Key = db.Column(db.String, primary_key=True)
    State = db.Column(db.String)
    state_short = db.Column(db.String)
    sightings_total = db.Column(db.String)
    January = db.Column(db.String)
    February = db.Column(db.String)
    March = db.Column(db.String)
    April = db.Column(db.String)
    May = db.Column(db.String)
    June = db.Column(db.String)
    July = db.Column(db.String)
    August = db.Column(db.String)
    September = db.Column(db.String)
    October = db.Column(db.String)
    November = db.Column(db.String)
    December = db.Column(db.String)
    Marijuana = db.Column(db.String)
    No_Military_Bases = db.Column(db.String)
    description = db.Column(db.String)


# Save references to each table
    State_Metadata = Base.classes.UFO_ALL_data
    
    def __repr__(self):
        return '<UFO_ALL_data %r>' % (self.name)



#create session (link) from python to the db
session = Session(engine)

# conn = 'mysql://root:Kansas@2018@127.0.0.1/FRL_Project2_db'
# app.config['SQLALCHEMY_DATABASE_URI'] = conn
# db = SQLAlchemy(app)
# data = pd.read_sql("SELECT distinct State FROM mil_base", conn)
# # data = pd.read_sql("SELECT * FROM mil_base where State = 'Virginia'", conn)
# print(data)



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/restful_api")
def test():

    # stmt = db.session.query(UFO_ALL_data).statement
    # df = pd.read_sql_query(stmt, db.session.bind)

#     df = pd.DataFrame(data, columns=['Site_Name', 'Longitude', 'Latitude'])

#     # Format the data for Plotly
#     plot_trace = {
#         "x": df["Site_Name"].values.tolist(),
#         "y": df["Longitude"].values.tolist(),
#         "z": df["Latitude"].values.tolist(),
#         "type": "bar"
#    }
#     return jsonify(plot_trace)


    query_statement = db.session.query(UFO_ALL_data).\
        order_by(UFO_ALL_data.State.desc()).\
        limit(10).statement
    df = pd.read_sql_query(query_statement, db.session.bind)

    # Format the data for Plotly
    trace = {
        "x": df["State"].values.tolist(),
        "type": "bar"
    }
    return jsonify(trace)
    # results = db.session.query(UFO_ALL_data.State.all())

    # # Create lists from the query results
    # states = [result for result in results]

    # # Generate the plot trace
    # trace = {
    #     "x": states,
    #     "type": "bar"
    # }
    # return jsonify(trace)



    # results = db.session.query(UFO_ALL_data.State, UFO_ALL_data.description).\
    #     order_by(UFO_ALL_data.State.desc()).\
    #     limit(10).all()

    # # Create lists from the query results
    # states = [result[0] for result in results]
    # description = [int(result[1]) for result in results]

    # # Generate the plot trace
    # trace = {
    #     "x": states,
    #     "y": description,
    #     "type": "bar"
    # }
    # return jsonify(trace)

    # stmt = db.session.query(UFO_ALL_data).statement
    # df = pd.read_sql_query(stmt, db.session.bind)
    # ufo_data = df.loc[df[sample] > 1, ["otu_id", "otu_label", sample]]

    # # # Filter the data based on the sample number and
    # # # only keep rows with values above 1
    # # sample_data = df.loc[df[sample] > 1, ["otu_id", "otu_label", sample]]
    # # # Format the data to send as json
    # data = {
    #     "State": sample_data.otu_id.values.tolist(),
    #     "sample_values": sample_data[sample].values.tolist(),
    #     "otu_labels": sample_data.otu_label.tolist(),
    # }
    # return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)






#########################################################

# @app.route("/")
# def home():
#     """Render Home Page."""
#     return render_template("form.html")


# @app.route("/restful_api")
# def restful_api_data():

# # Query for the top 10 emoji data
#     results = pd.read_sql("SELECT * FROM mil_base where State = "Virginia"", conn)
#     # results = db.session.query(Emoji.emoji_char, Emoji.score).\
#     #     order_by(Emoji.score.desc()).\
#     #     limit(10).all()

#     # Create lists from the query results
#     # emoji_char = [result[0] for result in results]
#     # scores = [int(result[1]) for result in results]

#     # Generate the plot trace
#     # trace = {
#     #     "x": emoji_char,
#     #     "y": scores,
#     #     "type": "bar"
#     # }
#     return jsonify(results)


# # @app.route("/emoji_id")
# # def emoji_id_data():
# #     """Return emoji score and emoji id"""

# #     # Query for the emoji data using pandas
# #     query_statement = db.session.query(Emoji).\
# #         order_by(Emoji.score.desc()).\
# #         limit(10).statement
# #     df = pd.read_sql_query(query_statement, db.session.bind)

# #     # Format the data for Plotly
# #     trace = {
# #         "x": df["emoji_id"].values.tolist(),
# #         "y": df["score"].values.tolist(),
# #         "type": "bar"
# #     }
# #     return jsonify(trace)


# # @app.route("/emoji_name")
# # def emoji_name_data():
# #     """Return emoji score and emoji name"""

# #     # Query for the top 10 emoji data
# #     results = db.session.query(Emoji.name, Emoji.score).\
# #         order_by(Emoji.score.desc()).\
# #         limit(10).all()
# #     df = pd.DataFrame(results, columns=['name', 'score'])

# #     # Format the data for Plotly
# #     plot_trace = {
# #         "x": df["name"].values.tolist(),
# #         "y": df["score"].values.tolist(),
# #         "type": "bar"
# #     }
# #     return jsonify(plot_trace)


# if __name__ == '__main__':
#     app.run(debug=True)
