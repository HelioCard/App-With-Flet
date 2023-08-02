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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-01 13:19:37
