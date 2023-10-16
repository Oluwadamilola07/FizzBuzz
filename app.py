from flask import Flask, render_template

app = Flask(__name__)

@app.route('/fizzbuzz')
def FizzBuzz():
    fizzbuzz_data = []
        
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz_data.append('FizzBuzz')
        elif i % 3 == 0:
            fizzbuzz_data.append('Fizz')
        elif i % 5 == 0:
            fizzbuzz_data.append('Buzz')
        else:
            fizzbuzz_data.append(i)
    
    return render_template('fizzbuzz.html', fizzbuzz_data=fizzbuzz_data)


if __name__ == '__main__':
    app.run(debug=True)
