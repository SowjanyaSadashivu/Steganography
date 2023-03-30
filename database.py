from sqlalchemy import create_engine
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={'ssl': {
                         'ssl_ca': "/etc/ssl/cert.pem"
                       }})


def add_user(data):
  with engine.connect() as conn:
    query = "insert into register (name, username, password) values (:names, :usernames, :passwords)"
    conn.execute(query,
                 names=data['full_name'],
                 usernames=data['username'],
                 passwords=data['password']);


#below is the code co connect to db and get values from db
'''
#to get information from database
with engine.connect() as conn:
  query = "SELECT * from register;"
  result = conn.execute(text(query))
  print(type(result))  #it gives us cursor type
  print(result.all())  #result.all gives us values in list
  print(type(result.all()))
  result_all = result.all()
  value_dict = dict(
    result_all[0])  # takes one row of result and gives us in dict form

  # to make list of all rows in table
  result_all_dict = []
  for row in result.all():
    result_all_dict.append(dict(row))

# to get the values from db and display on web page

def load_values_from_db():
  with engine.connect as conn:
    result = conn.execute(text("select * from register"))
    result_all_dict = []
    for row in result.all():
      result_all_dict.append(dict(row))
'''
