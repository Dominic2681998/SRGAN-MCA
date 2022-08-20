from flask import Flask,render_template,request
app = Flask(__name__,template_folder='templates',static_url_path='/static')
import classifier as cl
from keras.preprocessing import image
from werkzeug.utils import secure_filename

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def home():
    #cl.model_load()
    return render_template('home.html')

@app.route('/result', methods=['GET','POST'])
def result():

    if request.method == 'POST':

        image = request.files["pic"]
        image.save("static/uploads/"+secure_filename(image.filename))
        result = cl.classify(secure_filename(image.filename))     
        if result:
            return render_template('result.html',cd = '../static/result/'+secure_filename(image.filename) )

if __name__ == "__main__":
    app.run(debug=True)