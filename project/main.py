from flask import Flask,render_template,request
app = Flask(__name__,static_folder='static')
import classifier as cl
from keras.preprocessing.image import load_img

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
        image.save("static/uploads/"+image.filename)
        print(image.filename)
        result = cl.classify(image.filename)  
       
        if result:
            #img =load_img("result/"+image.filename)
            print(image.filename)
            
            return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)