from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd

app = Flask(__name__)

submitted_data = []



StaffDF = pd.read_excel("Staff.xlsx", na_filter=False)


    

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        day = request.form['day']
        week = request.form['week']
        #return render_template('rooms.html', day=day, week=week)
    return render_template('home.html')

@app.route('/rooms', methods=['GET', 'POST'])
def rooms():
    global submitted_data
    day = request.args.get('day', '')
    week = request.args.get('week', '')

    df = pd.read_excel("Rooms Sept 2024.xlsx", na_filter=False)
    rooms = df['ROOM'].tolist()
    print(rooms)
    
    if request.method == 'POST':
        room = request.form.get('room')
        periods = request.form.getlist('period')

        if room and periods:
            # Add the submitted data to the list
            submitted_data.append({
                'room': room,
                'periods': periods,
                'day': day,
                'week': week
            })
            return redirect(url_for('rooms', day=day, week=week))  # Refresh the page to show the updated list

    return render_template('rooms.html', day=day, week=week, submitted_data=submitted_data, rooms=rooms)

@app.route('/remove', methods=['POST'])
def remove():
    global submitted_data
    try:
        index = int(request.json.get('index'))  # Retrieve the index from the request data
        if 0 <= index < len(submitted_data):
            submitted_data.pop(index)  # Remove the item at the specified index
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'failure', 'message': 'Invalid index'})
    except Exception as e:
        return jsonify({'status': 'failure', 'message': str(e)})


if __name__ == "__main__":
    app.run(debug=True)