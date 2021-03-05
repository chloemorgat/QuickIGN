
<h1> QUICKIGN </h1>

1. Télécharger le Plugin QuickIGN

2. Ranger ce Plugin dans le répertoire : /home/formation/.local/share/QGIS/QGIS3/profiles/default/python/plugins

3. Ouvrir un terminal dans le fichier QuickIGN (clique droit > ouvrir un terminal)

4.  Tapez la ligne de commande ci-dessous :
	<p align="center">
		<img src="https://raw.githubusercontent.com/chloemorgat/QuickIGN/main/Image/pyrcc5.png">
	<p>
	<p align="center">
		Cette ligne va permettre d'ajouter un fichier resources.py et resources.qrc dans le fichier QuickIGN. Ces fichiers sont nécessaires à l'ajout de toutes images.
	<p>
	
5. Ouvrir QGis, Aller dans Extensions > Installer/Gérer les extensions. Tapez dans la barre de recherche QuickIGN puis cochez le plugin comme ci-dessous :
	
	<p align="center">
		<img src="https://raw.githubusercontent.com/chloemorgat/QuickIGN/main/Image/quickign.png">
	<p>
	<p align="center">
		Cette action peut nécessiter, dans certains cas, un redémarrage du logiciel.
	<p>
	
 6. Cliquez sur le logo apparu dans la barre des outils dockwidget (voir ci-dessous) :
	
	<img src="https://raw.githubusercontent.com/chloemorgat/QuickIGN/main/Image/logo.png">
	<p align="center">
		La fenêtre WMS va permettre de manipuler les différents fonds de cartes en cochant ou décochant les cases.
	<p>
	<p align="center">
		<img src="https://raw.githubusercontent.com/chloemorgat/QuickIGN/main/Image/plugiin.png">
	<p>
	
		La fenêtre Couche Vecteur va permettre de manipuler les couches de la BDTopo d'un département que l'utilisateur a, au préalable, <span style= "color: red"> téléchargé sur le site de l'IGN </span>. Pour obtenir ces couches de vecteurs, le Plugin nécessite d'avoir le chemin indiquant l'emplacement de la BDTopo dans l'ordinateur. 
	<p align="center">	
	<a href= "https://geoservices.ign.fr/documentation/diffusion/telechargement-donnees-libres.html"> Site de téléchargement BDTopo (IGN) </a>
	<p>
	
	<p align="center">
		<img src="https://raw.githubusercontent.com/chloemorgat/QuickIGN/main/Image/plugiiin*.png">
	<p>

7. Ouvrir le dossier BDTopo.
	Exemple : ouvrir BDTOPO_3-0_TOUSTHEMES_SHP_LAMB93_D076_2020-12-1 > BDTOPO > 1_DONNEES_LIVRAISON_2021-01-00019 > BDT_3-0_SHP_LAMB93_D076-ED2020-12-15 > HYDROGRAPHIE

8. Clic droit sur l'un des dossier thème > propiétés > copier l'adresse dossier parent  
	Exemple : /home/formation/Documents/BDTOPO_3-0_TOUSTHEMES_SHP_LAMB93_D076_2020-12-15/BDTOPO/1_DONNEES_LIVRAISON_2021-01-00019/BDT_3-0_SHP_LAMB93_D076-ED2020-12-15/HYDROGRAPHIE

9. Coller l'adresse du dossier parent dans la case blanche, Valider ! 
	
	<p align="center">
	<img src="https://raw.githubusercontent.com/chloemorgat/QuickIGN/main/Image/chemintxtedit.png">
	<p>
	
