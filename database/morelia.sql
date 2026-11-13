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
('f92c4afc-df96-11f1-9bf1-6e304db6703a','Juan','Perez','Lopez','PELJ010101ABC'),
('3cc50f93-df98-11f1-9bf1-6e304db6703a','María','López','Hernández','LOHM900422MDF'),
('3cc58878-df98-11f1-9bf1-6e304db6703a','Carlos','González','Martínez','GOMC821210ABC'),
('3cc596e2-df98-11f1-9bf1-6e304db6703a','Ana','Rodríguez','Sánchez','ROSA950618XYZ'),
('3cc59758-df98-11f1-9bf1-6e304db6703a','Luis','Hernández','Pérez','HEPL8809051H0'),
('3cc5978b-df98-11f1-9bf1-6e304db6703a','Sofía','Martínez','López','MALS9203112H9'),
('3cc597bd-df98-11f1-9bf1-6e304db6703a','Jorge','Sánchez','García','SAGJ7907253K1'),
('3cc597eb-df98-11f1-9bf1-6e304db6703a','Carmen','Ramírez','Flores','RAFC8411304L2'),
('3cc5ef03-df98-11f1-9bf1-6e304db6703a','Alejandro','Torres','Cruz','TOCA9102145M3'),
('3cc5f03f-df98-11f1-9bf1-6e304db6703a','Gabriela','Flores','Ramírez','FORG9608076N4');
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
('f147edba-df9f-11f1-9bf1-6e304db6703a','Av. Madero','120','Centro','Michoacan','58000','f92c4afc-df96-11f1-9bf1-6e304db6703a'),
('f149a87c-df9f-11f1-9bf1-6e304db6703a','Acueducto','450','Chapultepec Norte','Michoacan','58260','3cc50f93-df98-11f1-9bf1-6e304db6703a'),
('f149c13d-df9f-11f1-9bf1-6e304db6703a','Ventura Puente','85','Ventura Puente','Michoacan','58020','3cc58878-df98-11f1-9bf1-6e304db6703a'),
('f149c17e-df9f-11f1-9bf1-6e304db6703a','Av. Camelinas','320','Las Americas','Michoacan','58270','3cc596e2-df98-11f1-9bf1-6e304db6703a'),
('f149c19e-df9f-11f1-9bf1-6e304db6703a','Calzada Juarez','210','Felicitas del Rio','Michoacan','58040','3cc59758-df98-11f1-9bf1-6e304db6703a'),
('f149c1b8-df9f-11f1-9bf1-6e304db6703a','Av. Universidad','150','Villa Universidad','Michoacan','58060','3cc5978b-df98-11f1-9bf1-6e304db6703a'),
('f149c1d1-df9f-11f1-9bf1-6e304db6703a','Bucareli','75','Erendira','Michoacan','58240','3cc597bd-df98-11f1-9bf1-6e304db6703a'),
('f149c1e9-df9f-11f1-9bf1-6e304db6703a','Av. Periodismo','560','Nueva Valladolid','Michoacan','58190','3cc597eb-df98-11f1-9bf1-6e304db6703a'),
('f149c27a-df9f-11f1-9bf1-6e304db6703a','Av. Pedregal','230','Eduardo Ruiz','Michoacan','58149','3cc5ef03-df98-11f1-9bf1-6e304db6703a'),
('f149c29d-df9f-11f1-9bf1-6e304db6703a','Av. Solidaridad','390','Felix Ireta','Michoacan','58070','3cc5f03f-df98-11f1-9bf1-6e304db6703a');
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

-- Dump completed on 2026-11-13 22:14:24
