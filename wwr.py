from bs4 import BeautifulSoup
import requests


headers = {'Accept-Language': "en-US,en;q=0.9,ko;q=0.8",
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}


def we_work_remote(language):
    jobs = []
    main_url = f"https://weworkremotely.com/remote-jobs/search?term={language}&button="
    find_job_from_url(main_url, jobs)
    return jobs


def find_job_from_url(main_url, jobs):

    init_page = result = requests.get(main_url, headers=headers)
    if init_page.status_code != 200:
        return
    init_page_soup = BeautifulSoup(init_page.text, 'html.parser')
    sections = init_page_soup.findAll("section", {"class": "jobs"})

    for section in sections:
        lis = section.findAll("li", {"class": "feature"})
        for li in lis:
            parent = li.find("a")
            # print(parent)
            link = "https://weworkremotely.com" + parent['href']
            # print(link)
            company = li.find(
                "span", {"class": "company"}).text.strip().replace(",", " ")
            position = li.find(
                "span", {"class": "title"}).text.strip().replace(",", " ")
            jobs.append((company, position, link))
