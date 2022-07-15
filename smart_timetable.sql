-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Jul 10, 2022 at 09:42 PM
-- Server version: 5.7.34
-- PHP Version: 7.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `smart_timetable`
--

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`id`, `name`) VALUES
(1, 'CAE'),
(2, 'CSE'),
(3, 'ENG'),
(4, 'FND'),
(5, 'NRE'),
(6, 'PIR'),
(7, 'SME');

-- --------------------------------------------------------

--
-- Table structure for table `group_`
--

CREATE TABLE `group_` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `group_`
--

INSERT INTO `group_` (`id`, `name`) VALUES
(1, 'CIE'),
(2, 'CE1/SE1/CS1'),
(3, 'CE2/SE2/CS2'),
(4, 'CS/SE'),
(5, 'CE'),
(6, 'CS'),
(7, 'SE'),
(8, 'CE'),
(9, 'ENG'),
(10, 'FND'),
(11, 'PE'),
(12, 'GPDS'),
(13, 'PIR'),
(14, 'BMEF1'),
(15, 'BMEF2'),
(16, 'BM'),
(17, 'EF'),
(18, 'CS/CE'),
(19, 'CE/CS/SE');

-- --------------------------------------------------------

--
-- Table structure for table `lecturer`
--

CREATE TABLE `lecturer` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lecturer`
--

INSERT INTO `lecturer` (`id`, `name`) VALUES
(1, 'Kamran Panaghi'),
(2, 'Ahmed Nareman'),
(3, 'Faroojan Siakian'),
(4, 'Alan Collins'),
(5, 'Hawkar Abdulhaq'),
(6, 'VL'),
(7, 'Bootan Rahman'),
(8, 'Sarfraz Munir'),
(9, 'Seyed M Ghasimi'),
(10, 'Lone Goulani'),
(11, 'Sarbaz Hamza'),
(12, 'Kamal Memehrashi'),
(13, 'Idris Musa'),
(14, 'Abbas Yeganeh'),
(15, 'Wrya Monnet'),
(16, 'Rawan Al-Rashid'),
(18, 'Fattah Alizadeh'),
(19, 'Tarik Rashid'),
(20, 'Ibrahim Hamad'),
(21, 'Govand Kadir'),
(22, 'Birzo Ismael'),
(23, 'Rabi Habash'),
(24, 'Tarik Ahmed'),
(25, 'Hossein Hassani'),
(26, 'Zana Ibrahim'),
(27, 'Victoria Whiteside'),
(28, 'Matthew Lambert'),
(29, 'Joseph Greenwood'),
(30, 'Kirstin Crawford'),
(31, 'Sahar Zarza'),
(32, 'Ergin Opengin'),
(33, 'Pierrine Bouchet'),
(34, 'Jana Kosemund'),
(35, 'Isabel Kaser'),
(36, 'Iman Ahmed'),
(37, 'Paul Dirk Embery'),
(38, 'Ararat Rahimy'),
(39, 'Abdullah Awdal'),
(40, 'Ramyar Suramairy'),
(41, 'Ala Ghafur'),
(42, 'Maha Hamoudi'),
(43, 'Akram Hamoodi'),
(44, 'Rubar Dizayee'),
(45, 'Sarhad Farkha'),
(46, 'Baroz Aziz'),
(47, 'Andrew Shaben'),
(48, 'Arzu Yilmaz'),
(49, 'Sara Mustafa'),
(50, 'Giovanni Mascaretti'),
(51, 'Nigel Greaves'),
(52, 'Mohammed Bapir'),
(53, 'Hemin Mirkhan'),
(54, 'Bayar Mustafa'),
(55, 'Goran Mustafa'),
(56, 'Jegr Nadhim'),
(57, 'George Tasie'),
(58, 'Ghaith Abdullah'),
(59, 'Ebrahim Mansoori'),
(60, 'Rebin Al-Silefanee'),
(61, 'Kym F');

-- --------------------------------------------------------

--
-- Table structure for table `level`
--

CREATE TABLE `level` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `level`
--

INSERT INTO `level` (`id`, `name`) VALUES
(1, 'UG1'),
(2, 'UG2'),
(3, 'UG3'),
(4, 'UG4'),
(5, 'UG5'),
(6, 'B1'),
(7, 'B1+'),
(8, 'B2'),
(9, 'A2\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `major`
--

CREATE TABLE `major` (
  `id` int(11) NOT NULL,
  `department_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `major`
--

INSERT INTO `major` (`id`, `department_id`, `name`) VALUES
(2, 1, 'CIE'),
(3, 2, 'CSE'),
(4, 2, 'CS'),
(5, 2, 'CE'),
(6, 3, 'ENG'),
(7, 4, 'FND'),
(8, 5, 'PE'),
(9, 6, 'GPDS'),
(10, 6, 'PIR'),
(11, 7, 'BM'),
(12, 7, 'EF'),
(13, 2, 'CSE'),
(14, 7, 'BMEF');

-- --------------------------------------------------------

--
-- Table structure for table `major_level`
--

CREATE TABLE `major_level` (
  `id` int(11) NOT NULL,
  `major_id` int(11) NOT NULL,
  `level_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `major_level`
--

INSERT INTO `major_level` (`id`, `major_id`, `level_id`) VALUES
(1, 2, 1),
(2, 2, 2),
(3, 2, 3),
(4, 2, 4),
(5, 5, 1),
(6, 5, 2),
(7, 5, 3),
(8, 5, 4),
(9, 4, 1),
(10, 4, 2),
(11, 4, 3),
(12, 4, 4),
(13, 3, 1),
(14, 3, 2),
(15, 3, 3),
(16, 3, 4),
(17, 6, 1),
(18, 6, 2),
(19, 6, 3),
(20, 6, 4),
(21, 8, 1),
(22, 8, 2),
(23, 8, 3),
(24, 8, 4),
(25, 9, 1),
(26, 10, 2),
(27, 10, 3),
(28, 10, 4),
(29, 14, 1),
(30, 14, 2),
(31, 14, 3),
(32, 14, 4),
(33, 11, 1),
(34, 12, 1),
(35, 11, 2),
(36, 12, 2),
(37, 11, 3),
(38, 12, 3),
(39, 11, 4),
(40, 12, 4);

-- --------------------------------------------------------

--
-- Table structure for table `major_level_module`
--

CREATE TABLE `major_level_module` (
  `module_code` varchar(20) NOT NULL,
  `major_level_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `no_of_students` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `major_level_module`
--

INSERT INTO `major_level_module` (`module_code`, `major_level_id`, `group_id`, `no_of_students`) VALUES
('CIE101', 1, 1, 9),
('CIE106', 1, 1, 8),
('CIE201', 1, 1, 9),
('ENG201', 1, 1, 8),
('MAT103', 1, 1, 9),
('CIE202', 2, 1, 16),
('CIE306', 2, 1, 16),
('ENG215', 2, 1, 16),
('MAT101', 2, 1, 16),
('MAT204', 2, 1, 16),
('CIE301', 3, 1, 23),
('CIE304', 3, 1, 23),
('CIE309', 3, 1, 23),
('CIE310', 3, 1, 23),
('CIE311', 3, 1, 23),
('CIE410', 4, 1, 5),
('CIE408', 4, 1, 5),
('CIE409', 4, 1, 5),
('CIE415', 4, 1, 5),
('CSE104', 13, 2, 34),
('CSE107', 13, 2, 34),
('ENG201', 13, 2, 34),
('MAT103', 13, 2, 34),
('CSE104', 13, 3, 35),
('CSE107', 13, 3, 35),
('ENG201', 13, 3, 34),
('MAT103', 13, 3, 35),
('CSE208', 14, 4, 24),
('ENG215', 14, 2, 29),
('MAT101', 14, 4, 24),
('MAT105', 14, 2, 29),
('CE202', 14, 8, 5),
('CE206', 14, 8, 5),
('CS304', 15, 4, 14),
('CS305', 15, 6, 7),
('CSE302', 15, 4, 14),
('CSE303', 15, 18, 15),
('SE302', 15, 7, 7),
('CE302', 15, 8, 8),
('CE303', 15, 8, 8),
('CS404', 16, 6, 3),
('CS405', 16, 6, 3),
('CS401', 16, 2, 25),
('SE404', 16, 7, 8),
('SE405', 16, 7, 8),
('CE403', 16, 8, 14),
('CE401', 16, 8, 14),
('ENG116', 17, 9, 20),
('ENG117', 17, 9, 20),
('ENG118', 17, 9, 21),
('ENG119', 17, 9, 20),
('ENG115', 17, 9, 20),
('ENG209', 18, 9, 19),
('ENG212', 18, 9, 19),
('ENG219', 18, 9, 19),
('ENG218', 18, 9, 19),
('ENG213', 18, 9, 9),
('ENG214', 18, 9, 8),
('ENG305', 19, 9, 24),
('ENG306', 19, 9, 24),
('ENG307', 19, 9, 24),
('ENG308', 19, 9, 24),
('ENG309', 19, 9, 24),
('ENG223', 19, 9, 3),
('ENG220', 19, 9, 6),
('ENG201', 21, 11, 11),
('MAT101', 21, 11, 10),
('MAT103', 21, 10, 10),
('NRE104', 21, 11, 10),
('NRE105', 21, 11, 10),
('NRE107', 21, 11, 15),
('ENG215', 22, 11, 15),
('MAT202', 22, 11, 15),
('PE202', 22, 11, 15),
('PE203', 22, 11, 15),
('PE204', 22, 11, 15),
('PE205', 22, 11, 15),
('PE304', 23, 11, 16),
('PE305', 23, 11, 15),
('PE306', 23, 11, 15),
('PE307', 23, 11, 15),
('PE405', 24, 11, 13),
('PE406', 24, 11, 13),
('PE407', 24, 11, 13),
('PIR101', 25, 12, 23),
('PIR105', 25, 12, 24),
('PIR109', 25, 12, 25),
('PIR116', 25, 12, 24),
('PIR118', 25, 12, 24),
('PIR210', 26, 13, 17),
('PIR215', 26, 13, 17),
('PIR211', 26, 13, 17),
('PIR220', 26, 13, 17),
('ENG223', 26, 13, 4),
('PIR312', 27, 13, 7),
('PIR314', 27, 13, 7),
('PIR316', 27, 13, 7),
('PIR317', 27, 13, 7),
('PIR318', 27, 13, 7),
('PIR405', 28, 13, 14),
('PIR409', 28, 13, 14),
('PIR407', 28, 13, 14),
('PIR410', 28, 13, 14),
('PIR412', 28, 13, 14),
('BMS118', 29, 14, 29),
('BMS118', 29, 15, 29),
('SOB102', 29, 14, 29),
('SOB102', 29, 15, 30),
('SOB103', 29, 14, 29),
('SOB103', 29, 15, 31),
('SOB105', 29, 14, 29),
('SOB105', 29, 15, 30),
('BM203', 35, 16, 21),
('BMS203', 35, 16, 22),
('BMS204', 30, 14, 33),
('ENG201', 30, 14, 33),
('EF203', 36, 17, 11),
('EF208', 36, 17, 11),
('BMS301', 37, 16, 29),
('BMS303', 37, 16, 28),
('BMS304', 31, 14, 36),
('BMS401', 31, 14, 35),
('EF303', 38, 17, 2),
('EF304', 38, 17, 3),
('BM402', 39, 16, 31),
('BM403', 39, 16, 31),
('BM405', 39, 16, 31),
('EF405', 40, 17, 6),
('EF408', 40, 17, 6),
('CSE201', 14, 19, 29);

-- --------------------------------------------------------

--
-- Table structure for table `module`
--

CREATE TABLE `module` (
  `code` varchar(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `lecturer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `module`
--

INSERT INTO `module` (`code`, `name`, `lecturer_id`) VALUES
('BM203', 'HUMAN RESOURCE MANAGEGEMNT', 57),
('BM402', 'GRAD RESEARCH', 61),
('BM403', 'STRATEGIC MANAGEMENT', 58),
('BM405', 'MANAGERIAL ACCOUNTING', 6),
('BMS118', 'ENG FOR PROS', 34),
('BMS203', 'ORG THEORY', 53),
('BMS204', 'INFO SYSTEMS', 23),
('BMS301', 'SERVICE MARKETING', 58),
('BMS303', 'INT BUSINESS', 53),
('BMS304', 'FINANCIAL MANAGEMENT', 59),
('BMS401', 'COST ACCOUNTING', 6),
('CE202', 'signals and systems', 20),
('CE206', 'digital and analogue electronics', 21),
('CE302', 'Programmable devices', 21),
('CE303', 'Digital image processing', 18),
('CE401', 'modeling and simulation', 24),
('CE403', 'industrial computer applications', 15),
('CIE101', 'Statics', 1),
('CIE106', 'Civil Engineering Drawing and Graphics', 2),
('CIE201', 'BUILDING MATERIALS FOR TESTING', 4),
('CIE202', 'Fluid Mechanics', 8),
('CIE207', 'Building Materials and Testing', 4),
('CIE301', 'Design of Reinforced Concrete Structures', 13),
('CIE304', 'Hydraulics', 14),
('CIE306', 'Environmental Engineering ', 9),
('CIE309', 'Research Methodology', 9),
('CIE310', 'Introduction to Earthquake Engineering', 1),
('CIE311', 'Foundation Engineering', 1),
('CIE408', 'Project Management', 4),
('CIE409', 'Hydraulic Structures', 14),
('CIE410', 'Professional Practice and Ethics', 14),
('CIE415', 'Bridge Engineering', 13),
('CS304', 'Web technologies', 22),
('CS305', 'Information theory', 23),
('CS401', 'Artificial intelligence', 19),
('CS404', 'distributed systems', 22),
('CS405', 'data mining', 24),
('CSE104', 'Intro to digital logic and electronics', 15),
('CSE107', 'Structured programming', 16),
('CSE201', 'OOP', 18),
('CSE208', 'algorithm design and analysis', 19),
('CSE302', 'operating systems', 23),
('CSE303', 'project management and group project', 19),
('EF203', 'MATH FOR ECONOMICS', 11),
('EF208', 'INT TRADE THEORY', 55),
('EF303', 'ENV ECONOMICS', 55),
('EF304', 'ECONOMETRICS', 60),
('EF405', 'ECONOMETRICS 2', 60),
('EF408', 'MONEY AND BANKING', 6),
('ENG115', 'english study skills and critical thinking', 30),
('ENG116', 'Academic listening and speaking 2', 26),
('ENG117', 'reading comp and voc', 27),
('ENG118', 'english grammer and comp', 28),
('ENG119', 'introduction to literature ', 29),
('ENG201', 'English Composition 2', 6),
('ENG209', 'english literature', 29),
('ENG212', 'ESL teaching practice', 31),
('ENG213', 'french 101', 33),
('ENG214', 'german 101', 34),
('ENG215', 'Public Speaking and Engagement ', 10),
('ENG218', 'introducation to translation studies', 32),
('ENG219', 'academic debate and speaking', 30),
('ENG220', 'german 103', 34),
('ENG223', 'french 103', 33),
('ENG305', 'contemporary english ', 29),
('ENG306', 'sociolinguistics', 32),
('ENG307', 'instructions and classroom management', 31),
('ENG308', 'consecutive interpreting', 26),
('ENG309', 'gender and politics in the middle east', 35),
('FND 261', 'ACADEMIC READING', 28),
('FND222', 'ACADEMIC WRITING', 36),
('FND223', 'GENERAL LANG DEV', 36),
('FND225', 'EXAM PREP', 37),
('FND241', 'ACADEMIC READING', 30),
('FND242', 'ACADEMIC WRITING', 28),
('FND243', 'GENERAL LANG DEV', 37),
('FND245', 'EXAM PREP', 36),
('FND251', 'ACADEMIC READING', 28),
('FND252', 'ACADEMIC WRITING', 27),
('FND253', 'GEN LANG DEV', 27),
('FND255', 'EXAMP PREP', 37),
('FND262', 'ACADEMIC WRITING', 30),
('FND263', 'GEN LANG DEV', 28),
('FND265', 'EXAM PREP', 37),
('MAT003', 'FOUND MATH', 38),
('MAT004', 'FOUNDATION MATH', 38),
('MAT101', 'Probability and Statistics', 11),
('MAT103', 'Engineering Mathematics', 7),
('MAT105', 'discrete mathematics', 12),
('MAT202', 'NUMERICAL METHODS', 12),
('MAT204', 'Numerical Methods', 12),
('NRE104', 'APPLIED CHEM', 9),
('NRE105', 'APPLIED PHYSICS', 23),
('NRE107', 'ENGINEERING MECHANICS', 4),
('PE202', 'SISMIC METHODS AND ANALYSIS', 39),
('PE203', 'PET ECONOMICS', 39),
('PE204', 'PET FLUIDS', 40),
('PE205', 'PET GEOLOGY', 41),
('PE304', 'RES ENGINEERING', 40),
('PE305', 'PRODUCTION ANGINEERING', 42),
('PE306', 'DRILLING ENGINEERING 2', 43),
('PE307', 'RESEARCH METHODS AND GROUP PROJECTS', 44),
('PE405', 'RES SIM', 40),
('PE406', 'NATURAL GAS ENGINEERING', 45),
('PE407', 'PETROCHEMICAL ENGINEERING', 46),
('PIR101', 'INTRO TO 20TH CENT HISTORY', 47),
('PIR105', 'FUND OF INT RELATIONS', 47),
('PIR109', 'INTRO TO MODERN ME', 48),
('PIR116', 'CRITICAL THINKING', 49),
('PIR118', 'HISTORY OF POLITICAL THOUGHT', 50),
('PIR210', 'CURRENT ISSUE IN INTERNATIONAL RELATIONS', 49),
('PIR211', 'POLITICAL GEO', 52),
('PIR215', 'COMPARATIVE POLITICAL SYSTEMS', 51),
('PIR220', 'PUBLIC POLICY', 47),
('PIR312', 'ADVANCED POLITICAL THEORY', 51),
('PIR314', 'GENDER AND POLITICS IN ME', 35),
('PIR316', 'ADVANCED RESEARCH METHODOLOGIES', 52),
('PIR317', 'CONFLICT ANALYSIS', 49),
('PIR318', 'STATISTICS FOR POLITICAL SCIENCE', 7),
('PIR405', 'THESIS', 49),
('PIR407', 'POLITICS OF KURDS AND KURDISTAN', 54),
('PIR409', 'POLITICAL ECONOMY', 53),
('PIR410', 'CONT POLITICAL THEORY', 51),
('PIR412', 'NATION BUILDING', 52),
('SE301', 'special topics in software engineering', 22),
('SE302', 'Intro to software testing', 25),
('SE404', 'Game design and development', 24),
('SE405', 'MOBILE APP DEVELOPMENT', 22),
('SOB102', 'PRINC OF ECONOMICS', 55),
('SOB103', 'INTRO TO STATISTICS', 12),
('SOB105', 'COMMERCIAL LAW', 56),
('SSE405', 'mobile application development', 22);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `group_`
--
ALTER TABLE `group_`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `lecturer`
--
ALTER TABLE `lecturer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `level`
--
ALTER TABLE `level`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `major`
--
ALTER TABLE `major`
  ADD PRIMARY KEY (`id`),
  ADD KEY `department__ibfk_1` (`department_id`);

--
-- Indexes for table `major_level`
--
ALTER TABLE `major_level`
  ADD PRIMARY KEY (`id`),
  ADD KEY `major__ibfk_1` (`major_id`),
  ADD KEY `level__ibfk_1` (`level_id`);

--
-- Indexes for table `major_level_module`
--
ALTER TABLE `major_level_module`
  ADD KEY `major_level__ibfk_1` (`major_level_id`),
  ADD KEY `module__ibfk_2` (`module_code`),
  ADD KEY `group__ibfk_3` (`group_id`);

--
-- Indexes for table `module`
--
ALTER TABLE `module`
  ADD PRIMARY KEY (`code`),
  ADD UNIQUE KEY `code` (`code`),
  ADD KEY `lecturer__ibfk_1` (`lecturer_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `department`
--
ALTER TABLE `department`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `group_`
--
ALTER TABLE `group_`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `lecturer`
--
ALTER TABLE `lecturer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- AUTO_INCREMENT for table `level`
--
ALTER TABLE `level`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `major`
--
ALTER TABLE `major`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `major_level`
--
ALTER TABLE `major_level`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `major`
--
ALTER TABLE `major`
  ADD CONSTRAINT `department__ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `department` (`id`);

--
-- Constraints for table `major_level`
--
ALTER TABLE `major_level`
  ADD CONSTRAINT `level__ibfk_1` FOREIGN KEY (`level_id`) REFERENCES `level` (`id`),
  ADD CONSTRAINT `major__ibfk_1` FOREIGN KEY (`major_id`) REFERENCES `major` (`id`);

--
-- Constraints for table `major_level_module`
--
ALTER TABLE `major_level_module`
  ADD CONSTRAINT `group__ibfk_3` FOREIGN KEY (`group_id`) REFERENCES `group_` (`id`),
  ADD CONSTRAINT `major_level__ibfk_1` FOREIGN KEY (`major_level_id`) REFERENCES `major_level` (`id`),
  ADD CONSTRAINT `module__ibfk_2` FOREIGN KEY (`module_code`) REFERENCES `module` (`code`);

--
-- Constraints for table `module`
--
ALTER TABLE `module`
  ADD CONSTRAINT `lecturer__ibfk_1` FOREIGN KEY (`lecturer_id`) REFERENCES `lecturer` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
