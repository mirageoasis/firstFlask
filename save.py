

def sv(jobs, language):
    loc = f"{language}.csv"
    f = open(loc, 'w')
    for job in jobs:
        word = ",".join(job)
        f.write(word + "\n")
    f.close()
