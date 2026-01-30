from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

LANGUAGES = {
    'en': 'English',
    'hi': 'Hindi',
    'te': 'Telugu',
    'ta': 'Tamil',
    'kn': 'Kannada',
    'ml': 'Malayalam',
    'mr': 'Marathi',
    'ur': 'Urdu',
    'fr': 'French',
    'de': 'German',
    'es': 'Spanish'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ''
    input_text = ''
    src_lang = 'en'
    dest_lang = 'hi'

    if request.method == 'POST':
        input_text = request.form['input_text']
        src_lang = request.form['src_lang']
        dest_lang = request.form['dest_lang']

        output = GoogleTranslator(
            source=src_lang,
            target=dest_lang
        ).translate(input_text)

    return render_template(
        'index.html',
        output=output,
        input_text=input_text,
        src_lang=src_lang,
        dest_lang=dest_lang,
        languages=LANGUAGES
    )

if __name__ == '__main__':
    app.run(debug=True)
