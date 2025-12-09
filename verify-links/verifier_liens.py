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
    "https://www.youtube.com/watch?v=LDgR8ffFzBo",
    "https://youtu.be/2YaFRe9DdUo",
    "https://youtu.be/jMXVgR8W1Mk",
    "https://www.youtube.com/watch?v=Y2EaevkTn1E",
    "https://www.youtube.com/watch?v=gUOQ9baRLUI",
    "https://www.youtube.com/watch?v=aCY3qnFvEXo",
    "https://youtu.be/9w1zh9fnmXg",
    "https://youtu.be/-ekmFySat9s",
    "https://youtu.be/LCMwHhYMxJE",
    "https://youtu.be/qZXaQ79hy9E",
    "https://www.youtube.com/watch?v=5e4OFhFmvH4",
    "https://www.youtube.com/watch?v=uLU6Ias-Au8",
    "https://www.youtube.com/watch?v=RvxiFg_2P-M",
    "https://www.youtube.com/watch?v=gzwlmzAkNb0",
    "https://www.youtube.com/watch?v=O1Zz75rYp6s",
    "https://www.youtube.com/watch?v=Q0Rz7vKqKXc",
    "https://www.youtube.com/watch?v=qSPbpoNb4A4",
    "https://aventura-costarica.com/coati-du-costa-rica/",
    "https://www.youtube.com/watch?v=mJUuAoKRy0g",
    "https://www.youtube.com/watch?v=vpHwGI4rt1w",
    "https://www.youtube.com/watch?v=p2ffAEdKqPI",
    "https://www.youtube.com/watch?v=Lgyf3EUnpSM",
    "https://www.youtube.com/watch?v=QeUWtfKiX9s",
    "https://www.youtube.com/watch?v=RvNEXSl24tI",
    "https://www.youtube.com/watch?v=VO2QzRF7P7Q"
]

# Affichage des résultats
if __name__ == "__main__":
    resultats = verifier_liens(liens_a_verifier)
    for lien, statut in resultats.items():
        print(f"{lien} : {statut}")
