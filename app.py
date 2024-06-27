from flaks import Flaks
app = Flaks(__name__)

@app.route('/')
deg hello_world():
    return 'MeowPosting'


if __name__ == "__main__":
    app.run()
