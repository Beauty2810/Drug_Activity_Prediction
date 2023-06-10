from flask import Flask, render_template, request
import pandas as pd
#from preprocess import preprocess_data
from model import activity_prediction

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Get the uploaded file
        file = request.files['file']

        # Read the CSV file
        df = pd.read_csv(file, header=None)

        # Preprocess the data
        #preprocessed_data = preprocess_data(df)

        # Run the model
        output = activity_prediction(df)

        return render_template('result.html', output=output)

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)



