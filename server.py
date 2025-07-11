from flask import Flask, render_template, request
from emotion_detection.emotion_detection import emotion_detector
import json

app = Flask("emotionDetector")

@app.route("/")
def index():
    """ root """
    return render_template("index.html")

#@app.errorhandler(400)
#def empyty(error):
#    empty_dict = {"anger":None, "disgust":None, "fear":None, "joy":None, "sadness":None, "dominant_emotion":None}
#   return empty_dict, 400

@app.route('/emotionDetector', methods=["GET"])
def emotion_detector_caller():
  
    text_to_analyze = request.args["textToAnalyze"]
    result = emotion_detector(text_to_analyze)
     
    if result["dominant_emotion"] == None:
        return "Invalid text! Please try again!"
       
    result_str = json.dumps(result)
    
    formatted_result = "For the given statement, the system response is " + result_str + " The dominant emotion is " + result["dominant_emotion"] + '.'
    formatted_result = formatted_result.replace("{", "")
    formatted_result = formatted_result.replace("}", '')
    formatted_result = formatted_result.replace('"', "'")

    return formatted_result

if __name__ == "__main__":
    app.run(debug = True)