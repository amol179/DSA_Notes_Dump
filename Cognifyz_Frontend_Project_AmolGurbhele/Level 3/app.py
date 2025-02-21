from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory booking information (this can be replaced by a database later)
booking_data = {}

@app.route('/api/bookings', methods=['GET'])
def get_booking():
    """ Get the booking details """
    if not booking_data:
        return jsonify({"message": "No booking information available."}), 404
    return jsonify(booking_data), 200

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    """ Create new booking and store the information """
    data = request.get_json()

    artist = data.get('artist')
    event_date = data.get('event_date')
    event_location = data.get('event_location')

    if not artist or not event_date or not event_location:
        return jsonify({"message": "Missing required fields."}), 400

    # Store the booking information
    booking_data['artist'] = artist
    booking_data['event_date'] = event_date
    booking_data['event_location'] = event_location

    return jsonify({"message": "Booking created successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
