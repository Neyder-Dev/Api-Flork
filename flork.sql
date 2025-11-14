-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-11-2025 a las 01:21:16
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `flork`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `favoritos`
--

CREATE TABLE `favoritos` (
  `id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `receta_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `favoritos`
--

INSERT INTO `favoritos` (`id`, `usuario_id`, `receta_id`) VALUES
(2, 1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `recetas`
--

CREATE TABLE `recetas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `imagen_url` varchar(255) NOT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  `descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `recetas`
--

INSERT INTO `recetas` (`id`, `nombre`, `imagen_url`, `categoria`, `descripcion`) VALUES
(1, 'Galletas de avena y banano', 'https://raw.githubusercontent.com/Neyder-Dev/Api-Flork/d9e08df5f0b7b4938cb06013119121cca6512020/images/banana%20oat%20cookies.jpg', 'Desayuno', 'Galletas saludables hechas con avena y banano.'),
(2, 'Tostadas francesas con miel', 'https://raw.githubusercontent.com/Neyder-Dev/Api-Flork/refs/heads/master/images/french%20toast%20honey.jpg', 'Desayuno', 'Pan dorado con mantequilla, canela y miel natural.'),
(3, 'Emparedado de aguacate y huevo', 'https://raw.githubusercontent.com/Neyder-Dev/Api-Flork/refs/heads/master/images/avocado%20egg%20toast.jpg', 'Desayuno', 'Tostada con aguacate cremoso y huevo suave.'),
(4, 'Pasta cremosa con pollo', 'https://raw.githubusercontent.com/Neyder-Dev/Api-Flork/refs/heads/master/images/creamy%20chicken%20pasta.jpg', 'Almuerzo', 'Pasta en salsa cremosa con trozos de pollo.'),
(5, 'Arroz con pollo casero', 'https://raw.githubusercontent.com/Neyder-Dev/Api-Flork/refs/heads/master/images/chicken%20rice%20homemade.jpg', 'Almuerzo', 'Receta tradicional casera con pollo jugoso.'),
(6, 'Wrap de pollo con vegetales', 'https://raw.githubusercontent.com/Neyder-Dev/Api-Flork/refs/heads/master/images/chicken%20veggie%20wrap.jpg', 'Almuerzo', 'Wrap ligero con pollo, lechuga y tomate.'),
(7, 'Sopa ligera de verduras', 'https://raw.githubusercontent.com/Neyder-Dev/Api-Flork/refs/heads/master/images/vegetable%20soup%20bowl.jpg', 'Cena', 'Sopa suave y saludable con vegetales frescos.'),
(8, 'Pechuga a la plancha con ensalada', 'https://raw.githubusercontent.com/Neyder-Dev/Api-Flork/refs/heads/master/images/grilled%20chicken%20salad.jpg', 'Cena', 'Pechuga dorada acompañada de ensalada fresca.'),
(9, 'Tortilla de espinacas y queso', 'https://raw.githubusercontent.com/Neyder-Dev/Api-Flork/refs/heads/master/images/spinach%20cheese%20omelette.jpg', 'Cena', 'Tortilla suave con espinacas y queso fundido.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `acepta_terminos` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `correo`, `password`, `fecha_nacimiento`, `acepta_terminos`) VALUES
(1, 'Admin', 'a@a.com', '$argon2id$v=19$m=65536,t=3,p=4$wJjTOue8935PqXWOMYbwng$c79tZEyq/U5pmcW+rZhwgYdhKxQv4gaQu0IW1pyk7LY', '2025-11-13', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `favoritos`
--
ALTER TABLE `favoritos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario_id` (`usuario_id`,`receta_id`),
  ADD KEY `receta_id` (`receta_id`);

--
-- Indices de la tabla `recetas`
--
ALTER TABLE `recetas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_recetas_id` (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_usuarios_correo` (`correo`),
  ADD KEY `ix_usuarios_id` (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `favoritos`
--
ALTER TABLE `favoritos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `recetas`
--
ALTER TABLE `recetas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `favoritos`
--
ALTER TABLE `favoritos`
  ADD CONSTRAINT `favoritos_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `favoritos_ibfk_2` FOREIGN KEY (`receta_id`) REFERENCES `recetas` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
