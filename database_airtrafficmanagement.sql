CREATE SCHEMA airtrafficmanagement;

COMMENT ON SCHEMA airtrafficmanagement IS 'Schema contenant les tables de l''application AirTrafficManagement';

CREATE TABLE airtrafficmanagement."Airline" (
    airline_id integer NOT NULL,
    airline_name character varying(50),
    airline_actif boolean,
    country_id integer NOT NULL
);

CREATE TABLE airtrafficmanagement."Airport" (
    airport_id integer NOT NULL,
    airport_name character varying(50),
    longitude double precision,
    latitude double precision,
    altitude double precision,
    timezone1 double precision,
    timezone2 character varying(50),
    city_id integer NOT NULL
);

CREATE TABLE airtrafficmanagement."City" (
    city_id integer NOT NULL,
    city_name character varying(50),
    country_id integer
);

CREATE TABLE airtrafficmanagement."Country" (
    country_id integer NOT NULL,
    country_name character varying(50)
);

CREATE TABLE airtrafficmanagement."Plane" (
    plane_id integer NOT NULL,
    plane_name character varying(50)
);

CREATE TABLE airtrafficmanagement."Routes" (
    routes_id integer NOT NULL,
    plane_id integer NOT NULL,
    airport_id_source integer NOT NULL,
    airport_id_dest integer NOT NULL,
    airline_id integer NOT NULL
);

ALTER TABLE ONLY airtrafficmanagement."Airline"
    ADD CONSTRAINT "Airline_pkey" PRIMARY KEY (airline_id);


ALTER TABLE ONLY airtrafficmanagement."Airport"
    ADD CONSTRAINT "Airport_pkey" PRIMARY KEY (airport_id);


ALTER TABLE ONLY airtrafficmanagement."City"
    ADD CONSTRAINT "City_pkey" PRIMARY KEY (city_id);


ALTER TABLE ONLY airtrafficmanagement."Country"
    ADD CONSTRAINT "Country_pkey" PRIMARY KEY (country_id);


ALTER TABLE ONLY airtrafficmanagement."Plane"
    ADD CONSTRAINT "Plane_pkey" PRIMARY KEY (plane_id);


ALTER TABLE ONLY airtrafficmanagement."Routes"
    ADD CONSTRAINT "Routes_pkey" PRIMARY KEY (routes_id, plane_id, airport_id_source, airport_id_dest, airline_id);


ALTER TABLE ONLY airtrafficmanagement."Airline"
    ADD CONSTRAINT "Airline_country_id_fkey" FOREIGN KEY (country_id) REFERENCES airtrafficmanagement."Country"(country_id) ON UPDATE RESTRICT ON DELETE RESTRICT;


ALTER TABLE ONLY airtrafficmanagement."Airport"
    ADD CONSTRAINT "Airport_city_id_fkey" FOREIGN KEY (city_id) REFERENCES airtrafficmanagement."City"(city_id) ON UPDATE RESTRICT ON DELETE RESTRICT;


ALTER TABLE ONLY airtrafficmanagement."City"
    ADD CONSTRAINT "City_country_id_fkey" FOREIGN KEY (country_id) REFERENCES airtrafficmanagement."Country"(country_id) ON UPDATE RESTRICT ON DELETE RESTRICT;


ALTER TABLE ONLY airtrafficmanagement."Routes"
    ADD CONSTRAINT "Routes_airline_id_fkey" FOREIGN KEY (airline_id) REFERENCES airtrafficmanagement."Airline"(airline_id) ON UPDATE RESTRICT ON DELETE RESTRICT;


ALTER TABLE ONLY airtrafficmanagement."Routes"
    ADD CONSTRAINT "Routes_airport_id_dest_fkey" FOREIGN KEY (airport_id_dest) REFERENCES airtrafficmanagement."Airport"(airport_id) ON UPDATE RESTRICT ON DELETE RESTRICT;


ALTER TABLE ONLY airtrafficmanagement."Routes"
    ADD CONSTRAINT "Routes_airport_id_source_fkey" FOREIGN KEY (airport_id_source) REFERENCES airtrafficmanagement."Airport"(airport_id) ON UPDATE RESTRICT ON DELETE RESTRICT;


ALTER TABLE ONLY airtrafficmanagement."Routes"
    ADD CONSTRAINT "Routes_plane_id_fkey" FOREIGN KEY (plane_id) REFERENCES airtrafficmanagement."Plane"(plane_id) ON UPDATE RESTRICT ON DELETE RESTRICT;
