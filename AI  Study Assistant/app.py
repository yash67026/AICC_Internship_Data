from flask import Flask, render_template, request
import google.generativeai as genai
import markdown

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ""
    user_question = ""
    
    if request.method == 'POST':
        api_key = request.form.get('api_key')
        user_question = request.form.get('question')
        
        if api_key and user_question:
            try:
                genai.configure(api_key=api_key)
                # Using the stable 2.5 series for April 2026
                model = genai.GenerativeModel('gemini-2.5-flash')
                response = model.generate_content(user_question)
                
                # CONVERSION STEP: This turns **Title** into <b>Title</b>
                raw_text = response.text
                answer = markdown.markdown(raw_text)
                
            except Exception as e:
                answer = f"Error: {str(e)}"
                
    return render_template('index.html', answer=answer, question=user_question)

if __name__ == '__main__':
    app.run(debug=True)