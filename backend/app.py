from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://faizauser:Fayiz%40293@34.136.236.4/faizadb'
db = SQLAlchemy(app)

# Define your data model
class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    value1 = db.Column(db.String(255))
    value2 = db.Column(db.String(255))

# Route to handle POST request
@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.json
        new_data = Data(value1=data['value1'], value2=data['value2'])
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'message': 'Data submitted successfully!'})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'message': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
