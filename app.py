from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

rooms = {
    'R1': None,
    'R2': None,
    'R3': None
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reserve', methods=['POST'])
def reserve():
    data = request.json
    app.logger.info('Received reservation request: %s', data)
    room = data['room']
    if room in rooms:
        rooms[room] = {
            'customer_name': data['customer_name'],
            'num_people': data['num_people'],
            'start_time': data['start_time'],
            'end_time': data['end_time']
        }
        app.logger.info('Reservation successful for room: %s', room)
        return jsonify({'status': 'success'}), 200
    app.logger.error('Invalid room: %s', room)
    return jsonify({'status': 'error', 'message': 'Invalid room'}), 400

@app.route('/rooms')
def get_rooms():
    return jsonify(rooms), 200

@app.route('/cancel', methods=['POST'])
def cancel_reservation():
    data = request.json
    app.logger.info('Received cancellation request: %s', data)
    room = data['room']
    if room in rooms and rooms[room] is not None:
        rooms[room] = None
        app.logger.info('Cancellation successful for room: %s', room)
        return jsonify({'status': 'success'}), 200
    app.logger.error('Invalid room or no reservation to cancel: %s', room)
    return jsonify({'status': 'error', 'message': 'Invalid room or no reservation to cancel'}), 400

if __name__ == '__main__':
    app.run(debug=True)
