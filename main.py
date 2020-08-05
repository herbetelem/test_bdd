#coding:utf-8

# import de la librairie que vas gerer le sql
import sqlite3

# ! Connection a la bdd
connection = sqlite3.connect("via_promo.db")
# ! instance du curseur
cursor = connection.cursor()

# # ! CREATE << a decommenter pour tester >>
# # ! -----------------------------------------------------------------------------------------------------------------------------------------
# # ! lastrowid recupere la dernier id, ensuite on rentre le nom et l'age choisi' grace a des input (ou autre)
# new_user_name = input("Choisissez le nouveau nom a mettre dans la bdd : ")
# new_user_age = int(input("Choisissez son age : "))
# new_user = (cursor.lastrowid, new_user_name, new_user_age)
# # ! on créer la requette qui vas ajouter un user, en mettant en argument un tuple créer precedement
# cursor.execute('INSERT INTO via_promo VALUES(?,?,?)', new_user)
# # ! pour add qlq chose dans la bd il faud le push comme un git
# connection.commit()
# # ! -----------------------------------------------------------------------------------------------------------------------------------------


# # ! READ ONE LINE << à decommenter pour tester >>
# # ! -----------------------------------------------------------------------------------------------------------------------------------------
# # ! je demande quel noms je dois chercher dans la bdd, et comme le format doit etre un tuple je la formate pour correspondre a ce format
# my_name = (input("qui recherchez vous : "),)
# cursor.execute('SELECT * FROM via_promo WHERE promo_name = ?', my_name)

# # ! je recupere au format de une seul ligne le nom trouvé
# result = cursor.fetchone()[1]

# print("Select UNE personne :")
# print(f"la personne {result} est bien dans la bdd")
# # ! -----------------------------------------------------------------------------------------------------------------------------------------

# # ! READ MULTI LINE << à decommenter pour tester >>
# # ! -----------------------------------------------------------------------------------------------------------------------------------------
# # ! je créer la requette qui vas recuperer uniquement les noms depuis la table via_promo car je ne selectionne pas * (* = all)
# cursor.execute('SELECT name FROM via_promo')

# result = cursor.fetchall()

# print("Select PLUSIEURS personnes :")
# for user in result:
#     print(f"la personne {user[0]} est bien dans la bdd")
# # ! -----------------------------------------------------------------------------------------------------------------------------------------


# # ! DELETE << à decommenter pour tester >>
# # ! -----------------------------------------------------------------------------------------------------------------------------------------
# # ! je demande quel noms je dois supprimer dans la bdd, et comme le format doit etre un tuple je la formate pour correspondre a ce format
# my_name = (input("qui voulez vous supprimer : "),)
# cursor.execute('DELETE FROM via_promo WHERE name = ?', my_name)
# # ! pour delete qlq chose dans la bd il faud le push comme un git
# connection.commit()
# # ! -----------------------------------------------------------------------------------------------------------------------------------------


# ! On doit TOUJOURS fermer une bdd mais a la fin du code
connection.close()