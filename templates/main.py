from flask import Flask, render_template

app = Flask(__name__)

@app.route('/FizzBuzz')
def fizzbuzz():
    FizzBuzz_data = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            FizzBuzz_data.append('FizzBuzz')
        elif i % 3 == 0:
            FizzBuzz_data.append('Fizz')
        elif i % 5 == 0:
            FizzBuzz_data.append('Buzz')
        else:
            FizzBuzz_data.append(i)
    
    return render_template('FizzBuzz.html', FizzBuzz_data=FizzBuzz_data)

if __name__ == '__main__':
    app.run(debug=True)
