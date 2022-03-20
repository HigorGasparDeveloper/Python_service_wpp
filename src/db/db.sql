/*
Banco de utilização do projeto - simples, em mysql
Campos para apenas verificar se já foi enviada, se já foi deletada, armazenar o texto da mensagem e o destino
*/
/*Tabela das mensagens*/
create table message(
  id_message int not null primary key auto_increment,
  text_message blob,
  number_message char(14),
  status_message char(1),
  was_deleted char(1)
);