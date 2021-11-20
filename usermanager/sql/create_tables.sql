USE EDI

CREATE TABLE users (
    id int IDENTITY(1,1) PRIMARY KEY,    
	email varchar(255) NOT NULL,
	password varchar(255) NOT NULL,
	name varchar(255) NOT NULL,
    surname varchar(255) NOT NULL,
	comp_name varchar(255) NOT NULL,
);

CREATE TABLE aziende (
    id int IDENTITY(1,1) PRIMARY KEY,
    comp_name varchar(255) NOT NULL,
    vat bigint NOT NULL,
	
    );
