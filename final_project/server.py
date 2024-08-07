'''  import work modules  '''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
'''  fun d.s  ''' 
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
'''  fun d.s  ''' 
    if request.method == 'POST':
        statement = request.form.get('statement')
        result = emotion_detector(statement)
        if result['dominant_emotion'] is None:
            print("Invalid text! Please try again.")
        else:
            return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
