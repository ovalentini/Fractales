import requests

def verifier_liens(liste_liens):
    resultat = {}
    for url in liste_liens:
        try:
            reponse = requests.head(url, allow_redirects=True, timeout=5)
            statut = reponse.status_code
            actif = 200 <= statut < 400
            resultat[url] = "Actif ✅" if actif else f"Inactif ❌ (code {statut})"
        except requests.RequestException as e:
            resultat[url] = f"Inactif ❌ (erreur : {e})"
    return resultat

# Liste des liens à vérifier
liens_a_verifier = [
    "https://www.youtube.com/watch?v=UOFoQ70m6Z8",
    "https://www.youtube.com/watch?v=ChchmDc_OhI",
    "https://www.youtube.com/watch?v=tMjVqBzSnGs",
    "https://www.routard.com/fr/photo/p/345-bali",
    "https://www.visitonsbali.com/photos",
    "https://www.okvoyage.com/post/paysages-bali/",
    "https://munki.audio/catalogue/albums/410/artistes-divers--comptines-et-berceuses-des-rizieres",
    "https://soundcloud.com/julien-boulier/episodes-rizieres-by-julien",
    "https://www.youtube.com/watch?v=jKxOceVX9wk",
    "https://www.youtube.com/watch?v=jm4lKVxihI4",
    "https://www.youtube.com/watch?v=go7GM3N6kqY",
    "https://www.youtube.com/watch?v=LDgR8ffFzBo"
]

# Affichage des résultats
if __name__ == "__main__":
    resultats = verifier_liens(liens_a_verifier)
    for lien, statut in resultats.items():
        print(f"{lien} : {statut}")
