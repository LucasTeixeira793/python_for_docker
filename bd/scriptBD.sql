DROP DATABASE IF EXISTS musica;
CREATE DATABASE musica;
use musica;

CREATE TABLE musica(
	idMusica int primary key auto_increment,
    nomeMusica varchar(30)
);

CREATE TABLE artista(
	idArtista int primary key auto_increment,
    nome varchar(40)
);

CREATE TABLE musica_artista(
	fkMusica int,
    fkArtista int,
    foreign key (fkMusica) references musica(idMusica),
    foreign key (fkArtista) references artista(idArtista)
);

select * from artista;
select * from musica;
select * from musica_artista;

select idMusica from musica order by idMusica desc limit 1 ;