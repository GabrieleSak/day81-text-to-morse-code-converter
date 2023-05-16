"""
Program that takes any String input and converts it into Morse Code
-	Dash (dahs)
.	Dot (dits)
Space	Letter separator
/	Word separator
#	Untranslatable character
"""

from flask import Flask, render_template
from morse_code import *
from forms import InputForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'djhejfwefDGsFaFėįnfsūIKJNūd'


@app.route("/", methods=["GET", "POST"])
def index():
    form = InputForm()
    output = ""
    if form.validate_on_submit():
        string_to_convert = form.input_text.data

        for element in string_to_convert:
            if element == " ":
                code = "/"
            else:
                try:
                    code = morse_code[element.upper()]
                except KeyError:
                    code = "#"
            output += code
            output += " "
        form.output_text.data = output
    return render_template("index.html", form=form, output=output)


if __name__ == "__main__":
    app.run(debug=True)
