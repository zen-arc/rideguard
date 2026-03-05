-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 27, 2025 at 08:08 AM
-- Server version: 10.5.27-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ridegonew`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_category`
--

CREATE TABLE `adminapp_category` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adminapp_category`
--

INSERT INTO `adminapp_category` (`id`, `name`, `image`) VALUES
(1, 'Sedan', 'images/banner-1_jv3iIlf.jpg'),
(2, 'Hatchback', 'images/blog-3.jpg'),
(3, 'xuv', 'images/about-img-1_rqYfFRE.jpg'),
(4, 'Sports', 'images/about-img-1_IvaU7c8.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add tbl user log', 7, 'add_tbluserlog'),
(26, 'Can change tbl user log', 7, 'change_tbluserlog'),
(27, 'Can delete tbl user log', 7, 'delete_tbluserlog'),
(28, 'Can view tbl user log', 7, 'view_tbluserlog'),
(29, 'Can add driver', 8, 'add_driver'),
(30, 'Can change driver', 8, 'change_driver'),
(31, 'Can delete driver', 8, 'delete_driver'),
(32, 'Can view driver', 8, 'view_driver'),
(33, 'Can add tbl user reg', 9, 'add_tbluserreg'),
(34, 'Can change tbl user reg', 9, 'change_tbluserreg'),
(35, 'Can delete tbl user reg', 9, 'delete_tbluserreg'),
(36, 'Can view tbl user reg', 9, 'view_tbluserreg'),
(37, 'Can add category', 10, 'add_category'),
(38, 'Can change category', 10, 'change_category'),
(39, 'Can delete category', 10, 'delete_category'),
(40, 'Can view category', 10, 'view_category'),
(41, 'Can add booking', 11, 'add_booking'),
(42, 'Can change booking', 11, 'change_booking'),
(43, 'Can delete booking', 11, 'delete_booking'),
(44, 'Can view booking', 11, 'view_booking'),
(45, 'Can add vehicle', 12, 'add_vehicle'),
(46, 'Can change vehicle', 12, 'change_vehicle'),
(47, 'Can delete vehicle', 12, 'delete_vehicle'),
(48, 'Can view vehicle', 12, 'view_vehicle'),
(49, 'Can add review', 13, 'add_review'),
(50, 'Can change review', 13, 'change_review'),
(51, 'Can delete review', 13, 'delete_review'),
(52, 'Can view review', 13, 'view_review');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(10, 'adminApp', 'category'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(12, 'driverApp', 'vehicle'),
(8, 'indexapp', 'driver'),
(7, 'indexapp', 'tbluserlog'),
(9, 'indexapp', 'tbluserreg'),
(6, 'sessions', 'session'),
(11, 'userApp', 'booking'),
(13, 'userApp', 'review');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-02-24 05:42:40.062367'),
(2, 'auth', '0001_initial', '2025-02-24 05:42:40.662225'),
(3, 'admin', '0001_initial', '2025-02-24 05:42:40.798751'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-02-24 05:42:40.810201'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-02-24 05:42:40.822070'),
(6, 'adminApp', '0001_initial', '2025-02-24 05:42:40.840025'),
(7, 'contenttypes', '0002_remove_content_type_name', '2025-02-24 05:42:40.916778'),
(8, 'auth', '0002_alter_permission_name_max_length', '2025-02-24 05:42:40.982791'),
(9, 'auth', '0003_alter_user_email_max_length', '2025-02-24 05:42:41.002244'),
(10, 'auth', '0004_alter_user_username_opts', '2025-02-24 05:42:41.013944'),
(11, 'auth', '0005_alter_user_last_login_null', '2025-02-24 05:42:41.062673'),
(12, 'auth', '0006_require_contenttypes_0002', '2025-02-24 05:42:41.069805'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2025-02-24 05:42:41.081545'),
(14, 'auth', '0008_alter_user_username_max_length', '2025-02-24 05:42:41.110287'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2025-02-24 05:42:41.130049'),
(16, 'auth', '0010_alter_group_name_max_length', '2025-02-24 05:42:41.150088'),
(17, 'auth', '0011_update_proxy_permissions', '2025-02-24 05:42:41.163038'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2025-02-24 05:42:41.183599'),
(19, 'indexapp', '0001_initial', '2025-02-24 05:42:41.336947'),
(20, 'driverApp', '0001_initial', '2025-02-24 05:42:41.466832'),
(21, 'sessions', '0001_initial', '2025-02-24 05:42:41.501405'),
(22, 'userApp', '0001_initial', '2025-02-24 05:42:41.717155'),
(23, 'userApp', '0002_review', '2025-03-15 09:26:57.303096'),
(24, 'indexapp', '0002_alter_tbluserreg_phone_number', '2025-03-21 13:28:41.554557'),
(25, 'userApp', '0003_booking_payment_status', '2025-03-21 15:27:30.208874'),
(26, 'userApp', '0004_booking_destination_location_name_and_more', '2025-03-24 06:29:26.576696');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('5jeigcng75hp0uk77nanln7nao4jj8ha', '.eJyrVsrJT8_Mi89MUbIy1FFKKcosSy2C8YpS0zOLS4oSSzLzoSpqAZRiEKI:1tq9Ck:hapVpJa5fjKMgNAg6pqKmOvTUMxwZ-9GtDQMQvM2E24', '2025-03-20 11:15:54.126092'),
('7fh8zvfv5a3koi42anp8k0vew8vmg3vd', 'eyJsb2dpbl9pZCI6MTMsImRyaXZlcl9pZCI6NX0:1tvuzy:HIbfZkL8ZGOqD_OswA9eYw0imXXH1f0SFXY9VVaiQDg', '2025-04-05 09:18:34.829197'),
('7wn6v997dgdayvpukl029fi78par72y6', 'eyJsb2dpbl9pZCI6Mn0:1txISb:QN9r5A6SMsYE-Xm2wTgYkipEj4-P4W0WmGO4XJg8NLQ', '2025-04-09 04:33:49.726637'),
('a23vggxnkb1hkzebuqt4fnp5dpmptobb', 'eyJsb2dpbl9pZCI6MywiZHJpdmVyX2lkIjoxfQ:1ttP61:zQDMbUlhGfWW5A9ypvMgf6pW7Ft7XUY0wCckoeP2bzY', '2025-03-29 10:50:25.817136'),
('h4kuhh7zk0l2xxx2j0ayh449ewomx6oe', 'eyJsb2dpbl9pZCI6Mn0:1txhJU:kJvSz-igbWxhRn3YR_B5Do3IjhdCa0IK_wq7OlBgSnQ', '2025-04-10 07:06:04.923334'),
('ibu4aa948118clid5ru3v5tm7cwpw5bg', 'eyJsb2dpbl9pZCI6MTAsInJlZ2lzdHJhdGlvbl9pZCI6N30:1twZds:GVTRGhwWs4HCwZNZtZK3ZpXo9bsMyXJKaijT9T_VCFY', '2025-04-07 04:42:28.539929'),
('jcfv3hdqyi7dwu6kumqm6mvm91423283', 'eyJsb2dpbl9pZCI6MywiZHJpdmVyX2lkIjoxfQ:1tvuuv:-xowTDpu_1l6yaKZy07Z_k4vOu-Brp1HEfNnRPTSkPo', '2025-04-05 09:13:21.083710'),
('mydy6ug0phugc815qnin0bym0l9ly6pi', 'eyJsb2dpbl9pZCI6MSwicmVnaXN0cmF0aW9uX2lkIjoxfQ:1tplqH:-0KkFiiB9eGHxo045egehdf6b6PilVTT8vHCmlyd6Pg', '2025-03-19 10:19:09.967620'),
('qpea9xvsrehnnh44tsxogegvanqzqqfy', 'eyJsb2dpbl9pZCI6MSwicmVnaXN0cmF0aW9uX2lkIjoxfQ:1tpkPK:XfKXJLwyFgXLm2K_-4UlK9ePCoUFB5aLNtjjIS77yoY', '2025-03-19 08:47:14.486385'),
('rchb0nknq10brgf8qwvnisv8zcpcb780', 'eyJsb2dpbl9pZCI6MSwiZHJpdmVyX2lkIjoyLCJyZWdpc3RyYXRpb25faWQiOjF9:1tmRsD:aAcIUsw6kBnCPRM8SKi1rtoGvAmL8WeHEyxjJNfULMs', '2025-03-10 06:23:25.943610'),
('ru8selmgtip2a5iybimq4bwirdal2ghd', 'eyJsb2dpbl9pZCI6MTAsInJlZ2lzdHJhdGlvbl9pZCI6N30:1txIir:Iyc7fNu4BcKuO3SOkxo6hhW3-EaICsfgAapXbC4yhdM', '2025-04-09 04:50:37.249772'),
('shsa599cpl58gkj6jxd7045179p3uavo', 'eyJsb2dpbl9pZCI6MSwicmVnaXN0cmF0aW9uX2lkIjoxfQ:1tq46g:zsFkYouz_KRbXkzpWDbFPsrThpslqtvr1ktuGDho4ZE', '2025-03-20 05:49:18.404975'),
('w5q23w7n2hhjs5aejpu892df0zhilc3n', 'eyJsb2dpbl9pZCI6MTAsImRyaXZlcl9pZCI6NiwicmVnaXN0cmF0aW9uX2lkIjo3fQ:1txhJj:4JnWUqRfRAtPdso5CKBiEjqNafRbwz_Dz6gr5NvoL_c', '2025-04-10 07:06:19.407328'),
('y2ti1vb7e6uyjb84mahxzm72fsxfnkxh', 'eyJsb2dpbl9pZCI6MywicmVnaXN0cmF0aW9uX2lkIjoxLCJkcml2ZXJfaWQiOjF9:1tqo6o:R-LNozykgmMOxULozG-288iNnI9UElQKF2l7TxyylV4', '2025-03-22 06:56:30.442879');

-- --------------------------------------------------------

--
-- Table structure for table `driverapp_vehicle`
--

CREATE TABLE `driverapp_vehicle` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `regno` varchar(100) NOT NULL,
  `fuel_type` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  `no_of_seats` int(11) NOT NULL,
  `price_per_km` int(11) DEFAULT NULL,
  `category_id` bigint(20) NOT NULL,
  `driverid_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `driverapp_vehicle`
--

INSERT INTO `driverapp_vehicle` (`id`, `name`, `image`, `regno`, `fuel_type`, `model`, `no_of_seats`, `price_per_km`, `category_id`, `driverid_id`) VALUES
(1, 'Buggati Chiron', 'images/car-4_vLtiFdf.png', 'KL12G6666', 'Diesel', '2025', 2, 90, 1, 1),
(2, 'Porsche 911 GT3 RS', 'images/blog-1_YREYwAg.jpg', 'KL12G0007', 'Petrol', '2025', 2, 76, 1, 1),
(3, 'BMW M4 Competition', 'images/car-3_LAblggQ.png', '007', 'PETROL', '2025', 2, 60, 1, 2),
(4, 'Toyota Supra', 'images/car-1_crRgSwT.png', '666', 'Electric', '2018', 2, 90, 4, 2);

-- --------------------------------------------------------

--
-- Table structure for table `indexapp_driver`
--

CREATE TABLE `indexapp_driver` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `pcc` varchar(100) NOT NULL,
  `aadhar` varchar(100) NOT NULL,
  `status` varchar(50) NOT NULL,
  `loginid_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `indexapp_driver`
--

INSERT INTO `indexapp_driver` (`id`, `name`, `image`, `pcc`, `aadhar`, `status`, `loginid_id`) VALUES
(1, 'zen', 'images/team-1_7lgqR68.jpg', 'documents/bg-1_WOv4bi3.jpg', 'documents/about-img_CFgbs8H.jpg', 'approved', 3),
(2, 'Jagal baby', 'images/team-2_bY8w9BW.jpg', 'documents/about-img-1_FfGt3Pv.jpg', 'documents/blog-3_zY6s4FL.jpg', 'approved', 4),
(5, 'cj', 'images/team-3_hCNJWI1.jpg', 'documents/banner-1_dZt7yyk.jpg', 'documents/blog-2_b3aL7mV.jpg', 'approved', 13),
(6, 'domi', 'images/team-4_G0sKInd.jpg', 'documents/blog-1_OBX31jj.jpg', 'documents/blog-2_TH49B68.jpg', 'pending', 15);

-- --------------------------------------------------------

--
-- Table structure for table `indexapp_tbluserlog`
--

CREATE TABLE `indexapp_tbluserlog` (
  `id` bigint(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `usertype` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `indexapp_tbluserlog`
--

INSERT INTO `indexapp_tbluserlog` (`id`, `email`, `password`, `usertype`) VALUES
(1, 'leo@gmail.com', 'zxc', 'user'),
(2, 'admin@gmail.com', 'zxc', 'admin'),
(3, 'zen@gmail.com', 'zxc', 'driver'),
(4, 'jagalb@gmail.com', 'zxc', 'driver'),
(6, 'leomessi551255@gmail.com', 'zxc', 'user'),
(7, 'leomessi551255@gmail.com', 'zxc', 'user'),
(8, 'leomessi551255@gmail.com', 'zxc', 'user'),
(9, 'c43jagalbaby@gmail.com', 'zxc', 'user'),
(10, 'sample@gmail.com', 'zxc', 'user'),
(13, 'cj@gmail.com', 'cj@12345678', 'driver'),
(14, 'uthara3004@gmail.com', 'uthara@123', 'user'),
(15, 'domi@gmail.com', 'domi@123', 'driver');

-- --------------------------------------------------------

--
-- Table structure for table `indexapp_tbluserreg`
--

CREATE TABLE `indexapp_tbluserreg` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `phone_number` varchar(10) NOT NULL,
  `login_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `indexapp_tbluserreg`
--

INSERT INTO `indexapp_tbluserreg` (`id`, `name`, `phone_number`, `login_id`) VALUES
(1, 'leo', '1234567890', 1),
(2, 'admin', '1234567890', 2),
(3, 'leomessi', '1234567890', 6),
(4, 'leomessi', '1234567890', 7),
(5, 'leomessi', '1234567890', 8),
(6, 'jj', '1234567890', 9),
(7, 'sample', '9074105388', 10),
(9, 'uthara', '1234567891', 14);

-- --------------------------------------------------------

--
-- Table structure for table `userapp_booking`
--

CREATE TABLE `userapp_booking` (
  `id` bigint(20) NOT NULL,
  `from_location` varchar(255) NOT NULL,
  `destination_location` varchar(255) NOT NULL,
  `travel_date` date NOT NULL,
  `travel_time` time(6) NOT NULL,
  `total_price` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `driverid_id` bigint(20) DEFAULT NULL,
  `userid_id` bigint(20) NOT NULL,
  `vehicleid_id` bigint(20) NOT NULL,
  `payment_status` varchar(20) NOT NULL,
  `destination_location_name` varchar(255) DEFAULT NULL,
  `from_location_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userapp_booking`
--

INSERT INTO `userapp_booking` (`id`, `from_location`, `destination_location`, `travel_date`, `travel_time`, `total_price`, `created_at`, `status`, `driverid_id`, `userid_id`, `vehicleid_id`, `payment_status`, `destination_location_name`, `from_location_name`) VALUES
(7, 'Ernakulam South', 'vytilla', '2025-03-08', '12:33:00.000000', 76, '2025-03-08 07:04:09.516783', 'completed', 1, 1, 2, 'paid', NULL, NULL),
(14, 'Ernakulam South', 'vytilla', '2025-03-15', '12:45:00.000000', 90, '2025-03-15 07:15:10.720113', 'available', 2, 7, 4, 'unpaid', NULL, NULL),
(15, 'rexhfcgjhvjbknlm;', 'aefsrgdxthyfcjguvh', '2025-03-21', '21:21:00.000000', 76, '2025-03-21 15:51:52.840985', 'cancelled', 1, 7, 2, 'cancelled', NULL, NULL),
(16, 'Ernakulam South', 'vytilla', '2025-03-22', '14:43:00.000000', 90, '2025-03-22 09:14:10.719544', 'completed', 1, 7, 1, 'paid', NULL, NULL),
(17, 'Ernakulam South', 'pala', '2025-03-27', '14:02:00.000000', 76, '2025-03-24 05:30:29.528219', 'pending', 1, 7, 2, 'unpaid', NULL, NULL),
(18, 'Ernakulam South', 'pala', '2025-03-28', '14:02:00.000000', 76, '2025-03-24 05:31:42.034959', 'pending', 1, 7, 2, 'unpaid', NULL, NULL),
(19, '9.602916547951423, 76.3452676603528', '8.539738394397492, 77.004230213496', '2025-03-28', '16:11:00.000000', 76, '2025-03-24 05:36:43.646287', 'pending', 1, 7, 2, 'unpaid', NULL, NULL),
(20, '10.943888437257428, 75.97934462138895', '11.21342792694782, 75.86402617458891', '2025-03-30', '16:27:00.000000', 2991, '2025-03-24 05:57:10.967284', 'pending', 1, 7, 2, 'unpaid', NULL, NULL),
(21, '10.766751374434332, 76.65393966735861', '10.78007359393042, 76.64518782094972', '2025-03-31', '16:27:00.000000', 170, '2025-03-24 06:02:05.495221', 'pending', 1, 7, 2, 'unpaid', NULL, NULL),
(22, '10.754052555561211, 76.28131625078306', '10.768893084362741, 76.37192360184022', '2025-03-28', '18:18:00.000000', 1188, '2025-03-24 06:48:27.103060', 'pending', 1, 7, 2, 'unpaid', 'Kanniampuram, Ottappalam, Palakkad, Kerala, 679101, India', 'Shoranur, Ottappalam, Palakkad, Kerala, 679121, India'),
(23, '10.652172909863134, 76.24219600373073', '10.758100044955231, 76.28406758262838', '2025-03-29', '18:19:00.000000', 1233, '2025-03-24 06:49:32.961195', 'pending', 1, 7, 2, 'unpaid', 'Shoranur, Ottappalam, Palakkad, Kerala, 679121, India', 'Kodungallur - Shornur Road, Ottupara, Wadakkancherry, Talappilly, Thrissur, Kerala, 680582, India'),
(24, '10.110246540336917, 76.34891481649782', '10.105155501984818, 76.35873705916946', '2025-03-26', '09:57:00.000000', 293, '2025-03-26 04:27:15.153464', 'pending', 1, 7, 1, 'unpaid', 'zeenath, Sub Jail Road, Thottakkattukara, Aluva, Ernakulam, Kerala, 683101, India', 'Thottakkattukara, Aluva, Ernakulam, Kerala, 683108, India'),
(25, '10.110246540336917, 76.34891481649782', '10.105155501984818, 76.35873705916946', '2025-03-26', '09:57:00.000000', 293, '2025-03-26 04:27:16.096657', 'completed', 1, 7, 1, 'paid', 'zeenath, Sub Jail Road, Thottakkattukara, Aluva, Ernakulam, Kerala, 683101, India', 'Thottakkattukara, Aluva, Ernakulam, Kerala, 683108, India'),
(26, '10.873093421676758, 76.67168144931244', '10.831282752142348, 76.81720234646487', '2025-03-27', '10:33:00.000000', 2519, '2025-03-27 05:03:16.679452', 'pending', 1, 7, 2, 'unpaid', 'Vattapara Attupathi Road, Palakkad, Kerala, 678624, India', 'Anackal, Palakkad, Kerala, 678651, India'),
(27, '9.151417778958777, 76.73185612331113', '9.144638659125045, 76.7706388152409', '2025-03-27', '12:36:00.000000', 374, '2025-03-27 07:06:57.637590', 'pending', 1, 7, 2, 'unpaid', 'Kayamkulam - Pathanapuram Road, Ezhamkulam Junction, Parakode, Ezhamkulam, Adoor, Pathanamthitta, Kerala, 691155, India', 'Nellimoottilpadi, Adoor, Pathanamthitta, Kerala, 691523, India'),
(28, '9.151417778958777, 76.73185612331113', '9.144638659125045, 76.7706388152409', '2025-03-27', '12:36:00.000000', 374, '2025-03-27 07:06:58.615030', 'pending', 1, 7, 2, 'unpaid', 'Kayamkulam - Pathanapuram Road, Ezhamkulam Junction, Parakode, Ezhamkulam, Adoor, Pathanamthitta, Kerala, 691155, India', 'Nellimoottilpadi, Adoor, Pathanamthitta, Kerala, 691523, India');

-- --------------------------------------------------------

--
-- Table structure for table `userapp_review`
--

CREATE TABLE `userapp_review` (
  `id` bigint(20) NOT NULL,
  `rating` int(11) NOT NULL,
  `comment` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `vehicle_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userapp_review`
--

INSERT INTO `userapp_review` (`id`, `rating`, `comment`, `created_at`, `user_id`, `vehicle_id`) VALUES
(1, 4, 'okay', '2025-03-15 09:34:48.205992', 7, 4),
(2, 1, 'bad', '2025-03-15 10:01:11.430989', 7, 2),
(3, 1, 'no', '2025-03-15 10:06:14.340019', 7, 4),
(4, 5, 'best', '2025-03-21 13:21:07.406429', 7, 2),
(5, 3, 'ftvgybhjn', '2025-03-26 04:51:44.006301', 7, 1),
(6, 5, 'the best in segment', '2025-03-27 06:42:35.662641', 1, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adminapp_category`
--
ALTER TABLE `adminapp_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `driverapp_vehicle`
--
ALTER TABLE `driverapp_vehicle`
  ADD PRIMARY KEY (`id`),
  ADD KEY `driverApp_vehicle_category_id_38fccc8b_fk_adminApp_category_id` (`category_id`),
  ADD KEY `driverApp_vehicle_driverid_id_9f888676_fk_indexapp_driver_id` (`driverid_id`);

--
-- Indexes for table `indexapp_driver`
--
ALTER TABLE `indexapp_driver`
  ADD PRIMARY KEY (`id`),
  ADD KEY `indexapp_driver_loginid_id_015ed3b7_fk_indexapp_tbluserlog_id` (`loginid_id`);

--
-- Indexes for table `indexapp_tbluserlog`
--
ALTER TABLE `indexapp_tbluserlog`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `indexapp_tbluserreg`
--
ALTER TABLE `indexapp_tbluserreg`
  ADD PRIMARY KEY (`id`),
  ADD KEY `indexapp_tbluserreg_login_id_330a22e6_fk_indexapp_tbluserlog_id` (`login_id`);

--
-- Indexes for table `userapp_booking`
--
ALTER TABLE `userapp_booking`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApp_booking_driverid_id_b597179c_fk_indexapp_driver_id` (`driverid_id`),
  ADD KEY `userApp_booking_userid_id_009d693b_fk_indexapp_tbluserreg_id` (`userid_id`),
  ADD KEY `userApp_booking_vehicleid_id_4fc036c7_fk_driverApp_vehicle_id` (`vehicleid_id`);

--
-- Indexes for table `userapp_review`
--
ALTER TABLE `userapp_review`
  ADD PRIMARY KEY (`id`),
  ADD KEY `userApp_review_user_id_7a34587d_fk_indexapp_tbluserreg_id` (`user_id`),
  ADD KEY `userApp_review_vehicle_id_64f94284_fk_driverApp_vehicle_id` (`vehicle_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adminapp_category`
--
ALTER TABLE `adminapp_category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `driverapp_vehicle`
--
ALTER TABLE `driverapp_vehicle`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `indexapp_driver`
--
ALTER TABLE `indexapp_driver`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `indexapp_tbluserlog`
--
ALTER TABLE `indexapp_tbluserlog`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `indexapp_tbluserreg`
--
ALTER TABLE `indexapp_tbluserreg`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `userapp_booking`
--
ALTER TABLE `userapp_booking`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `userapp_review`
--
ALTER TABLE `userapp_review`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `driverapp_vehicle`
--
ALTER TABLE `driverapp_vehicle`
  ADD CONSTRAINT `driverApp_vehicle_category_id_38fccc8b_fk_adminApp_category_id` FOREIGN KEY (`category_id`) REFERENCES `adminapp_category` (`id`),
  ADD CONSTRAINT `driverApp_vehicle_driverid_id_9f888676_fk_indexapp_driver_id` FOREIGN KEY (`driverid_id`) REFERENCES `indexapp_driver` (`id`);

--
-- Constraints for table `indexapp_driver`
--
ALTER TABLE `indexapp_driver`
  ADD CONSTRAINT `indexapp_driver_loginid_id_015ed3b7_fk_indexapp_tbluserlog_id` FOREIGN KEY (`loginid_id`) REFERENCES `indexapp_tbluserlog` (`id`);

--
-- Constraints for table `indexapp_tbluserreg`
--
ALTER TABLE `indexapp_tbluserreg`
  ADD CONSTRAINT `indexapp_tbluserreg_login_id_330a22e6_fk_indexapp_tbluserlog_id` FOREIGN KEY (`login_id`) REFERENCES `indexapp_tbluserlog` (`id`);

--
-- Constraints for table `userapp_booking`
--
ALTER TABLE `userapp_booking`
  ADD CONSTRAINT `userApp_booking_driverid_id_b597179c_fk_indexapp_driver_id` FOREIGN KEY (`driverid_id`) REFERENCES `indexapp_driver` (`id`),
  ADD CONSTRAINT `userApp_booking_userid_id_009d693b_fk_indexapp_tbluserreg_id` FOREIGN KEY (`userid_id`) REFERENCES `indexapp_tbluserreg` (`id`),
  ADD CONSTRAINT `userApp_booking_vehicleid_id_4fc036c7_fk_driverApp_vehicle_id` FOREIGN KEY (`vehicleid_id`) REFERENCES `driverapp_vehicle` (`id`);

--
-- Constraints for table `userapp_review`
--
ALTER TABLE `userapp_review`
  ADD CONSTRAINT `userApp_review_user_id_7a34587d_fk_indexapp_tbluserreg_id` FOREIGN KEY (`user_id`) REFERENCES `indexapp_tbluserreg` (`id`),
  ADD CONSTRAINT `userApp_review_vehicle_id_64f94284_fk_driverApp_vehicle_id` FOREIGN KEY (`vehicle_id`) REFERENCES `driverapp_vehicle` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
