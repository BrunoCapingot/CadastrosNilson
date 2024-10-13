use plannextsistem;
create table Inadiplencia_Geral (
id int not null auto_increment,
cliente_nome  longtext,
cliente_parcelas_em_aberto longtext,
cliente_valores_em_aberto longtext,

primary key(id))