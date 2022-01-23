from bs4 import BeautifulSoup
import requests


headers = {'Accept-Language': "en-US,en;q=0.9,ko;q=0.8",
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
# https://stackoverflow.com/jobs?q=python&pg=2


def remote(language):
    main_url = f"https://remoteok.com/remote-{language}-jobs"
    jobs = []
    find_job_from_url(main_url, jobs)
    return jobs


def find_job_from_url(main_url, jobs):

    init_page = result = requests.get(main_url, headers=headers)
    if init_page.status_code != 200:
        return

    init_page_soup = BeautifulSoup(init_page.text, 'html.parser')
    charts = init_page_soup.find(
        "div", {"class": "page"}).find("table").findAll("tr", {"class": "job"})

    # print(init_page_soup)
    # print(charts)
    for job in charts:
        temp = job.find("td", {"class": "company"})
        company = temp.find("h3").text.strip().replace(",", " ")
        position = temp.find("a").text.strip().replace(",", " ")
        link = "https://remoteok.com" + temp.find("a")['href'].strip()
        jobs.append((company, position, link))
