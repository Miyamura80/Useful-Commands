# WikiData

TLDR: WikiData has **Entities (Q numbers)** and **Properties (P numbers)** and can query based on those

# Quick Start

Write SQL-esk query, SPARQL at https://query.wikidata.org
The site can also generate code for JS, Python, Java, Perl, R, Ruby, Matlab, etc

# Get aliases
<details>

  ```sparql
  #Machine Learning
  SELECT ?item ?itemLabel ?itemAltLabel
  WHERE 
  {
    ?item wdt:P279 wd:Q2539. # Must be subclass (P279) of neural network (Q2539)
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". } # Helps get the label in your language, if not, then en language
  }
  ```

</details>
