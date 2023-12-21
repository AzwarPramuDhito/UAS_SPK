--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: handphone; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.handphone (
    "Nama_HP" text,
    "Reputasi_Brand" text,
    "Processor_Antutu" integer,
    "Baterai" text,
    "Harga" text,
    "Ukuran_Layar" real
);


ALTER TABLE public.handphone OWNER TO postgres;

--
-- Data for Name: handphone; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.handphone ("Nama_HP", "Reputasi_Brand", "Processor_Antutu", "Baterai", "Harga", "Ukuran_Layar") FROM stdin;
Redmi 12	Lumayan Terkenal	524500	5000 mAh	2.1 jutaan	6.8
Infinix Note 30	Kurang Terkenal	548000	5000 mAh	2 jutaan	6.78
Redmi Note 12	Lumayan Terkenal	415448	5000 mAh	2 jutaan	6.7
Realme C55 NFC	Cukup Terkenal	452916	5000 mAh	2.2 jutaan	6.7
Redmi 10 5G	Lumayan Terkenal	478448	4700 mAh	2.5 jutaan	6.58
Techno Pova 4 Pro	Kurang Terkenal	934558	6000 mAh	3.1 jutaan	6.66
Infinix Note 12	Kurang Terkenal	670439	5000 mAh	2.6 jutaan	6.67
Samsung Galxy A23	Sangat Terkenal	798330	5000 mAh	2.8 jutaan	6.6
Redmi Note 11	Lumayan Terkenal	624000	5000 mAh	2.3 jutaan	6.43
Realme 9i	Lumayan Terkenal	789376	5000 mAh	2.78 jutaan	6.6
\.


--
-- PostgreSQL database dump complete
--

