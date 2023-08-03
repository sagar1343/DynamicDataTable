from flask import Flask,render_template
app=Flask(__name__)
headings=('id','Name','Role')
data=(
        ('1','Shubham','Product manager'),
        ('2', 'Tarun', 'junior developer'),
        ('3', 'Vasu', 'Data engineer'),
        ('4','Sahu','Financial officer'),
        ('5', 'Udit', 'Senior developer'),
        ('6', 'Suryansh', 'Chief executive officer')
    )
@app.route('/')
def table():
    return render_template('_table.html',headings=headings,data=data)
if __name__=='__main__':
    app.run()