-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.1.72-community - MySQL Community Server (GPL)
-- Server OS:                    Win32
-- HeidiSQL Version:             9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for edi
DROP DATABASE IF EXISTS `edi`;
CREATE DATABASE IF NOT EXISTS `edi` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `edi`;

-- Dumping structure for table edi.aziende
DROP TABLE IF EXISTS `aziende`;
CREATE TABLE IF NOT EXISTS `aziende` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comp_name` varchar(255) NOT NULL,
  `vat` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- Dumping data for table edi.aziende: 0 rows
/*!40000 ALTER TABLE `aziende` DISABLE KEYS */;
INSERT INTO `aziende` (`id`, `comp_name`, `vat`) VALUES
	(5, 'Ferrero International S.A.', 20000000001),
	(6, 'The Coca-Cola Company', 20000000002);
/*!40000 ALTER TABLE `aziende` ENABLE KEYS */;

-- Dumping structure for table edi.users
DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL,
  `comp_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `ban`;
CREATE TABLE IF NOT EXISTS `ban` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `banner_ip` varchar(255) NOT NULL,
  
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1;

-- Dumping data for table edi.users: 0 rows
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`id`, `email`, `password`, `name`, `surname`, `comp_name`) VALUES
	(1, 'mario.rossi@email.com', 'ciao', 'Mario', 'Rossi', 'Ferrero International S.A.'),
	(2, 'luigi.verdi@email.com', 'ciao', 'Luigi', 'Verdi', 'Ferrero International S.A.'),
	(3, 'giovanni.bianchi@email.com', 'ciao', 'Giovanni', 'Bianchi', 'The Coca-Cola Company'),
	(4, 'federico.azzurri@email.com', 'ciao', 'Federico', 'Azzurri', 'The Coca-Cola Company');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
