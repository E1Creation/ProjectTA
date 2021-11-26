-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 23, 2021 at 12:44 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_recognition`
--

-- --------------------------------------------------------

--
-- Table structure for table `pengunjung`
--

CREATE TABLE `pengunjung` (
  `nim` varchar(25) NOT NULL,
  `nama` varchar(30) NOT NULL,
  `pekerjaan` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pengunjung`
--

INSERT INTO `pengunjung` (`nim`, `nama`, `pekerjaan`) VALUES
('12', 'Namira Aulia', 'Mahasiswa'),
('123', 'Fadilah Hafis', 'siswa'),
('1234', 'Rassya Hilabih', 'siswa'),
('12345', 'Alvira Sudirman', 'Mahasiswa'),
('21060117130098', 'Alam Suminto', 'Mahasiswa'),
('21060117140080', 'Kurniawan Sudirman', 'mahasiswa');

-- --------------------------------------------------------

--
-- Table structure for table `rlabkom`
--

CREATE TABLE `rlabkom` (
  `nim` varchar(100) NOT NULL,
  `tanggal` varchar(15) NOT NULL,
  `nama` varchar(25) NOT NULL,
  `waktu` varchar(15) NOT NULL,
  `status` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rlabkom`
--

INSERT INTO `rlabkom` (`nim`, `tanggal`, `nama`, `waktu`, `status`) VALUES
('123', '17-07-21', 'FADILAH HAFIS', '21:26:01', 'masuk'),
('1234', '26-07-21', 'RASSYA HILABIH', '18:44:17', 'masuk'),
('21060117140080', '26-07-21', 'KURNIAWAN SUDIRMAN', '18:44:22', 'masuk');

-- --------------------------------------------------------

--
-- Table structure for table `rlabkom2`
--

CREATE TABLE `rlabkom2` (
  `id` varchar(100) NOT NULL,
  `tanggal` varchar(25) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `waktu` varchar(25) NOT NULL,
  `status` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rlabkom2`
--

INSERT INTO `rlabkom2` (`id`, `tanggal`, `nama`, `waktu`, `status`) VALUES
('10', '23-10-21', 'kurniawan sudirman', '17:31:33', 'masuk');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pengunjung`
--
ALTER TABLE `pengunjung`
  ADD PRIMARY KEY (`nim`);

--
-- Indexes for table `rlabkom`
--
ALTER TABLE `rlabkom`
  ADD PRIMARY KEY (`nim`);

--
-- Indexes for table `rlabkom2`
--
ALTER TABLE `rlabkom2`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
