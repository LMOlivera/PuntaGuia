-- phpMyAdmin SQL Dump
-- version 3.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 14-03-2019 a las 23:20:11
-- Versión del servidor: 5.5.24-log
-- Versión de PHP: 5.4.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `uruguia_bd_test`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `agrega_a_lista`
--

CREATE TABLE IF NOT EXISTS `agrega_a_lista` (
  `id` int(11) NOT NULL,
  `ide` int(11) NOT NULL,
  `orden` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE IF NOT EXISTS `categoria` (
  `idc` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`idc`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`idc`, `nombre`) VALUES
(1, 'Al aire libre'),
(2, 'Restaurante'),
(3, 'Tienda'),
(4, 'Otro');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empresa`
--

CREATE TABLE IF NOT EXISTS `empresa` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `empresa`
--

INSERT INTO `empresa` (`id`, `nombre`) VALUES
(3, 'Empresa de Test 3'),
(4, 'Empresa de Test 4');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lugar`
--

CREATE TABLE IF NOT EXISTS `lugar` (
  `ide` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(1000) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `ubicacion` varchar(100) NOT NULL,
  `tipo` varchar(20) NOT NULL,
  `horario` varchar(100) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  PRIMARY KEY (`ide`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- Volcado de datos para la tabla `lugar`
--

INSERT INTO `lugar` (`ide`, `nombre`, `descripcion`, `imagen`, `ubicacion`, `tipo`, `horario`, `fecha`) VALUES
(1, 'Establecimiento Empresa 3', 'Un lugar lindo para pasar con la familia.', NULL, 'Un lugar muy lindo', 'Establecimiento', '8:00 a 20:00', '0000-00-00'),
(2, 'Evento Empresa 3', 'AAAA', NULL, 'Alguna parte', 'Evento', 'Todo el día', '0000-00-00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pertenece_a`
--

CREATE TABLE IF NOT EXISTS `pertenece_a` (
  `ide` int(11) NOT NULL,
  `idc` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `pertenece_a`
--

INSERT INTO `pertenece_a` (`ide`, `idc`) VALUES
(1, 1),
(2, 4),
(3, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiene`
--

CREATE TABLE IF NOT EXISTS `tiene` (
  `ide` int(11) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `tiene`
--

INSERT INTO `tiene` (`ide`, `id`) VALUES
(1, 3),
(2, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `turista`
--

CREATE TABLE IF NOT EXISTS `turista` (
  `id` int(11) NOT NULL,
  `edad` int(11) NOT NULL,
  `pais_origen` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `turista`
--

INSERT INTO `turista` (`id`, `edad`, `pais_origen`) VALUES
(1, 20, 'Pais de prueba'),
(2, 44, 'PaisDePrueba2');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE IF NOT EXISTS `usuario` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `contrasena` varchar(100) NOT NULL,
  `foto` varchar(100) DEFAULT NULL,
  `tipo` varchar(100) NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `email_2` (`email`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `email`, `nombre`, `contrasena`, `foto`, `tipo`) VALUES
(1, 'test1@test1.com', 'Test 1 Turista', '123', NULL, 'turista'),
(2, 'test2@test2.com', 'Test 2 Turista', '123', NULL, 'turista'),
(3, 'test3@test3.com', 'Test 3 Empresa', '123', NULL, 'empresa'),
(4, 'test4@test4.com', 'Test 4 Empresa', '123', NULL, 'empresa');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `visito`
--

CREATE TABLE IF NOT EXISTS `visito` (
  `id` int(11) NOT NULL,
  `ide` int(11) NOT NULL,
  `calificacion` int(11) DEFAULT NULL,
  `comentario` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
