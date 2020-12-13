CREATE TABLE AGENTS
(
	AGENT_CODE CHAR(6) NOT NULL PRIMARY KEY,
    AGENT_NAME CHAR(40),
    WORKING_AREA CHAR(40),
    COMMSION int(10,2),
    PHONE CHAR(15),
    COUNTRY VARCHAR(25)
    
);

INSERT INTO AGENTS VALUES('a007', 'Suman Thapa Magar', 'TEXAS', '0.13', '3456789012' , 'NEPAL');
INSERT INTO AGENTS VALUES('A006','SUNIL THAPA MAGAR','KATHMANDU','0.45','98417999963' , 'AMERICA');

CREATE TABLE CUSTOMER
(
	CUST_CODE VARCHAR(6) NOT NULL PRIMARY KEY,
    CUST_NAME VARCHAR(40) NOT NULL
    
);