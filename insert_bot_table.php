<?php

	$bdd = new PDO('mysql:host=localhost;dbname=WikiStat.py','jchopin','jchopintnm18;', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
 
 
    $id_bot = $_GET["id_bot"];
    $nom = $_GET["nom"];
    $date_creation = $_GET["date_creation"];
    $nb_modification = $_GET["nb_modification"];
    $statut = $_GET["statut"];
    $id_contributeur = $_GET["id_contributeur"];

   
    function add_info_bot()
    {

    	//URL EXAMPLE: http://on.nexioh.eu/isfates_jchopin/bdd/insert_bot_table.php?id_bot='bot705'&nom=%27test3%27&date_creation=2023-05-03&nb_modification=%270%27&statut=%27en%20test%27

    	global $bdd, $id_bot, $nom, $date_creation, $nb_modification, $statut;

    	$req = $bdd->prepare('INSERT INTO bot(id_bot, nom, date_creation, nb_modification, statut) VALUES(:id_bot, :nom, :date_creation, :nb_modification, :statut)');
 
    	$req->execute(array(
	        'id_bot' => $id_bot,
	        'nom' => $nom,
	        'date_creation' => utf8_decode($date_creation),
	        'nb_modification' => $nb_modification,
	        'statut' => utf8_decode($statut)
	        ));
    }


    function add_for_key_bot()
    {
    	global $bdd, $id_bot, $id_contributeur;

    	$req = $bdd->prepare('UPDATE bot SET id_contributeur = :id_contributeur WHERE id_bot = :id_bot');
    	
    	$req->execute(array(
	        'id_contributeur' => $id_contributeur,
	        'id_bot' => $id_bot
	        ));
    }


    //add_info_bot();
    add_for_key_bot();

?>