-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: infostore
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `adress`
--

DROP TABLE IF EXISTS `adress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `adress` (
  `idadress` int NOT NULL AUTO_INCREMENT,
  `cod_customer` varchar(18) NOT NULL,
  `ender` varchar(150) NOT NULL,
  `cidade` varchar(45) DEFAULT NULL,
  `uf` varchar(2) DEFAULT NULL,
  `CEP` varchar(9) DEFAULT NULL,
  PRIMARY KEY (`idadress`),
  KEY `cpf_cnpj_idx` (`cod_customer`),
  CONSTRAINT `cpf_cnpj` FOREIGN KEY (`cod_customer`) REFERENCES `customers` (`cpf_cnpj`)
) ENGINE=InnoDB AUTO_INCREMENT=158 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adress`
--

LOCK TABLES `adress` WRITE;
/*!40000 ALTER TABLE `adress` DISABLE KEYS */;
INSERT INTO `adress` VALUES (92,'222.717.890-60','Rua dos Inventores, 1000, Vila da Criatividade','Anchiano','IT','00000-000'),(93,'646.613.010-05','Rua da Eletricidade, 5555, Vila da Iluminação','Smiljan','CR','00000-000'),(94,'646.613.010-05','Rua dos Inventos, 5555, Vila Criativa','New York','US','00000-000'),(96,'950.351.340-59','Rua da Gravitação Universal, 1000, Vila das Maças','London','UK','00000-000'),(104,'236.465.850-05','Rua do Vapor, 1050, Vila Locomotiva','Glasgow','GB','98765-432'),(109,'406.031.790-02','Rua da Matemática, 0123, Vila dos Cálculos','Clermont','FR','00000-000'),(112,'326.023.440-36','Rua da Imprensa, 900, Vila dos Livros','Estrasburgo','FR','00000-000'),(113,'223.305.740-61','Rua dos Parachoques, 500, V. dos Carros','Richmond','CA','00000-000'),(118,'946.958.510-08','Rua das Lampadas, 1258, V. Iluminada','Milan','OH','00000-000'),(119,'946.958.510-08','Rua Luminária, n. 1250, V. dos Iluminados','Ilunópolis','BR','00000-000'),(130,'960.892.920-28','Rua das Armas, 800, V. das Pistolas','Gardone Val Trompia','IT','99999-000'),(131,'355.230.610-26','Rua do Diesel, 100, V. dos Caminhões','Karlsruhe','GE','00000-000'),(139,'317.337.600-59','Rua dos Vapores, 600, V. das Bombas','Modbury','UK','01234-000'),(140,'071.885.220-65','Rua da Eletricidade, 40, V. das Luzes','Newington','UK','0123-0123'),(141,'391.128.800-00','Rua dos Livros, 100, Vila da Biblioteca','Stratford-upon-avon','UK','12345-678'),(142,'945.754.400-51','Rua das Lanternas, 555, Vila Iluminada','Bishopwearmouth','UK','12345-000'),(144,'859.289.190-69','Rua das Torres, 1550, Vila dos Orelhoes','Lucélia','SP','17780-000'),(145,'859.289.190-69','Rua dos Telefones, 1234, Vila da Comunicação','Telefonópolis','BR','01234-567'),(147,'540.466.440-10','St. Internet, 404','London','UK','00000-000'),(148,'739.274.610-32','Agriculture St.','Dover','US','12345-789'),(149,'578.989.070-94','Rua do Cinema, 1000, Vila dos Filmes','Lyon','FR','00000-000'),(150,'50.858.693/0001-26','Rua dos Inventos, 2000, Vila Empresarial','São Paulo','SP','12345-123'),(152,'352.560.790-34','Rua dos Fogões, 500, B. Fogareiro','Boston','US','01234-012'),(153,'59.593.414/0001-14','Rua Vitória, 7133, Bairro São José','Itapipoca','CE','01234-567'),(154,'86.934.423/0001-02','Rua dos Santos, 2000, Vila da Santidade','Santos','SP','01234-567'),(155,'969.651.350-00','Rua da Relatividade, 100','Ulm','GE','00000-000'),(157,'993.532.450-87','Rua da Matemática, 12345, V. dos Números','São Paulo','SP','12345-000');
/*!40000 ALTER TABLE `adress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brand`
--

DROP TABLE IF EXISTS `brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brand` (
  `idbrand` int NOT NULL AUTO_INCREMENT,
  `brand` varchar(45) NOT NULL,
  PRIMARY KEY (`idbrand`),
  UNIQUE KEY `trend_UNIQUE` (`brand`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brand`
--

LOCK TABLES `brand` WRITE;
/*!40000 ALTER TABLE `brand` DISABLE KEYS */;
INSERT INTO `brand` VALUES (40,'Acer'),(25,'AOC'),(37,'Asus'),(24,'Compaq'),(34,'Enermax'),(38,'Gigabyte'),(30,'Google'),(21,'HP'),(33,'Intel'),(39,'Kingston'),(35,'Leadership'),(23,'LG'),(4,'Marca 2'),(7,'Marca 3'),(8,'Marca 4'),(9,'Marca 5'),(11,'Marca 6'),(13,'Marca 7'),(14,'Marca 8'),(17,'Marca XYZ'),(28,'Monitores'),(32,'Multilaser'),(1,'Padrão'),(22,'Samsung'),(36,'TP Link');
/*!40000 ALTER TABLE `brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `idcategory` int NOT NULL AUTO_INCREMENT,
  `category` varchar(45) NOT NULL,
  PRIMARY KEY (`idcategory`),
  UNIQUE KEY `category_UNIQUE` (`category`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (35,'Cabos'),(25,'Categoria ABC'),(26,'Categoria CDE'),(45,'Impressoras'),(47,'Memória'),(43,'Monitores'),(36,'Mouses'),(46,'Notebooks'),(1,'Padrão'),(39,'Periféricos'),(38,'Placas'),(40,'Principais'),(42,'Processadores'),(44,'Roteadores'),(48,'Scaners'),(41,'Smartphones'),(50,'Tablets'),(37,'Teclados');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `idcustomers` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `cpf_cnpj` varchar(18) NOT NULL,
  `tel` varchar(20) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `observ` varchar(100) DEFAULT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`idcustomers`,`cpf_cnpj`),
  UNIQUE KEY `cpf_cnpj_UNIQUE` (`cpf_cnpj`)
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (35,'LEONARDO DA VINCI','222.717.890-60','18 99999 0000','leonardo@davinci','Observ...','2023-06-20'),(36,'NICOLA TESLA','646.613.010-05','19 99999 0000','nicola@tesla','...','2023-06-20'),(37,'ALEXANDER GRAHAN BELL','859.289.190-69','18 99999 9999','grahan@bell.com','.....','2023-06-20'),(38,'ISAAC NEWTON','950.351.340-59','16 05566 0555','isaac@newton','...','2023-06-20'),(40,'GALILEO GALILEI','448.200.420-09','17 99999 0000','galileo@galilei','...','2023-06-20'),(41,'JAMES WATT','236.465.850-05','00 00000 0000','james@watt','...','2023-06-20'),(43,'THOMAS EDSON','946.958.510-08','18 00000 1111','thomas@edson','...','2023-06-20'),(44,'BLAISE PASCAL','406.031.790-02','00 00000 0000','blaise@pascal','...','2023-06-20'),(47,'JOHANN GUTEMBERG','326.023.440-36','10 10101 1010','johann@gutemberg','...','2023-06-20'),(50,'GEORGE ALBERT LYON','223.305.740-61','00000 0000','george@lyon','','2023-06-20'),(56,'BARTOLOMEO BERETTA','960.892.920-28','11111 1111','bartolomeo@beretta','Observ','2023-06-20'),(64,'ALBERT EINSTEIN','969.651.350-00','12345 6789','albert@einstein','...','2023-06-20'),(66,'KARL FRIEDRICH MICHAEL BENZ','355.230.610-26','00000 1111','karl@benz','.','2023-06-20'),(67,'WILLIAM SHAKESPEARE','391.128.800-00','00000 0000','william@shakespeare','','2023-06-20'),(68,'BENJAMIN FRANKLIN','352.560.790-34','14 12345-000','benjamin@franklin','','2023-06-20'),(69,'ARQUIMEDES DE SIRACUSA','993.532.450-87','01 98765-432','arquim@siracusa.com','.....','2023-06-20'),(70,'THOMAS SAVERY','317.337.600-59','00000 0000','thomas@savery.com','','2023-06-20'),(71,'MICHAEL FARADAY','071.885.220-65','45612-123','michale@faraday.com','','2023-06-20'),(72,'JOSEPH WILSON SWAN','945.754.400-51','12 34567 8901','joseph@swan','...','2023-06-20'),(73,'TIMOTHY JOHN BERNERS-LEE','540.466.440-10','00000-0000','timothy@berners.lee','...','2023-07-10'),(74,'EDWARD HUBER','739.274.610-32','12345-1234','dover@edward','...','2023-07-10'),(75,'AUGUSTE MARIE LOUIS NICHOLAS LUMIÈRE','578.989.070-94','20 21215 2020','auguste@lumiere','','2023-07-14'),(76,'EMPRESA XYZ LTDA','50.858.693/0001-26','14 12345 1234','empresa@empresa.xyz','','2023-07-14'),(79,'EMPRESA FICTICIA UM','15.364.086/0001-09','12 34567 8901','empresa@ficticia.com','','2023-07-17'),(80,'ECO EMPRESA SÃO PAULO','59.593.414/0001-14','20 00000-0000','eco@saopaulo.com','...','2023-07-18'),(81,'EMPRESA SANTOS & SANTOS','86.934.423/0001-02','11111 1111','santos@santos.com','Em atividade','2023-07-22');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `idproducts` int NOT NULL AUTO_INCREMENT,
  `descr` varchar(50) NOT NULL,
  `idcategory` int NOT NULL,
  `idbrand` int NOT NULL,
  `stock` int unsigned NOT NULL,
  `minstock` int unsigned NOT NULL,
  `maxstock` int unsigned NOT NULL,
  `observ` varchar(100) DEFAULT NULL,
  `costs` float NOT NULL,
  `sellprice` float NOT NULL,
  `margin` float NOT NULL,
  PRIMARY KEY (`idproducts`),
  KEY `category_fk_idx` (`idcategory`),
  KEY `trend_fk_idx` (`idbrand`),
  CONSTRAINT `brand_fk` FOREIGN KEY (`idbrand`) REFERENCES `brand` (`idbrand`),
  CONSTRAINT `category_fk` FOREIGN KEY (`idcategory`) REFERENCES `category` (`idcategory`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (13,'PRODUTO CDE',26,17,51,30,150,'...',1,2.5,150),(17,'TECLADO SEM FIO MODELO TC240',37,32,63,20,100,'.....',110,180,63.64),(18,'TECLADO SEM FIO MODELO TC250',37,32,49,20,100,'Bateria Recarregável',110,180,63.64),(19,'IMPRESSORA LASER MOD. ML-2165W',39,22,13,5,30,'-',200.5,250,24.69),(20,'SMARTPHONE SAMSUNG MOD. M54 COR PRETA',41,22,19,5,35,'...',1800,2199.95,22.22),(21,'MOUSE SEM FIO MODELO AC540',36,32,39,20,100,'Bateria Recarregável',200,300,50),(22,'PLACA DE VÍDEO 8GB',38,14,45,10,50,'',600,1000.6,66.77),(23,'COOLER PARA PROCESSADOR INTEL 775',40,33,139,20,200,'...',50,75,50),(24,'ESTABILIZADOR 300VA',40,34,19,10,30,'...',58.5,90.55,54.79),(25,'FONE DE OUVIDO COM MICROFONE',39,22,14,5,20,'',25,80,220),(26,'HEADPHONE PROFISSIONAL',39,35,50,10,60,'',20,50,150),(27,'PLACA-MÃE MODELO ABC-0123',38,33,26,10,30,'...',500,750,50),(28,'MONITOR LG 19,5 LED 20MK400H',43,23,17,15,50,'',350,533.4,52.4),(29,'MONITOR LED 23,8 IPS FULL HD 24MK430H LG',43,23,19,15,50,'',620,843.8,36.1),(30,'PLACA PCI EXPRESS WI-FI 6 AX3000, ARCHER TX5',38,36,44,30,100,'',325,479.89,47.66),(31,'ROTEADOR WIRELESS 4 DUAL BAND AC1200 ARCHER',44,36,38,30,80,'',255,339.89,33.29),(32,'IMPRESSORA OFFICEJET MOBILE 200 CZ993A COLORIDA',1,21,4,5,20,'',1200,1438.68,19.89),(33,'PLACA DE VÍDEO RTX ASUS NVIDIA GEFORCE RTX 3060',38,37,11,10,20,'',1540,2099.94,36.36),(35,'NOTEBOOK 15.6 CORE I3-10110U 4GB 1TB WIN10 PRATA',46,22,19,15,25,'',2499,2999.9,20.04),(36,'PLACA MÃE H510M LGA 1200 DDR4 10ª E 11ª GERAÇÃO',38,38,9,10,20,'',410,519.02,26.59),(37,'MEMÓRIA FURY IMPACT 16GB 3200MHZ, DDR4, CL20',47,39,25,15,50,'...',153.99,269.99,75.33),(39,'TABLET SAMSUNG GALAXY TAB A 32 GB 8\" T290NZKMZTO',50,22,16,15,25,'Android - Quad-Core',712,854.4,20);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales`
--

DROP TABLE IF EXISTS `sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales` (
  `idsale` int NOT NULL AUTO_INCREMENT,
  `idcustomer` int NOT NULL,
  `date` date NOT NULL,
  `total` float NOT NULL,
  PRIMARY KEY (`idsale`),
  KEY `customer_fk_idx` (`idcustomer`),
  CONSTRAINT `customer_fk` FOREIGN KEY (`idcustomer`) REFERENCES `customers` (`idcustomers`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales`
--

LOCK TABLES `sales` WRITE;
/*!40000 ALTER TABLE `sales` DISABLE KEYS */;
INSERT INTO `sales` VALUES (13,36,'2023-06-16',6118.49),(15,40,'2023-06-21',2924.95),(16,43,'2023-06-21',1843.68),(17,44,'2023-06-21',2547.45),(18,47,'2023-06-21',1060),(24,37,'2023-06-21',2632.45),(26,64,'2023-06-21',1235.5),(27,50,'2023-06-21',6406.1),(29,41,'2023-06-22',2359.95),(31,38,'2023-06-22',2800.6),(32,67,'2023-06-27',250),(33,64,'2023-06-28',2151.1),(34,56,'2023-06-28',5004.3),(35,69,'2023-06-28',1800.6),(36,70,'2023-06-29',130),(37,72,'2023-06-29',3495.66),(38,70,'2023-06-29',482.39),(39,66,'2023-06-29',2099.94),(40,41,'2023-07-02',2294.95),(41,68,'2023-07-06',1050.5),(42,69,'2023-07-07',5250.97),(43,66,'2023-07-07',2962.36),(44,72,'2023-07-10',3533.34),(45,74,'2023-07-10',2579.83),(46,73,'2023-07-10',281.1),(47,35,'2023-07-11',6299.88),(48,73,'2023-07-12',2033.4),(49,47,'2023-07-13',2309.94),(50,66,'2023-07-14',1764),(51,68,'2023-07-14',3600),(52,75,'2023-07-14',2338.68),(53,76,'2023-07-14',477.5),(54,67,'2023-07-17',1439.67),(55,47,'2023-07-17',930),(56,79,'2023-07-17',2099.94),(57,80,'2023-07-18',4540.48),(58,71,'2023-07-19',3000),(59,35,'2023-07-19',1477.15),(60,44,'2023-07-19',2877.36),(61,37,'2023-07-19',4438.58),(62,75,'2023-07-22',269.99),(63,81,'2023-07-22',1033.05),(64,76,'2023-07-24',161.02),(65,66,'2023-07-26',848.99),(66,73,'2023-07-26',848.99),(67,81,'2023-07-26',25),(68,43,'2023-07-26',986.14),(70,70,'2023-07-30',1368.01),(71,50,'2023-07-30',2939.9),(72,66,'2023-07-30',564.98),(73,72,'2023-07-31',4534.66),(74,56,'2023-08-01',973.8);
/*!40000 ALTER TABLE `sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soldproducts`
--

DROP TABLE IF EXISTS `soldproducts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `soldproducts` (
  `idsoldproducts` int NOT NULL AUTO_INCREMENT,
  `idsale` int NOT NULL,
  `idproduct` int NOT NULL,
  `quantity` int NOT NULL,
  `unitprice` float NOT NULL,
  `cost` float NOT NULL,
  `total` float NOT NULL,
  PRIMARY KEY (`idsoldproducts`),
  KEY `idsale_fk_idx` (`idsale`),
  KEY `idproduct_fk_idx` (`idproduct`),
  CONSTRAINT `idproduct_fk` FOREIGN KEY (`idproduct`) REFERENCES `products` (`idproducts`),
  CONSTRAINT `idsale_fk` FOREIGN KEY (`idsale`) REFERENCES `sales` (`idsale`)
) ENGINE=InnoDB AUTO_INCREMENT=349 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soldproducts`
--

LOCK TABLES `soldproducts` WRITE;
/*!40000 ALTER TABLE `soldproducts` DISABLE KEYS */;
INSERT INTO `soldproducts` VALUES (119,26,23,1,75,50,75),(120,26,24,1,1000.5,58.5,1000.5),(121,26,25,2,80,25,160),(136,17,20,1,2199.95,1800,2199.95),(137,17,21,1,300,200,300),(138,17,26,1,47.5,20,47.5),(147,29,20,1,2199.95,1800,2199.95),(148,29,25,2,80,25,160),(174,32,19,1,250,200.5,250),(178,18,25,1,80,25,80),(179,18,18,1,180,110,180),(180,18,26,1,50,20,50),(181,18,27,1,750,500,750),(184,24,18,1,180,110,180),(185,24,19,1,250,200.5,250),(186,24,20,1,2199.95,1800,2199.95),(187,24,13,1,2.5,1,2.5),(188,34,13,1,2.5,1,2.5),(189,34,19,2,250,200.5,500),(190,34,21,5,300,200,1500),(191,34,22,3,1000.6,600,3001.8),(192,35,27,1,750,500,750),(193,35,26,1,50,20,50),(194,35,22,1,1000.6,600,1000.6),(195,33,23,2,75,50,150),(196,33,24,1,1000.5,58.5,1000.5),(197,33,22,1,1000.6,600,1000.6),(198,36,25,1,80,25,80),(199,36,26,1,50,20,50),(200,37,32,1,1438.68,1200,1438.68),(201,37,31,2,339.89,255,679.78),(202,37,28,1,533.4,350,533.4),(203,37,29,1,843.8,620,843.8),(218,38,30,1,479.89,325,479.89),(219,38,13,1,2.5,1,2.5),(220,39,33,1,2099.94,1540,2099.94),(224,40,20,1,2089.95,1800,2089.95),(225,40,23,1,75,50,75),(226,40,25,1,80,25,80),(227,40,26,1,50,20,50),(228,15,19,1,250,200.5,250),(229,15,20,1,2199.95,1800,2199.95),(230,15,26,2,50,20,100),(231,15,23,5,75,50,375),(249,13,13,1,2.5,1,2.5),(250,13,17,2,180,110,360),(251,13,18,1,180,110,180),(252,13,19,1,250,200.5,250),(253,13,21,2,300,200,600),(254,13,22,1,1000.6,600,1000.6),(255,13,23,1,75,50,75),(256,13,25,1,80,25,80),(257,13,26,1,50,20,50),(258,13,27,1,750,500,750),(259,13,20,1,2199.95,1800,2199.95),(260,13,30,1,479.89,325,479.89),(261,13,24,1,90.55,58.5,90.55),(262,43,25,1,80,25,80),(263,43,32,2,1438.68,1200,2877.36),(264,43,13,2,2.5,1,5),(267,27,20,2,2199.95,1800,4399.9),(268,27,13,2,2.5,1,5),(269,27,22,2,1000.6,600,2001.2),(270,44,21,3,300,200,900),(271,44,33,1,2099.94,1540,2099.94),(272,44,28,1,533.4,350,533.4),(273,16,21,1,300,200,300),(274,16,26,2,50,20,100),(275,16,13,2,2.5,1,5),(276,16,32,1,1438.68,1200,1438.68),(277,45,33,1,2099.94,1540,2099.94),(278,45,30,1,479.89,325,479.89),(279,46,26,2,50,20,100),(280,46,24,2,90.55,58.5,181.1),(281,31,21,1,300,200,300),(282,31,22,1,1000.6,600,1000.6),(283,31,21,5,300,200,1500),(284,42,29,2,843.8,620,1687.6),(285,42,32,1,1438.68,1200,1438.68),(286,42,33,1,2099.94,1540,2099.94),(287,42,13,10,2.48,1,24.75),(289,47,33,2,2099.94,1540,4199.88),(290,47,21,7,300,200,2100),(291,48,27,2,750,500,1500),(292,48,28,1,533.4,350,533.4),(293,49,25,2,80,25,160),(294,49,26,1,50,20,50),(295,49,33,1,2099.94,1540,2099.94),(296,50,17,10,176.4,110,1764),(297,51,17,10,180,110,1800),(298,51,18,10,180,110,1800),(299,52,32,1,1438.68,1200,1438.68),(300,52,17,5,180,110,900),(304,53,17,1,180,110,180),(305,53,18,1,180,110,180),(306,53,25,1,80,25,80),(307,53,13,15,2.5,1,37.5),(308,54,30,3,479.89,325,1439.67),(309,55,23,10,75,50,750),(310,55,17,1,180,110,180),(311,56,33,1,2099.94,1540,2099.94),(312,57,22,3,1000.6,600,3001.8),(313,57,26,2,50,20,100),(314,57,32,1,1438.68,1200,1438.68),(315,58,21,10,300,200,3000),(317,60,32,2,1438.68,1200,2877.36),(318,61,35,1,2999.9,2499,2999.9),(319,61,32,1,1438.68,1200,1438.68),(320,62,37,1,269.99,153.99,269.99),(321,63,37,2,269.99,153.99,539.98),(322,63,36,1,493.07,410,493.07),(323,64,23,1,75,50,75),(324,64,24,1,86.02,58.5,86.02),(325,65,39,1,848.99,712,848.99),(326,66,39,1,848.99,712,848.99),(327,67,13,10,2.5,1,25),(328,68,36,2,493.07,410,986.14),(332,59,24,13,90.55,58.5,1177.15),(333,59,21,1,300,200,300),(334,41,26,1,50,20,50),(335,41,24,1,1000.5,58.5,1000.5),(338,70,36,1,519.02,410,519.02),(339,70,39,1,848.99,712,848.99),(340,71,35,1,2939.9,2499,2939.9),(341,72,37,2,269.99,153.99,539.98),(342,72,13,10,2.5,1,25),(343,73,32,1,1438.68,1200,1438.68),(344,73,33,1,2057.94,1540,2057.94),(345,73,36,2,519.02,410,1038.04),(346,74,25,1,80,25,80),(347,74,26,1,50,20,50),(348,74,29,1,843.8,620,843.8);
/*!40000 ALTER TABLE `soldproducts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `idUser` int NOT NULL AUTO_INCREMENT,
  `name` varchar(65) NOT NULL,
  `user` varchar(20) NOT NULL,
  `password` varchar(80) NOT NULL,
  `date` date NOT NULL,
  `acesso` varchar(10) NOT NULL,
  PRIMARY KEY (`idUser`),
  UNIQUE KEY `user_UNIQUE` (`user`)
) ENGINE=InnoDB AUTO_INCREMENT=163 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-01 14:10:43
