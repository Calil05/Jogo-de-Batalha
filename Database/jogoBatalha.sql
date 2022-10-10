/*
SQLyog Ultimate
MySQL - 5.5.28 : Database - jogo_batalha
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
/*Table structure for table `easy_enemies` */

DROP TABLE IF EXISTS `easy_enemies`;

CREATE TABLE `easy_enemies` (
  `easy_Code` int(11) NOT NULL AUTO_INCREMENT,
  `easy_Nome` varchar(50) NOT NULL,
  `easy_Hp` int(11) NOT NULL,
  `easy_Forca` int(11) NOT NULL,
  `easy_Defesa` int(11) NOT NULL,
  `easy_Agilidade` int(11) NOT NULL,
  `easy_Arma` int(11) NOT NULL,
  PRIMARY KEY (`easy_Code`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `easy_enemies` */

insert  into `easy_enemies`(`easy_Code`,`easy_Nome`,`easy_Hp`,`easy_Forca`,`easy_Defesa`,`easy_Agilidade`,`easy_Arma`) values 
(1,'Rato Gigante',40,25,20,30,5),
(2,'Slime',40,15,35,5,15),
(3,'Cobra',70,20,15,30,10),
(4,'O Baratão',80,10,20,10,7),
(5,'Aranha',30,15,10,15,15);

/*Table structure for table `hard_enemies` */

DROP TABLE IF EXISTS `hard_enemies`;

CREATE TABLE `hard_enemies` (
  `hard_Code` int(11) NOT NULL AUTO_INCREMENT,
  `hard_Nome` varchar(50) NOT NULL,
  `hard_Hp` int(11) NOT NULL,
  `hard_Forca` int(11) NOT NULL,
  `hard_Defesa` int(11) NOT NULL,
  `hard_Agilidade` int(11) NOT NULL,
  `hard_Arma` int(11) NOT NULL,
  PRIMARY KEY (`hard_Code`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `hard_enemies` */

insert  into `hard_enemies`(`hard_Code`,`hard_Nome`,`hard_Hp`,`hard_Forca`,`hard_Defesa`,`hard_Agilidade`,`hard_Arma`) values 
(1,'Ogroide',100,40,30,10,15),
(2,'Minotauro',90,50,35,25,20),
(3,'Serpente Voadora',50,70,15,50,18),
(4,'A Baleia',250,10,65,5,5),
(5,'Ciclope',150,45,70,12,25);

/*Table structure for table `items` */

DROP TABLE IF EXISTS `items`;

CREATE TABLE `items` (
  `item_Code` int(11) NOT NULL AUTO_INCREMENT,
  `item_Nome` varchar(50) NOT NULL,
  `item_Preco` int(11) NOT NULL,
  `item_Descricao` varchar(100) NOT NULL,
  PRIMARY KEY (`item_Code`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `items` */

insert  into `items`(`item_Code`,`item_Nome`,`item_Preco`,`item_Descricao`) values 
(1,'Poção',30,'Recupera 30 de HP'),
(2,'Poção Grande',85,'Recupera 85 de HP'),
(3,'Poção Maxima',200,'Recupera todo o HP'),
(4,'Scanner',70,'Vizualiza os Status de um Inimigo'),
(5,'Seletor',300,'Seleciona o proximo Inimigo');

/*Table structure for table `medium_enemies` */

DROP TABLE IF EXISTS `medium_enemies`;

CREATE TABLE `medium_enemies` (
  `medium_Code` int(11) NOT NULL AUTO_INCREMENT,
  `medium_Nome` varchar(50) NOT NULL,
  `medium_Hp` int(11) NOT NULL,
  `medium_Forca` int(11) NOT NULL,
  `medium_Defesa` int(11) NOT NULL,
  `medium_Agilidade` int(11) NOT NULL,
  `medium_Arma` int(11) NOT NULL,
  PRIMARY KEY (`medium_Code`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `medium_enemies` */

insert  into `medium_enemies`(`medium_Code`,`medium_Nome`,`medium_Hp`,`medium_Forca`,`medium_Defesa`,`medium_Agilidade`,`medium_Arma`) values 
(1,'Tigre',65,30,20,23,10),
(2,'Esqueleto',30,60,20,35,13),
(3,'Lartaguixa',40,30,25,45,5),
(4,'Zumbi',60,70,15,5,15),
(5,'Centauro',130,20,40,3,10);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
