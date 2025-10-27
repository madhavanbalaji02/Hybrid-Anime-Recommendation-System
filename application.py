from flask import Flask,render_template,request
from pipeline.prediction_pipeline import hybrid_recommendation

app = Flask(__name__)

@app.route('/' , methods=['GET','POST'])
def home():
    recommendations = None

    if request.method == 'POST':
        try:
            user_id = int(request.form["userID"])

            recommendations = hybrid_recommendation(user_id)
        except Exception as e:
            print("Erorr occured....")

    return render_template('index.html' , recommendations=recommendations)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5001))  # defaults to 5001 if not set
    app.run(debug=True, port=port)