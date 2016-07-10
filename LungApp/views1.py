from LungApp import app
from flask import Flask, request, redirect, url_for, send_from_directory, render_template


# def allowed_file(filename):
# 	return '.' in filename and \
# 		filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
# 	if request.method == 'POST':
# 		# Check if the post request has the file part
# 		if 'file' not in request.files:
# 			flash('No file in part')
# 			return redirect(request.url)
# 		file = request.files['file']
# 		# if user does not select file, browser also
# 		# submit a empty part without filename
# 		if file.filename == '':
# 			flash('No selected file')
# 			return redirect(request.url)
# 		if file and allowed_file(file.filename):
# 			filename = secure_filename(file.filename)
# 			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
# 			return redirect(url_for('uploaded_file',filename=filename))
# 	return render_template('upload.html')

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
# 	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
@app.route('/index')#, methods=['GET', 'POST'])
def index(name=None):
	return render_template('index.html')
    # if flask.request.method == 'GET':
    # return 'Hello??'#render_template('index.html', name=name)

    # email = flask.request.form['email']
    # if flask.request.form['pw'] == users[email]['pw']:
    #     user = User()
    #     user.id = email
    #     flask_login.login_user(user)
    #     return flask.redirect(flask.url_for('protected'))

    # return 'Bad login'
