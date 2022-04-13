# Web Scraping

Use beautifulsoup whenever possible - faster & better designed, but only works for static sites. Selenium better for performing user operations, using drivers.

# Beautifulsoup

<details>
  <summary> ✨ BeautifulSoup </summary>
  
  ```python
  import requests
  from bs4 import BeautifulSoup
  
  URL = ""
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
    
  result_by_id = soup.find("a", id="entry-inner")
  result_by_string_content = soup.find("h2", string=lambda text: "python" in text.lower())
  grab_parent = result_by_id.parent
  grab_href = result_by_id["href"]
  job_elements = results.find_all("div", class_="card-content") #iterable

  print(result.prettify())
  
  ```
  
  Saving:
  ```python
  with open("file.html", "w", encoding='utf-8') as f:
      f.write(page.text)
  ```
  
</details>


# Selenium 

<details>
  <summary> 👗 Selenium </summary>
  
  ```python
  
  ```
  
  
  
</details>
