#coding:utf-8
"""
Opérateur de comparaison : == (égal a)
						   != (différent de)
						   < (Inferieur a)
						   > (Superieur a)
						   <=(Inferieur ou égal a)
						   >=(Superieur ou égal )

Mot clés des conditions : if / elif / else

Conditions multiples	 : and (ET)
						   or (OU)
						   in / not in (DANS / PAS DANS)
"""

identifiant = "Jason"
mot_de_passe = "987"

print("Interface Utilisateur")

user_id = input("Entrer votre identifiant : ")
user_password = input("Entrer votre mot de passe : ")

if user_id == identifiant and user_password == mot_de_passe:
	print("Vous êtes connectés. Bienvenue", user_id)
elif user_id != identifiant and user_password == mot_de_passe:
	print("L'identifiant est incorrecte.")
elif user_password != mot_de_passe and user_id == identifiant:
	print("Le mot de passe est incorrecte.")
else:
	print("Le mot de passe et l'identifiant sont incorrectes.")
