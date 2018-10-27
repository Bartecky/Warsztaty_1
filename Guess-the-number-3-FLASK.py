from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def game():
    def guess(min, max):
        return int((max - min) / 2) + min

    def gameform():
        form = """
            <h2>Guess the number game</h2>
            <p>Imagine a number in the range 1-1000, and I'll guess it</p>
            <p>I guess: {} !<br></p>
            <form action='' method='POST'>
                <input type='hidden' name='min' value='{}'>
                <input type='hidden' name='max' value='{}'>
                <input type='hidden' name='bet' value='{}'>
                <input type='submit' name='choice' value='More'>
                <input type='submit' name='choice' value='Less'>
                <input type='submit' name='choice' value='Correct!'>
            </form>
            """.format(bet, min_value, max_value, bet)
        return form

    if request.method == 'GET':
        min_value = 1
        max_value = 1000
        bet = guess(min_value, max_value)
        return gameform()
    elif request.method == 'POST':
        choice = request.form['choice']
        if choice == 'More':
            min_value = int(request.form['bet'])
            max_value = int(request.form['max'])
        elif choice == 'Less':
            min_value = int(request.form['min'])
            max_value = int(request.form['bet'])
        else:
            return """
            <h4>I guessed the number!</h4>
            <input type='button' onclick="location.href='/'" value='Again'>
            """

        bet = guess(min_value, max_value)
        return gameform()


if __name__ == '__main__':
    app.run(debug=True)
