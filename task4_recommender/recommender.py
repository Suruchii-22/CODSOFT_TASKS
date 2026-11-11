"""Task 4: Content-based movie recommender (TF-IDF + cosine similarity, pure Python)."""
import math
from collections import Counter

MOVIES = {
    # Sci-Fi / Action / Cyberpunk
    "The Matrix": "sci-fi action cyberpunk hacker simulation reality keanu reeves",
    "Inception": "sci-fi thriller dreams heist mind-bending christopher nolan",
    "Interstellar": "sci-fi space drama time gravity family nolan",
    "Blade Runner 2049": "sci-fi cyberpunk dystopia noir future detective",
    "The Dark Knight": "action crime superhero thriller gotham batman",
    "Avengers: Endgame": "action superhero sci-fi team epic marvel universe",
    "Spider-Man: Into the Spider-Verse": "animation action superhero multiverse comedy comic",
    # Animation & Family
    "Toy Story": "animation family adventure toys comedy pixar friendship",
    "Finding Nemo": "animation family adventure ocean fish comedy pixar",
    "Spirited Away": "animation fantasy adventure magic spirits anime studio ghibli",
    "The Lion King": "animation drama adventure royalty family animals musical",
    # Romance & Drama
    "The Notebook": "romance drama love emotional Nicholas Sparks destiny",
    "Titanic": "romance drama ship tragedy historical love disaster",
    "La La Land": "romance musical drama dreams hollywood jazz bittersweet",
    # Comedy / Friendship / Coming-of-Age
    "3 Idiots": "comedy drama college engineering friendship india dreams",
    "Zindagi Na Milegi Dobara": "comedy drama friendship travel road-trip spain self-discovery",
    "The Grand Budapest Hotel": "comedy drama quirky aesthetic heist friendship wes anderson",
    # Crime / Thriller / Mystery
    "Parasite": "thriller drama class society dark-comedy korean satire oscar",
    "Pulp Fiction": "crime thriller dark-comedy cult nonlinear mob tarantino",
    "Fight Club": "psychological thriller mystery rebellion identity underground",
    "Shutter Island": "psychological thriller mystery asylum mind-bending detective",
    # Horror & Supernatural
    "The Conjuring": "horror supernatural paranormal thriller haunted demons investigation",
    "A Quiet Place": "horror sci-fi suspense monsters family survival tension",
    # Sports & Biopic
    "Dangal": "drama sports wrestling family india biopic empowerment",
    "Whiplash": "drama music psychological obsession jazz competition passion",
}


def tokenize(text):
    return text.lower().split()


def build_tfidf(docs):
    n = len(docs)
    # df: document frequency of each token across the entire corpus
    df = Counter(t for d in docs.values() for t in set(tokenize(d)))
    # idf: smooth inverse document frequency: log((1 + N)/(1 + df)) + 1
    idf = {t: math.log((1 + n) / (1 + c)) + 1 for t, c in df.items()}
    vecs = {}
    for name, d in docs.items():
        toks = tokenize(d)
        tf = Counter(toks)
        # tf-idf = (term_count / doc_len) * idf
        vecs[name] = {t: (c / len(toks)) * idf[t] for t, c in tf.items()}
    return vecs


def cosine(a, b):
    dot = sum(a[t] * b[t] for t in a if t in b)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0


VECS = build_tfidf(MOVIES)


def resolve_title(user_input):
    """Case-insensitive and partial match against movie titles."""
    query = user_input.strip().lower()
    if not query:
        return None
    # Exact match (case-insensitive)
    for title in MOVIES:
        if title.lower() == query:
            return title
    # Substring match
    for title in MOVIES:
        if query in title.lower():
            return title
    return None


def recommend(liked_titles, k=3):
    """Average the liked movies' TF-IDF vectors into a user profile, rank the rest."""
    resolved = []
    for item in liked_titles:
        match = resolve_title(item)
        if match and match not in resolved:
            resolved.append(match)

    if not resolved:
        return [], []

    profile = Counter()
    for m in resolved:
        for t, v in VECS[m].items():
            profile[t] += v / len(resolved)

    scores = [(m, cosine(profile, v)) for m, v in VECS.items() if m not in resolved]
    scores.sort(key=lambda x: -x[1])
    return resolved, scores[:k]


def main():
    print("=" * 60)
    print("CodSoft AI - Content-Based Movie Recommender")
    print("=" * 60)
    print("Available movies in database:")
    for title in sorted(MOVIES):
        print(f"  • {title}")
    print("=" * 60)

    raw = input("\nEnter movies you liked (comma separated, e.g., 'Matrix, Inception'): ")
    liked_inputs = [x.strip() for x in raw.split(",") if x.strip()]
    resolved, recs = recommend(liked_inputs)

    if not resolved:
        print("\n[!] No matching movies found. Please check spelling against the catalog above.")
        return

    print(f"\nMatched your input to: {', '.join(resolved)}")
    print("\nTop Recommendations:")
    for rank, (m, score) in enumerate(recs, 1):
        tags = MOVIES[m]
        print(f"  {rank}. {m} (Similarity: {score * 100:.1f}%)")
        print(f"     Key features: {tags}\n")


if __name__ == "__main__":
    main()
