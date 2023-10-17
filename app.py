from flask import Flask, render_template

app = Flask(__name__)

@app.route('/fizzbuzz')
def FizzBuzz():
    fizzbuzz = []
        
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz.append('FizzBuzz')
        elif i % 3 == 0:
            fizzbuzz.append('Fizz')
        elif i % 5 == 0:
            fizzbuzz.append('Buzz')
        else:
            fizzbuzz.append(i)
    
    return render_template('fizzbuzz.html', fizzbuzz=fizzbuzz)


if __name__ == '__main__':
    app.run(debug=True)
