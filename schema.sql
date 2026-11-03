CREATE TABLE IF NOT EXISTS Clientes (
    Id              UUID         NOT NULL,
    Nombre          VARCHAR(60)  NOT NULL,
    ApellidoPaterno VARCHAR(60)  NOT NULL,
    ApellidoMaterno VARCHAR(60)  NULL,
    RFC             VARCHAR(13)  NOT NULL,
    PRIMARY KEY (Id),
    UNIQUE KEY uq_clientes_rfc (RFC),
    KEY idx_clientes_nombre (Nombre, ApellidoPaterno, ApellidoMaterno)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS Direcciones (
    Id        UUID         NOT NULL,
    Calle     VARCHAR(100) NOT NULL,
    Numero    VARCHAR(10)  NOT NULL,
    Colonia   VARCHAR(100) NOT NULL,
    Estado    VARCHAR(50)  NOT NULL,
    CP        CHAR(5)      NOT NULL,
    idCliente UUID         NOT NULL,
    PRIMARY KEY (Id),
    KEY idx_direcciones_cliente (idCliente),
    CONSTRAINT fk_direcciones_cliente
        FOREIGN KEY (idCliente) REFERENCES Clientes (Id)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;