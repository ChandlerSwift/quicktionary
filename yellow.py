import wikipedia


def collect_links_from_wikipedia_page(s):
    for link in wikipedia.page(s).links:
        if ' ' not in link and link.upper() != link:
            yield link


# def y1():
#     """Associated with computers"""
#     return collect_links_from_wikipedia_page("computer")

# def y2():
#     """Associated with transportation"""
#     return collect_links_from_wikipedia_page("transportation")

# def y3():
#     """Associated with space"""
#     return collect_links_from_wikipedia_page("Outer space")

# def y4():
#     """Associated with politics"""
#     return collect_links_from_wikipedia_page("politics")

# def y5():
#     """Associated with beach"""
#     return collect_links_from_wikipedia_page("beach")

# def y6():
#     """Associated with time"""
#     return collect_links_from_wikipedia_page("time")

# def y7():
#     """Associated with literature"""
#     return collect_links_from_wikipedia_page("literature")

# def y8():
#     """Associated with music"""
#     return collect_links_from_wikipedia_page("music")

# def y9():
#     """Associated with crime"""
#     return collect_links_from_wikipedia_page("crime")

# def y10():
#     """Associated with vacation"""
#     return collect_links_from_wikipedia_page("vacation")

# def y11():
#     """Associated with art"""
#     return collect_links_from_wikipedia_page("art")

# def y12():
#     """Associated with school"""
#     return collect_links_from_wikipedia_page("school")

# def y13():
#     """Associated with sports"""
#     return collect_links_from_wikipedia_page("sports")

# def y14():
#     """Associated with love"""
#     return collect_links_from_wikipedia_page("love")

# def y15():
#     """Associated with money"""
#     return collect_links_from_wikipedia_page("money")

# def y16():
#     """Associated with family"""
#     return collect_links_from_wikipedia_page("family")

# def y17():
#     """Associated with math"""
#     return collect_links_from_wikipedia_page("math")

# def y18():
#     """Associated with parties"""
#     return collect_links_from_wikipedia_page("parties")

# def y19():
#     """Associated with the human body"""
#     return collect_links_from_wikipedia_page("human body")

# def y20():
#     """Associated with weather"""
#     return collect_links_from_wikipedia_page("weather")

# def y21():
#     """Associated with science"""
#     return collect_links_from_wikipedia_page("science")

def y22():
    """A type of plant"""
    return collect_links_from_wikipedia_page("List of plants by common name")