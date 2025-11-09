-- Table Voie
CREATE TABLE voie (
  num_voie INT(11) NOT NULL,
  interdite TINYINT(1) NOT NULL,
  PRIMARY KEY (num_voie)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table Rames
CREATE TABLE rames (
  num_serie VARCHAR(12) NOT NULL,
  type_rame VARCHAR(50) NOT NULL,
  voie INT(11) UNIQUE,
  conducteur_entrant VARCHAR(50) NOT NULL,
  PRIMARY KEY (num_serie),
  CONSTRAINT fk_rame_voie FOREIGN KEY (voie) REFERENCES voie(num_voie)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table Taches
CREATE TABLE taches (
  num_serie VARCHAR(12) NOT NULL,
  num_tache INT(11) NOT NULL,
  tache TEXT NOT NULL,
  PRIMARY KEY (num_serie, num_tache),
  CONSTRAINT fk_tache_rame FOREIGN KEY (num_serie) REFERENCES rames(num_serie)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
