import pickle
from flask import Flask,request,render_template
app=Flask(__name__)
model=pickle.load(open('heart.pkl','rb'))
@app.route('/')
def main():
    return render_template('index.html')
@app.route('/heart',methods=['GET','POST'])
def heart():
    data=request.form.values()
    lst=[i for i in data]
    result=model.predict([lst])
    if result[0]==1:
        return render_template('fail.html')
    else:
        return render_template('safe.html')
    

if __name__ == '__main__':
    app.run(debug=True)