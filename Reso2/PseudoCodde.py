


def Globalloop(pathparking,pathdemand):

    creation du dictionaire de demande (fichier csv)
    depoupage du temps à partir de la demande (fichier csv)
    création du parking et des places de swap (fichier csv)
    création des robots(nombre, temps d'initialisation)

    pour chaque point du découpage du temps:

        récupération du typė d'action(liste demande, pas de temps)
        récupération de l'identité du client concerné(liste demande, pas de temps)


        if si arrivee:

            (parkspot,nextime)=give_place(parking,swapavailable,orderlist,tf,identity,customers[identity][0],customers[identity][1])
            simulation de l'arrivee du client (choix de la place et temps d'attente)

            choix de la place a l'intérieur du parking.

            création d'un ordre de déplacement et ajout de celui-ci dans la liste des taches.

            répartition des teches aux différents robots.


        if si depart:

            récupération de l'emplacement actuel de la voiture du client et des voitures génantes.

            déplacement des voitures génantes autre part dans le parking, création des ordre et ajout de ceux-ci dans la liste des taches.

            détermination d'une place de swap pour la voiture devant partir.

            calcul "au plus tot" de l'horaire de début de l'action.

            création de l'ordre de dépose et ajout de celui-ci au fond de la liste des taches.

            répartition des taches aux robots suivant la politique du premier disponible. Simulation de leur exécussion.

            simulation du départ du client et temps d'attente.
