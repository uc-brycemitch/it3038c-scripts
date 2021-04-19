from flask import Flask, render_template, request 

#using the flask app to create a web server
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if request.method == "POST":
    #this is collecting the responses from the form in index
        animal=request.form.get('animal')
        country=request.form.get('country')
        pluralNoun=request.form.get('pluralNoun')
        food=request.form.get('food')
        screen=request.form.get('screen')
        noun=request.form.get('noun')
        verb=request.form.get('verb')
        verb2=request.form.get('verb2')
        adjective=request.form.get('adjective')
        #the data is returned within the story
        return "The majestic " + animal + " has roamed the forests of " + country + " for thousands of years. Today, she wanders in search of " + pluralNoun + ". She must find food to survive. While hunting for " + food + ", she found a/an " + screen + " hidden behind a " + noun + ". She has never seen anything like this before. What will she do? With the device between her teeth, she tries to " + verb + ", but nothing happens. She takes it back to her family. When her family sees it, they quickly " + verb2 + ". Soon, the device becomes " + adjective + ", and the family decides to put it back where they found it."
       
  
    #the story is outputted to the welcome.html page
    return render_template("welcome.html")



app.run(debug=True, port=5000, host='0.0.0.0')

