# CeneoScrapperN11
## Etap 1 - Pobranie składowych pojedynczej opinii o wyranym produkcie z serwisu [Ceneo.pl](https://www.ceneo.pl/)
* Pobranie kodu pojedynczej strony z opiniami o wskazanym produkcie
* Analiza kodu HTML pojedynczej opinii

|Składowa opinii|Celektor CSS|Nazwa zmiennej|Typ danych|
|:--------------|:-----------|:-------------|:---------|
|Opinia|`div.js_product-review`|review|dict|
|Identyfikator opinii|`["data-entry-id"]`|review_id|str|
|Autor|`span.user-post__author-name`|author|str|
|Rekomendacja|`span.user-post__author-recomendation`|recommendation|bool|
|Liczba gwiazdek|`span.user-post__score-count`|stars|float|
|Treść|`div.user-post__text`|content|str|
|Lista zalet|`review-feature__col:has(> div.review-feature__title--positives) > review-feature__item` <br> `review-feature__col:has(> div[class*="positives") > review-feature__item` <br> `div.review-feature__title--positives ~ review-feature__item`|pros|\[str\]|
|Lista wad|`review-feature__col:has(> div.review-feature__title--negatives) > review-feature__item` <br> `review-feature__col:has(> div[class*="negatives") > review-feature__item` <br> `div.review-feature__title--negatives ~ review-feature__item`|cons|\[str\]|
|Dla ilu osób użyteczna|`span[id^="votes-yes"]` <br> `button.vote-yes > span` <br> `button.vote-yes["data-total-vote"]`|useful|int|
|Dla ilu osób nieużyteczna|`span[id^="votes-no"]` <br> `button.vote-no > span` <br> `button.vote-no["data-total-vote"]`|useless|int|
|Czy opinia potwierdzona zakupem|`div.review-pz`|purchased|bool|
|Data wystawienia opinii|`span.user-post__published > time:nth-child(1)["datetime"]`|review_date|str|
|Data zakupu produktu|`span.user-post__published > time:nth-child(2)["datetime"]`|purchase_date|str|

3. Pobieranie składowych opinii do pojedynczych zmiennych
