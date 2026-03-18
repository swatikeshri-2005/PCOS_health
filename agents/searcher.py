from duckduckgo_search import DDGS # type: ignore

def search_web(query, num_results=8):
    links = []
    
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=num_results)
            
            for result in results:
                if "href" in result:
                    links.append(result["href"])
    
    except Exception as e:
        print("Search error:", e)

    return links