from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory booking information (this can be replaced by a database later)
booking_data = {}

artists = [
    {"name": "Earl Klugh", "genre": "Rock, Jazz, Pop", "image_url": "earlklugh.jpg"},
    {"name": "Whitney Houston", "genre": "Rock, Pop", "image_url": "WhitneyHouston.jpg"}
]

# Store bookings with unique IDs
bookings = {}
booking_counter = 1  # To simulate a unique booking ID (you can replace it with UUIDs or database)

@app.route('/api/artists', methods=['GET'])
def get_artists():
    return jsonify({"artists": artists})

@app.route('/api/bookings', methods=['GET'])
def get_booking():
    """ Get the booking details """
    if not booking_data:
        return jsonify({"message": "No booking information available."}), 404
    return jsonify(booking_data), 200

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    """ Create new booking and store the information """
    global booking_counter  # Use the global counter for IDs
    data = request.get_json()

    artist = data.get('artist')
    event_date = data.get('event_date')
    event_location = data.get('event_location')

    if not artist or not event_date or not event_location:
        return jsonify({"message": "Missing required fields."}), 400

    # Check if the artist exists
    if artist not in [a["name"] for a in artists]:
        return jsonify({"message": "Artist not found."}), 404

    # Store the booking information
    booking = {
        'id': booking_counter,
        'artist': artist,
        'event_date': event_date,
        'event_location': event_location
    }

    bookings[booking_counter] = booking
    booking_counter += 1  # Increment the booking ID counter

    return jsonify({"message": "Booking created successfully!", "booking": booking}), 201

if __name__ == '__main__':
    app.run(debug=True)
