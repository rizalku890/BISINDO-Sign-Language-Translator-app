
"""
Copyright by
| Alvin Sengkey
| 001202000115
| President University
| Faculty of Computing
| Major of Informatics
| MAY 2023

"""

from flask import (
    Flask,
    Response,
    render_template,
    url_for,
)

from detection import doDetection


app = Flask(__name__)


# TRANSLATION ARRAY
translation = []
complete_trans = []


def gen_frames(cam):
    while True:
        data = cam.get_frame()
        frame = data[0]
        yield (
            b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
        )  # concat frame one by one and show result



@app.route("/detection-result")
def show_result():
    result_info = doDetection.get_result()
    result = result_info[0]
    translation.append(result)
    trans_str = "".join(translation)
    comp_trans_str = " ".join(complete_trans)
    print("Translation - show_result: ", trans_str)
    return render_template(
        "index.html",
        show_translation=trans_str,
        visibility="visible",
        show_complete_trans=comp_trans_str,
    )


@app.route("/detection-result-delete")
def delete():
    str_length = len(translation)
    if str_length > 0:
        del translation[-1]
    trans_str = "".join(translation)
    comp_trans_str = " ".join(complete_trans)
    print("Translation - delete: ", trans_str)
    return render_template(
        "index.html",
        show_translation=trans_str,
        visibility="visible",
        show_complete_trans=comp_trans_str,
    )


@app.route("/detection-result-reset")
def reset():
    global translation
    translation = []
    trans_str = "".join(translation)
    comp_trans_str = " ".join(complete_trans)
    print("Translation - reset: ", trans_str)
    return render_template(
        "index.html",
        show_translation="*prediction result*",
        visibility="hidden",
        show_complete_trans=comp_trans_str,
    )


@app.route("/save-detection-result")
def save_result():
    global translation
    trans_str = "".join(translation)
    complete_trans.append(trans_str)
    comp_trans_str = " ".join(complete_trans)
    translation = []
    print("Complete_Trans - save_result: ", comp_trans_str)
    return render_template(
        "index.html",
        show_translation="*prediction result*",
        visibility="hidden",
        show_complete_trans=comp_trans_str,
    )


@app.route("/delete-all-translation")
def x_reset():
    global translation
    global complete_trans
    complete_trans = []
    trans_str = "".join(translation)
    comp_trans_str = "".join(complete_trans)
    return render_template(
        "index.html",
        show_translation=trans_str,
        visibility="visible",
        show_complete_trans=comp_trans_str,
    )


@app.route("/video_feed")
def video_feed():
    return Response(
        gen_frames(doDetection()), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/")
def index():
    return render_template(
        "index.html", 
        show_translation="*prediction result*", visibility="hidden"
    )


@app.route("/switch")
def indexSwitch():
    return render_template(
        "indexSwitch.html"
    )


@app.route("/hand-sign-list")
def sign_list_page():
    return render_template(
        "handSignList.html"
    )


if __name__ == "__main__":
    app.run(debug=True)
