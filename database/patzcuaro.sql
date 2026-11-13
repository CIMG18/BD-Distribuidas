/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.20-11.8.9-MariaDB, for debian-linux-gnu (aarch64)
--
-- Host: localhost    Database: sucursal
-- ------------------------------------------------------
-- Server version	11.8.9-MariaDB-ubu2404

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Dumping data for table `Clientes`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Clientes` WRITE;
/*!40000 ALTER TABLE `Clientes` DISABLE KEYS */;
INSERT INTO `Clientes` VALUES
('46db6e94-dfa0-11f1-9dd2-569b24a5d72d','Daniela','Mendoza','Lopez','MELD010101P01'),
('46dba570-dfa0-11f1-9dd2-569b24a5d72d','Roberto','Garcia','Soto','GASR020202P02'),
('46dbf262-dfa0-11f1-9dd2-569b24a5d72d','Fernanda','Ortiz','Vega','OIVF030303P03'),
('46dbf2e0-dfa0-11f1-9dd2-569b24a5d72d','Miguel','Navarro','Diaz','NADM040404P04'),
('46dbf31b-dfa0-11f1-9dd2-569b24a5d72d','Valeria','Reyes','Cruz','RECV050505P05'),
('46dbf391-dfa0-11f1-9dd2-569b24a5d72d','Andres','Silva','Mora','SIMA060606P06'),
('46dbfec4-dfa0-11f1-9dd2-569b24a5d72d','Camila','Rojas','Perez','ROPC070707P07'),
('46dbff1e-dfa0-11f1-9dd2-569b24a5d72d','Ricardo','Vargas','Luna','VALR080808P08'),
('46dbffe1-dfa0-11f1-9dd2-569b24a5d72d','Paola','Castillo','Rios','CARP090909P09'),
('46dc0013-dfa0-11f1-9dd2-569b24a5d72d','Emilio','Fuentes','Paz','FUPE101010P10');
/*!40000 ALTER TABLE `Clientes` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Dumping data for table `Direcciones`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Direcciones` WRITE;
/*!40000 ALTER TABLE `Direcciones` DISABLE KEYS */;
INSERT INTO `Direcciones` VALUES
('a39064e5-dfa0-11f1-9dd2-569b24a5d72d','Portal Hidalgo','15','Centro','Michoacan','61600','46db6e94-dfa0-11f1-9dd2-569b24a5d72d'),
('a3906a1f-dfa0-11f1-9dd2-569b24a5d72d','Ponce de Leon','42','Centro','Michoacan','61600','46dba570-dfa0-11f1-9dd2-569b24a5d72d'),
('a3906a33-dfa0-11f1-9dd2-569b24a5d72d','Ibarra','120','Centro','Michoacan','61600','46dbf262-dfa0-11f1-9dd2-569b24a5d72d'),
('a3906a3f-dfa0-11f1-9dd2-569b24a5d72d','Federico Tena','85','Centro','Michoacan','61600','46dbf2e0-dfa0-11f1-9dd2-569b24a5d72d'),
('a3906a48-dfa0-11f1-9dd2-569b24a5d72d','Alvaro Obregon','210','Centro','Michoacan','61600','46dbf31b-dfa0-11f1-9dd2-569b24a5d72d'),
('a3906a51-dfa0-11f1-9dd2-569b24a5d72d','Benigno Serrato','65','Centro','Michoacan','61600','46dbf391-dfa0-11f1-9dd2-569b24a5d72d'),
('a3906a5a-dfa0-11f1-9dd2-569b24a5d72d','Teran','34','Centro','Michoacan','61600','46dbfec4-dfa0-11f1-9dd2-569b24a5d72d'),
('a3906a62-dfa0-11f1-9dd2-569b24a5d72d','Navarrete','90','Centro','Michoacan','61600','46dbff1e-dfa0-11f1-9dd2-569b24a5d72d'),
('a3906a6a-dfa0-11f1-9dd2-569b24a5d72d','Dr. Coss','125','Centro','Michoacan','61600','46dbffe1-dfa0-11f1-9dd2-569b24a5d72d'),
('a3906a72-dfa0-11f1-9dd2-569b24a5d72d','Libertad','180','Centro','Michoacan','61600','46dc0013-dfa0-11f1-9dd2-569b24a5d72d');
/*!40000 ALTER TABLE `Direcciones` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2026-11-13 22:15:50
