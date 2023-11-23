from flask import request
import sqlalchemy as db
import pandas as pd
import os

from . import api

con = db.create_engine(os.environ.get("SQLALCHEMY_DATABASE_URI"))

@api.route("/upload-file", methods=["POST"])
def upload_file():
    file = request.files['file']
    usecols = ['first_name', 'last_name', 'email', 'gender', 'date_of_birth', 'phone_number']
    result = 'Undefined'

    try:
        file_data = pd.read_csv(file, usecols=usecols, index_col=None)
        print(file_data)
    except Exception as err:
        print("Columns Mismatch! ", err)
    else:
        file_data.to_sql(name='rapgen_db', if_exists='append', con=con, index=False)
        print('WAS here')
        result = 'success'
    finally:
        print("Done")
        return {'result': result}
