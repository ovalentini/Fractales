import requests

def verifier_liens(liens_a_verifier):
    resultat = {}
    for url in liens_a_verifier:
        try:
            reponse = requests.get(url, allow_redirects=True, timeout=5)
            statut = reponse.status_code
            contenu = reponse.text.lower()
            if "cette vidéo n'est plus disponible" in contenu or "video unavailable" in contenu:
                resultat[url] = "Inactif ❌ (vidéo indisponible)"
            else:
                actif = 200 <= statut < 400
                resultat[url] = "Actif ✅" if actif else f"Inactif ❌ (code {statut})"
        except requests.RequestException as e:
            resultat[url] = f"Inactif ❌ (erreur : {e})"
    return resultat

# Liste des liens à vérifier
liens = {
    "Inde (Hampi)": [
        "https://www.youtube.com/watch?v=UOFoQ70m6Z8",
        "https://www.youtube.com/watch?v=ChchmDc_OhI",
        "https://www.youtube.com/watch?v=tMjVqBzSnGs",
    ],
    "Bali": [
        "https://www.routard.com/fr/photo/p/345-bali",
        "https://www.visitonsbali.com/photos",
        "https://www.okvoyage.com/post/paysages-bali/",
    ],
    "Flores": [
        "https://munki.audio/catalogue/albums/410/artistes-divers--comptines-et-berceuses-des-rizieres",
        "https://soundcloud.com/julien-boulier/episodes-rizieres-by-julien",
        "https://www.youtube.com/watch?v=jKxOceVX9wk",
    ],
    "Perou": [
        "https://www.youtube.com/watch?v=jm4lKVxihI4",  # Vidéo YouTube - musique Pérou
        "https://www.youtube.com/watch?v=go7GM3N6kqY",  # Vidéo YouTube - paysages Pérou
        "https://www.youtube.com/watch?v=LDgR8ffFzBo",  # Vidéo YouTube - danse Pérou
    ],
    "Maurice": [
        "https://youtu.be/2YaFRe9DdUo",                 # Vidéo YouTube courte Maurice
        "https://youtu.be/jMXVgR8W1Mk",                 # Vidéo YouTube courte Maurice
        "https://www.youtube.com/watch?v=Y2EaevkTn1E",  # Vidéo YouTube - musique Maurice
    ],
    "Maldives": [
        "https://www.youtube.com/watch?v=gUOQ9baRLUI",
        "https://www.youtube.com/watch?v=aCY3qnFvEXo",
        "https://youtu.be/9w1zh9fnmXg",
    ],
    "Laos": [
        "https://youtu.be/-ekmFySat9s",
        "https://youtu.be/LCMwHhYMxJE",
        "https://youtu.be/qZXaQ79hy9E",
    ],
    "Californie": [
        "https://www.youtube.com/watch?v=5e4OFhFmvH4",
        "https://www.youtube.com/watch?v=uLU6Ias-Au8",
        "https://www.youtube.com/watch?v=RvxiFg_2P-M",
    ],
    "Costa Rica": [
        "https://www.youtube.com/watch?v=qSPbpoNb4A4",
        "https://aventura-costarica.com/coati-du-costa-rica/",
        "https://www.youtube.com/watch?v=mJUuAoKRy0g",
    ],
    "Dominicaine": [
        "https://www.youtube.com/watch?v=vpHwGI4rt1w",
        "https://www.youtube.com/watch?v=p2ffAEdKqPI",
        "https://www.youtube.com/watch?v=Lgyf3EUnpSM",
    ],
    "Guyane": [
        "https://www.youtube.com/watch?v=QeUWtfKiX9s",
        "https://www.youtube.com/watch?v=RvNEXSl24tI",
        "https://www.youtube.com/watch?v=VO2QzRF7P7Q",
    ],
    "Australie": [
        "https://www.youtube.com/watch?v=gzwlmzAkNb0",
        "https://www.youtube.com/watch?v=O1Zz75rYp6s",
        "https://www.youtube.com/watch?v=t62jpUY0EQU",  # Remplacement du lien cassé
        "https://www.youtube.com/watch?v=Q0Rz7vKqKXc",  # ancien lien cassé
    ]
}

# Vérification par bloc thématique
def verifier_liens_par_bloc(dictionnaire_liens, nom_fichier="resultats.txt"):
    with open(nom_fichier, "w", encoding="utf-8") as f:
        for destination, urls in dictionnaire_liens.items():
            f.write(f"\n--- {destination} ---\n")
            print(f"\n--- {destination} ---")
            resultats = verifier_liens(urls)
            for lien, statut in resultats.items():
                ligne = f"{lien} : {statut}"
                print(ligne)
                f.write(ligne + "\n")

# Exécution principale
if __name__ == "__main__":
    verifier_liens_par_bloc(liens)