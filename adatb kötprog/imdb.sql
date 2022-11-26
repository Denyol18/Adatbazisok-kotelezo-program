-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2022. Nov 25. 16:40
-- Kiszolgáló verziója: 10.4.25-MariaDB
-- PHP verzió: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Adatbázis: `imdb`
--

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `ertekelesek`
--

CREATE TABLE `ertekelesek` (
  `felhasznalonev` varchar(50) NOT NULL,
  `film_id` int(3) NOT NULL,
  `uzenet` varchar(300) DEFAULT NULL,
  `pont` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `ertekelesek`
--

INSERT INTO `ertekelesek` (`felhasznalonev`, `film_id`, `uzenet`, `pont`) VALUES
('KeresztApu', 2, 'A legjobb film valaha!!!44!!4!', 10),
('MovieLover21', 3, 'Komplex, sötét és felejthetetlen! A legjobb képregény film valaha, ami megjárta a mozikat.', 10),
('MovieLover21', 8, 'Egyszerűen nem jön be Tarantino stílusa, nem tetszik a film.', 3);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `felhasznalok`
--

CREATE TABLE `felhasznalok` (
  `felhasznalonev` varchar(50) NOT NULL,
  `jelszo` varchar(25) DEFAULT NULL,
  `szuldatum` date DEFAULT NULL,
  `veznev` varchar(50) DEFAULT NULL,
  `kernev` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `felhasznalok`
--

INSERT INTO `felhasznalok` (`felhasznalonev`, `jelszo`, `szuldatum`, `veznev`, `kernev`) VALUES
('KeresztApu', 'godfather45', '1999-05-06', 'Szűcs', 'Bendegúz'),
('MovieLover21', 'asdfgh', '2002-11-01', 'Kiss', 'Jóska');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `filmek`
--

CREATE TABLE `filmek` (
  `film_id` int(3) NOT NULL,
  `cim` varchar(50) DEFAULT NULL,
  `jatekido` int(3) DEFAULT NULL,
  `bemutato` date DEFAULT NULL,
  `ertekeles` int(2) DEFAULT NULL,
  `forgalmazo_id` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `filmek`
--

INSERT INTO `filmek` (`film_id`, `cim`, `jatekido`, `bemutato`, `ertekeles`, `forgalmazo_id`) VALUES
(1, 'The Shawshank Redemption', 142, '1994-09-23', 9, 1),
(2, 'The Godfather', 175, '1972-03-24', 9, 2),
(3, 'The Dark Knight', 152, '2008-07-18', 9, 3),
(4, 'The Godfather Part II', 202, '1974-12-20', 9, 2),
(5, '12 Angry Men', 96, '1957-04-10', 9, 4),
(6, 'Schindler\'s List', 195, '1993-12-15', 9, 5),
(7, 'The Lord of the Rings: The Return of the King', 201, '2003-12-17', 9, 6),
(8, 'Pulp Fiction', 154, '1994-10-14', 9, 7),
(9, 'The Lord of the Rings: The Fellowship of the Ring', 178, '2001-12-19', 9, 6),
(10, 'The Good, the Bad and the Ugly', 161, '1966-12-23', 9, 8);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `filmek_mufajai`
--

CREATE TABLE `filmek_mufajai` (
  `film_id` int(3) NOT NULL,
  `mufaj` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `filmek_mufajai`
--

INSERT INTO `filmek_mufajai` (`film_id`, `mufaj`) VALUES
(1, 'Dráma'),
(2, 'Dráma'),
(2, 'Krimi'),
(3, 'Akció'),
(3, 'Dráma'),
(3, 'Krimi'),
(4, 'Dráma'),
(4, 'Krimi'),
(5, 'Dráma'),
(5, 'Krimi'),
(6, 'Dráma'),
(6, 'Életrajzi'),
(6, 'Történelmi'),
(7, 'Akció'),
(7, 'Dráma'),
(7, 'Kaland'),
(8, 'Dráma'),
(8, 'Krimi'),
(9, 'Akció'),
(9, 'Dráma'),
(9, 'Kaland'),
(10, 'Kaland'),
(10, 'Western');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `forgalmazok`
--

CREATE TABLE `forgalmazok` (
  `forgalmazo_id` int(3) NOT NULL,
  `nev` varchar(50) DEFAULT NULL,
  `alapitdatum` date DEFAULT NULL,
  `alapito` varchar(100) DEFAULT NULL,
  `kozpontorszag` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `forgalmazok`
--

INSERT INTO `forgalmazok` (`forgalmazo_id`, `nev`, `alapitdatum`, `alapito`, `kozpontorszag`) VALUES
(1, 'Columbia Pictures', '1924-01-10', 'Joe Brandt', 'Egyesült Államok'),
(2, 'Paramount Pictures', '1912-05-08', 'William Wadsworth Hodkinson', 'Egyesült Államok'),
(3, 'Warner Bros. Pictures', '1923-04-04', 'Harry Warner', 'Egyesült Államok'),
(4, 'United Artists', '1919-02-05', 'Mary Pickford', 'Egyesült Államok'),
(5, 'Universal Pictures', '1912-04-30', 'Carl Laemmle', 'Egyesült Államok'),
(6, 'New Line Cinema', '1967-06-18', 'Robert Shaye', 'Egyesült Államok'),
(7, 'Miramax', '1979-12-19', 'Harvey Weinstein', 'Egyesült Államok'),
(8, 'Produzioni Europee Associati', '1962-01-01', 'Alberto Grimaldi', 'Olaszország');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `gyartasok`
--

CREATE TABLE `gyartasok` (
  `gyarto_id` int(3) NOT NULL,
  `film_id` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `gyartasok`
--

INSERT INTO `gyartasok` (`gyarto_id`, `film_id`) VALUES
(1, 1),
(2, 2),
(2, 4),
(3, 3),
(4, 3),
(5, 3),
(6, 5),
(7, 6),
(8, 6),
(9, 7),
(9, 9),
(10, 7),
(10, 9),
(11, 8),
(12, 10),
(13, 10);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `gyartok`
--

CREATE TABLE `gyartok` (
  `gyarto_id` int(3) NOT NULL,
  `nev` varchar(50) DEFAULT NULL,
  `alapitdatum` date DEFAULT NULL,
  `alapito` varchar(100) DEFAULT NULL,
  `kozpontorszag` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `gyartok`
--

INSERT INTO `gyartok` (`gyarto_id`, `nev`, `alapitdatum`, `alapito`, `kozpontorszag`) VALUES
(1, 'Castle Rock Entertainment', '1987-06-19', 'Martin Shafer', 'Egyesült Államok'),
(2, 'Paramount Pictures', '1912-05-08', 'William Wadsworth Hodkinson', 'Egyesült Államok'),
(3, 'Warner Bros. Pictures', '1923-04-04', 'Harry Warner', 'Egyesült Államok'),
(4, 'Legendary Entertainment', '2000-01-01', 'Thomas Tull', 'Egyesült Államok'),
(5, 'Syncopy Inc.', '2001-02-27', 'Christopher Nolan', 'Egyesült Államok'),
(6, 'Orion-Nova Productions', NULL, NULL, NULL),
(7, 'Amblin Entertainment', '1980-01-01', 'Steven Spielberg', 'Egyesült Államok'),
(8, 'Universal Pictures', '1912-04-30', 'Carl Laemmle', 'Egyesült Államok'),
(9, 'New Line Cinema', '1967-06-18', 'Robert Shaye', 'Egyesült Államok'),
(10, 'WingNut Films', '1987-02-14', 'Peter Jackson', 'Új-Zéland'),
(11, 'A Band Apart', '1991-01-01', 'Quentin Tarantino', 'Egyesült Államok'),
(12, 'Produzioni Europee Associati', '1962-01-01', 'Alberto Grimaldi', 'Olaszország'),
(13, 'United Artists', '1919-02-05', 'Mary Pickford', 'Egyesült Államok');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `rendezesek`
--

CREATE TABLE `rendezesek` (
  `rendezo_id` int(3) NOT NULL,
  `film_id` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `rendezesek`
--

INSERT INTO `rendezesek` (`rendezo_id`, `film_id`) VALUES
(1, 1),
(2, 2),
(2, 4),
(3, 3),
(4, 5),
(5, 6),
(6, 7),
(6, 9),
(7, 8),
(8, 10);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `rendezok`
--

CREATE TABLE `rendezok` (
  `rendezo_id` int(3) NOT NULL,
  `veznev` varchar(50) DEFAULT NULL,
  `kernev` varchar(50) DEFAULT NULL,
  `szuldatum` date DEFAULT NULL,
  `nemzetiseg` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `rendezok`
--

INSERT INTO `rendezok` (`rendezo_id`, `veznev`, `kernev`, `szuldatum`, `nemzetiseg`) VALUES
(1, 'Darabont', 'Frank', '1959-01-28', 'francia'),
(2, 'Ford Coppola', 'Francis', '1939-04-07', 'amerikai'),
(3, 'Nolan', 'Christopher', '1970-07-30', 'brit'),
(4, 'Lumet', 'Sidney', '1924-06-25', 'amerikai'),
(5, 'Spielberg', 'Steven', '1946-12-18', 'amerikai'),
(6, 'Jackson', 'Peter', '1961-10-30', 'új-zélandi'),
(7, 'Tarantino', 'Quentin', '1963-03-27', 'amerikai'),
(8, 'Leone', 'Sergio', '1929-01-03', 'olasz');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `szereplesek`
--

CREATE TABLE `szereplesek` (
  `szinesz_id` int(3) NOT NULL,
  `film_id` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `szereplesek`
--

INSERT INTO `szereplesek` (`szinesz_id`, `film_id`) VALUES
(1, 1),
(2, 1),
(2, 3),
(3, 1),
(4, 2),
(5, 2),
(5, 4),
(6, 2),
(7, 3),
(8, 3),
(9, 3),
(10, 4),
(11, 4),
(12, 4),
(13, 5),
(14, 5),
(15, 5),
(16, 6),
(17, 6),
(18, 6),
(19, 7),
(19, 9),
(20, 7),
(20, 9),
(21, 7),
(21, 9),
(22, 8),
(23, 8),
(24, 8),
(25, 10),
(26, 10),
(27, 10);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `szineszek`
--

CREATE TABLE `szineszek` (
  `szinesz_id` int(3) NOT NULL,
  `veznev` varchar(50) DEFAULT NULL,
  `kernev` varchar(50) DEFAULT NULL,
  `szuldatum` date DEFAULT NULL,
  `nemzetiseg` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `szineszek`
--

INSERT INTO `szineszek` (`szinesz_id`, `veznev`, `kernev`, `szuldatum`, `nemzetiseg`) VALUES
(1, 'Robbins', 'Tim', '1958-10-16', 'amerikai'),
(2, 'Freeman', 'Morgan', '1937-06-01', 'amerikai'),
(3, 'Gurton', 'Bob', '1945-11-15', 'amerikai'),
(4, 'Brando', 'Marlon', '1924-04-03', 'amerikai'),
(5, 'Pacino', 'Al', '1940-04-25', 'amerikai'),
(6, 'Caan', 'James', '1940-03-26', 'amerikai'),
(7, 'Bale', 'Christian', '1974-01-30', 'brit'),
(8, 'Ledger', 'Heat', '1979-04-04', 'ausztrál'),
(9, 'Oldman', 'Gary', '1958-03-21', 'brit'),
(10, 'Duvall', 'Robert', '1931-01-05', 'amerikai'),
(11, 'Keaton', 'Diane', '1946-01-05', 'amerikai'),
(12, 'De Niro', 'Robert', '1943-08-17', 'amerikai'),
(13, 'Balsam', 'Martin', '1919-11-04', 'amerikai'),
(14, 'Fiedler', 'John', '1925-02-03', 'amerikai'),
(15, 'J. Cobb', 'Lee', '1911-12-08', 'amerikai'),
(16, 'Neeson ', 'Liam', '1952-06-07', 'brit'),
(17, 'Kingsley', 'Ben', '1943-12-31', 'brit'),
(18, 'Fiennes', 'Ralph', '1962-12-22', 'brit'),
(19, 'Wood', 'Elijah', '1981-01-28', 'amerikai'),
(20, 'McKellen', 'Ian', '1939-05-25', 'brit'),
(21, 'Mortensen', 'Viggo', '1958-10-20', 'amerikai'),
(22, 'Travolta', 'John', '1954-02-18', 'amerikai'),
(23, 'Jackson', 'Samuel', '1948-12-21', 'amerikai'),
(24, 'Thurman', 'Uma', '1970-04-29', 'amerikai'),
(25, 'Eastwood', 'Clint', '1930-05-31', 'amerikai'),
(26, 'Wallach', 'Eli', '1915-12-07', 'amerikai'),
(27, 'Van Cleef', 'Lee', '1925-01-09', 'amerikai');

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `ertekelesek`
--
ALTER TABLE `ertekelesek`
  ADD PRIMARY KEY (`felhasznalonev`,`film_id`),
  ADD KEY `felhasznalonev` (`felhasznalonev`,`film_id`),
  ADD KEY `ertekelesek_ibfk_1` (`film_id`);

--
-- A tábla indexei `felhasznalok`
--
ALTER TABLE `felhasznalok`
  ADD PRIMARY KEY (`felhasznalonev`);

--
-- A tábla indexei `filmek`
--
ALTER TABLE `filmek`
  ADD PRIMARY KEY (`film_id`),
  ADD KEY `forgalmazo_id` (`forgalmazo_id`);

--
-- A tábla indexei `filmek_mufajai`
--
ALTER TABLE `filmek_mufajai`
  ADD PRIMARY KEY (`film_id`,`mufaj`),
  ADD KEY `film_id` (`film_id`) USING BTREE;

--
-- A tábla indexei `forgalmazok`
--
ALTER TABLE `forgalmazok`
  ADD PRIMARY KEY (`forgalmazo_id`);

--
-- A tábla indexei `gyartasok`
--
ALTER TABLE `gyartasok`
  ADD PRIMARY KEY (`gyarto_id`,`film_id`),
  ADD KEY `gyarto_id` (`gyarto_id`,`film_id`),
  ADD KEY `film_id` (`film_id`);

--
-- A tábla indexei `gyartok`
--
ALTER TABLE `gyartok`
  ADD PRIMARY KEY (`gyarto_id`);

--
-- A tábla indexei `rendezesek`
--
ALTER TABLE `rendezesek`
  ADD PRIMARY KEY (`rendezo_id`,`film_id`),
  ADD KEY `rendezo_id` (`rendezo_id`,`film_id`),
  ADD KEY `film_id` (`film_id`);

--
-- A tábla indexei `rendezok`
--
ALTER TABLE `rendezok`
  ADD PRIMARY KEY (`rendezo_id`);

--
-- A tábla indexei `szereplesek`
--
ALTER TABLE `szereplesek`
  ADD PRIMARY KEY (`szinesz_id`,`film_id`),
  ADD KEY `szinesz_id` (`szinesz_id`,`film_id`),
  ADD KEY `film_id` (`film_id`);

--
-- A tábla indexei `szineszek`
--
ALTER TABLE `szineszek`
  ADD PRIMARY KEY (`szinesz_id`);

--
-- A kiírt táblák AUTO_INCREMENT értéke
--

--
-- AUTO_INCREMENT a táblához `filmek`
--
ALTER TABLE `filmek`
  MODIFY `film_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT a táblához `forgalmazok`
--
ALTER TABLE `forgalmazok`
  MODIFY `forgalmazo_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT a táblához `gyartok`
--
ALTER TABLE `gyartok`
  MODIFY `gyarto_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT a táblához `rendezok`
--
ALTER TABLE `rendezok`
  MODIFY `rendezo_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT a táblához `szineszek`
--
ALTER TABLE `szineszek`
  MODIFY `szinesz_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- Megkötések a kiírt táblákhoz
--

--
-- Megkötések a táblához `ertekelesek`
--
ALTER TABLE `ertekelesek`
  ADD CONSTRAINT `ertekelesek_ibfk_1` FOREIGN KEY (`film_id`) REFERENCES `filmek` (`film_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `ertekelesek_ibfk_2` FOREIGN KEY (`felhasznalonev`) REFERENCES `felhasznalok` (`felhasznalonev`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Megkötések a táblához `filmek`
--
ALTER TABLE `filmek`
  ADD CONSTRAINT `filmek_ibfk_1` FOREIGN KEY (`forgalmazo_id`) REFERENCES `forgalmazok` (`forgalmazo_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Megkötések a táblához `filmek_mufajai`
--
ALTER TABLE `filmek_mufajai`
  ADD CONSTRAINT `filmek_mufajai_ibfk_1` FOREIGN KEY (`film_id`) REFERENCES `filmek` (`film_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Megkötések a táblához `gyartasok`
--
ALTER TABLE `gyartasok`
  ADD CONSTRAINT `gyartasok_ibfk_1` FOREIGN KEY (`gyarto_id`) REFERENCES `gyartok` (`gyarto_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `gyartasok_ibfk_2` FOREIGN KEY (`film_id`) REFERENCES `filmek` (`film_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Megkötések a táblához `rendezesek`
--
ALTER TABLE `rendezesek`
  ADD CONSTRAINT `rendezesek_ibfk_1` FOREIGN KEY (`rendezo_id`) REFERENCES `rendezok` (`rendezo_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `rendezesek_ibfk_2` FOREIGN KEY (`film_id`) REFERENCES `filmek` (`film_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Megkötések a táblához `szereplesek`
--
ALTER TABLE `szereplesek`
  ADD CONSTRAINT `szereplesek_ibfk_1` FOREIGN KEY (`szinesz_id`) REFERENCES `szineszek` (`szinesz_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `szereplesek_ibfk_2` FOREIGN KEY (`film_id`) REFERENCES `filmek` (`film_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
