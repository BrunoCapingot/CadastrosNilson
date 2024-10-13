use plannextsistem;
create table Dados_De_Dagamento_Padrao (
id int not null auto_increment,
cliente_nome  longtext,
cliente_vencimento_da_parcela longtext,
cliente_valor longtext,
cliente_parcela longtext,
primary key(id))