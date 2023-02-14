import spacy
nlp = spacy.load('en_core_web_md')
# read in the movies.txt file and the Planet Hulk description,
movies = open("movies.txt", 'r', encoding='utf-8')
planetHulk = nlp("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.")
# define the function,
def mostSimilar(description):
    listStore = list()
    for line in movies:
        line = line.replace('\ufeff','')
        line = line.replace('\n', '')
        movieName = line[0:8]
        movieDesc = line[9:]
        nlpMovieDesc = nlp(movieDesc)
        similarityScore = planetHulk.similarity(nlpMovieDesc)
        listStore.append({"Name" : movieName,"Similarity" : similarityScore})
    movies.close()
    similarityScore = sorted(listStore, key = lambda d: d["Similarity"], reverse=True)
    return similarityScore[0].get("Name")
print("The movies with the the closest similarity to planet hulk is {}.".format(mostSimilar(planetHulk)))