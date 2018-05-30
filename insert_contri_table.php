<?php

	$bdd = new PDO('mysql:host=localhost;dbname=WikiStat.py','jchopin','jchopintnm18;', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
 
 
    $nom = $_GET["nom"];
    $date_pre_contr = $_GET["date_pre_contr"];
    $page_perso = $_GET["page_perso"];
    $id_contributeur = $_GET["id_contributeur"];

   
    function add_info_contr()
    {

    	global $bdd, $id_contributeur, $nom, $page_perso, $date_pre_contr;

    	$req = $bdd->prepare('INSERT INTO contributeur(id_contributeur, nom, date_pre_contr, page_perso) VALUES(:id_contributeur, :nom, :date_pre_contr, :page_perso)');
 
    	$req->execute(array(
	        'id_contributeur' => $id_contributeur,
	        'nom' => utf8_decode($nom),
	        'date_pre_contr' => utf8_decode($date_pre_contr),
	        'page_perso' => $page_perso
	        ));
    }

    add_info_contr();

?>