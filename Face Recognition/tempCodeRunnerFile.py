

class Users(db.Model):
    username = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session.pop('name', None)
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(username=username).first()
        print(user)
        if user is not None and user.password == password:
            session['name'] = user.name # store variable in session
            detected_name, label_name = recognition_liveness('face_recognition_and_liveness/face_liveness_detection/liveness.model',
                                                    'face_recognition_and_liveness/face_liveness_detection/label_encoder.pickle',
                                                    'face_recognition_and_liveness/face_liveness_detection/face_detector',
                                                    'face_recognition_and_liveness/face_recognition/encoded_faces.pickle',
                                                    confidence=0.5)
            if user.name == detected_name and label_name == 'real':
                return redirect(url_for('main'))
            else:
                return render_template('login_page.html', invalid_user=True, username=username)
        else:
            return render_template('login_page.html', incorrect=True)

    return render_template('login_page.html')

@app.route('/main', methods=['GET'])
def main():
    name = session['name']
    return render_template('main_page.html', name=name)

if __name__ == '__main__':
    db.create_all()

    # add users to database

    #new_user = Users(username='rajit_tete', password='123456789', name='Rajit')
    #db.session.add(new_user)
    app.run(debug=True)