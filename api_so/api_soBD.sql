create database api_so;
use api_so;

create table tbJogadorBasket (
	idJogador int primary key auto_increment,
    nomeJogador varchar(50),
    altura decimal(3,2),
    posicao varchar(3),
    numeroCamisa varchar(3),
    team varchar(50)
);

select * from tbJogadorBasket;


