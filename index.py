from logging import raiseExceptions
from flask import Flask, render_template, request, redirect
from Remote import remote
from Stack import stack
from wwr import we_work_remote
from save import sv

app = Flask(__name__)
WE_WORK = "https://weworkremotely.com/"
REMOTE = "https://remoteok.io/"
fake_db = {}
# https://weworkremotely.com/
# https: // stackoverflow.com/jobs
# https: // remoteok.io/


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/holycow')
def holycow():
    return "shit"


@app.route('/search')
def find_job():
    job = request.args.get('job')
    # print(job)
    if job not in fake_db:
        STACK_OVER_FLOW = f"https://stackoverflow.com/jobs?q={job}"
        r = remote(job)
        s = stack(job)
        w = we_work_remote(job)
        fake_db[job] = r+s+w
        # print(fake_db)

    return render_template("search.html", jobs=fake_db[job], language=job, length=len(fake_db[job]))


@app.route('/export')
def exp():
    # print(job)

    try:
        language = request.args.get('language')
        if not language:
            raise Exception()
        language = language.lower()
        jobs = fake_db.get(language)
        if not jobs:
            raise Exception()
        sv(jobs, language)
        return f"csv for {language} has been downloaded"
    except:
        return redirect("/")
