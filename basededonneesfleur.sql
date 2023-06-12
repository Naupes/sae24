-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mer. 10 mai 2023 à 22:42
-- Version du serveur : 8.0.31
-- Version de PHP : 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `fleur`
--

-- --------------------------------------------------------

--
-- Structure de la table `amateurs`
--

DROP TABLE IF EXISTS `amateurs`;
CREATE TABLE IF NOT EXISTS `amateurs` (
  `numAmateur` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(30) DEFAULT NULL,
  `prenom` varchar(30) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `resi_ville` varchar(30) DEFAULT NULL,
  `resi_region` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`numAmateur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Structure de la table `evenements`
--

DROP TABLE IF EXISTS `evenements`;
CREATE TABLE IF NOT EXISTS `evenements` (
  `numEvenement` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `lieu` varchar(30) NOT NULL,
  `nb_participants` int DEFAULT NULL,
  `numLieu` int NOT NULL,
  PRIMARY KEY (`numEvenement`),
  KEY `numLieu` (`numLieu`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Structure de la table `fleurs`
--

DROP TABLE IF EXISTS `fleurs`;
CREATE TABLE IF NOT EXISTS `fleurs` (
  `nbFleur` int NOT NULL AUTO_INCREMENT,
  `couleur` enum('bleu','rouge','vert') NOT NULL DEFAULT 'rouge',
  `nom` varchar(20) DEFAULT NULL,
  `petales` int DEFAULT NULL,
  `taille` int DEFAULT NULL,
  `typetige` varchar(10) DEFAULT NULL,
  `eclosion` date DEFAULT NULL,
  `saison` enum('Printemps','Été','Automne','Hiver') DEFAULT NULL,
  PRIMARY KEY (`nbFleur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Structure de la table `lieu`
--

DROP TABLE IF EXISTS `lieu`;
CREATE TABLE IF NOT EXISTS `lieu` (
  `numLieu` int NOT NULL AUTO_INCREMENT,
  `region` varchar(20) DEFAULT NULL,
  `coordonnees` varchar(30) DEFAULT NULL,
  `departement` varchar(30) DEFAULT NULL,
  `ville` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`numLieu`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Structure de la table `participer_a`
--

DROP TABLE IF EXISTS `participer_a`;
CREATE TABLE IF NOT EXISTS `participer_a` (
  `cleevenement` int NOT NULL,
  `cleamateur` int NOT NULL,
  PRIMARY KEY (`cleevenement`,`cleamateur`),
  KEY `cleamateur` (`cleamateur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Structure de la table `se_situer`
--

DROP TABLE IF EXISTS `se_situer`;
CREATE TABLE IF NOT EXISTS `se_situer` (
  `clefleur` int NOT NULL,
  `clelieu` int NOT NULL,
  `cardinaux` enum('Nord','Sud','Est','Ouest') DEFAULT NULL,
  PRIMARY KEY (`clefleur`,`clelieu`),
  KEY `clelieu` (`clelieu`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `evenements`
--
ALTER TABLE `evenements`
  ADD CONSTRAINT `evenements_ibfk_1` FOREIGN KEY (`numLieu`) REFERENCES `lieu` (`numLieu`) ON UPDATE CASCADE;

--
-- Contraintes pour la table `participer_a`
--
ALTER TABLE `participer_a`
  ADD CONSTRAINT `participer_a_ibfk_1` FOREIGN KEY (`cleevenement`) REFERENCES `evenements` (`numEvenement`) ON UPDATE CASCADE,
  ADD CONSTRAINT `participer_a_ibfk_2` FOREIGN KEY (`cleamateur`) REFERENCES `amateurs` (`numAmateur`) ON UPDATE CASCADE;

--
-- Contraintes pour la table `se_situer`
--
ALTER TABLE `se_situer`
  ADD CONSTRAINT `se_situer_ibfk_1` FOREIGN KEY (`clefleur`) REFERENCES `fleurs` (`nbFleur`) ON UPDATE CASCADE,
  ADD CONSTRAINT `se_situer_ibfk_2` FOREIGN KEY (`clelieu`) REFERENCES `lieu` (`numLieu`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
