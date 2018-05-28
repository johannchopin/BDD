CREATE TABLE contributeur(id_contributeur integer AUTO_INCREMENT,
	  nom varchar(50),
	  date_inscription date,
	  nb_modification integer,
	  date_modif date,
PRIMARY KEY(id_contributeur)
);

CREATE TABLE article(id_article integer AUTO_INCREMENT,
                     nom varchar(50),
                     type varchar(50),
                     nb_parties integer,
                     nb_mots integer,
                     nb_langues integer,
                     nb_sources integer,
                     date_modif date,
	  id_contributeur integer,
PRIMARY KEY (id_article),
FOREIGN KEY(id_contributeur) REFERENCES contributeur(id_contributeur)
);

CREATE TABLE portail(id_portail integer AUTO_INCREMENT PRIMARY KEY,
	  nom varchar(50),
	  nb_articles integer
);

CREATE TABLE categorie(id_categorie integer AUTO_INCREMENT PRIMARY KEY,
	  nom varchar(50),
	  id_portail integer,
FOREIGN KEY (id_portail) REFERENCES portail(id_portail)
);

CREATE TABLE categorie_portail(id_categorie integer,
		id_portail integer,
PRIMARY KEY(id_categorie, id_portail),
FOREIGN KEY(id_categorie) REFERENCES categorie(id_categorie),
FOREIGN KEY(id_portail) REFERENCES portail(id_portail)
);

CREATE TABLE categories_article(id_article integer,
	  id_categorie integer,
PRIMARY KEY (id_article, id_categorie),
FOREIGN KEY(id_article) REFERENCES article(id_article),
FOREIGN KEY(id_categorie) REFERENCES categorie(id_categorie)
);

CREATE TABLE bot(id_bot integer AUTO_INCREMENT,
	  nom varchar(50),
	  date_creation date,
	  nb_modification integer,
      id_contributeur integer,
PRIMARY KEY(id_bot),
FOREIGN KEY(id_contributeur) REFERENCES contributeur(id_contributeur)
);

