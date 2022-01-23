from bs4 import BeautifulSoup
import requests

# https://stackoverflow.com/jobs?q=python&pg=2


def stack(language):
    jobs = []
    main_url = f"https://stackoverflow.com/jobs?q={language}"
    find_job_from_url(main_url, jobs)
    return jobs


def find_job_from_url(main_url, jobs):
    init_page = requests.get(main_url)

    init_page_soup = BeautifulSoup(init_page.text, 'html.parser')
    pagination = init_page_soup.find("div", {"class": "s-pagination"})
    if pagination is None:
        return jobs

    max = int(pagination.findAll("span")[-2].text)

    for idx in range(1, max + 1):
        url = f"{main_url}&pg={idx}"  # 해당 page_url
        # print(url)
        url_page = requests.get(url)
        url_page_soup = BeautifulSoup(url_page.text, 'html.parser')
        listResults = url_page_soup.find("div", {"class": "listResults"}).findAll(
            "div", {"class", "js-result"})
        # print(type(listResults))
        # print(url)
        for listResult in listResults:
            position_link = listResult.find("h2").find("a")
            position = position_link['title'].strip().replace(",", " ")
            company = listResult.find("h3").find(
                "span").text.strip().replace('\n', '').replace(",", " ")
            link = "https://stackoverflow.com" + position_link['href'].strip()
            #print(position, company, link, sep=" || ")
            jobs.append((company, position, link))
