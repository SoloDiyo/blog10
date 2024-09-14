from flask import Flask as F, render_template as rt, request as r

app = F(__name__, template_folder="templates")


@app.route('/')
def home():
    h = open('head.txt', mode='r')
    s = open('story.txt', mode='r')
    if h.read() == '' and s.read() == '':
        return rt('no.html')
    else:
        return rt('index.html',heading=h.read(), story=s.read())


@app.route('/addstory', methods=["POST", "GET"])
def addStory():
    if r.method == "POST":
        name = r.form['name']
        heading = r.form['email']
        story = r.form['story']
        h = open('head.txt', mode='w')
        s = open('story.txt', mode='w')
        h.write(heading)
        s.write(story)
        return "Thank You go to Home Page"
    else:
        return rt('add.html')


if __name__ == "__main__":
    app.run(debug=True)
