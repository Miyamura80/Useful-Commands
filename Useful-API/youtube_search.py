import requests
import re
from bs4 import BeautifulSoup


def get_page_reading_time(url: int) -> int:
    page = requests.get("https://klopets.com/readtime/?url={}".format(url))
    soup = BeautifulSoup(page.content, "html.parser")
    result_by_id = soup.find("p")
    if result_by_id != None:
        time_read = re.findall('[0-9]+' ,result_by_id.text)
        time_read_minutes = int(time_read[0])
        return time_read_minutes
    else:
        return 0

if __name__=="__main__":
    print(get_page_reading_time("https://medium.com/@Relay_Chain/the-relay-bridge-how-does-it-works-d46ee1c795b3"))
