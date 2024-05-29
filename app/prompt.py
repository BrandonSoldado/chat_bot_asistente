

mensaje_bienvenida = """podes simular ser un chat bot asistente que determina que tipo de hongo hay en una superficie como la pared, techo, ect., quiero 
que en tu presentacion saludes a este nombre: """

mensaje_bienvenida2 = """Estas son las preguntas que un usuario hizo al chat bot asistente, si en alguna pregunta menciona que productos hay para eliminar ulgun hongo
quiero que le mostrar los producto con sus precios que estan en oferta para eliminar ese hongo o los productos con sus precios que estan marcados como nuevos,
si nunca menciona algun producto para eliminar un hongo, quiero que simplemente te presentes saludando a este nombre: """

prompt_chat_bot = """Quiero que tus respuestas no me saludes, no quiero que menciones a la bbdd,esta es tu bbdd: """



prompt_bbdd= """CREATE TABLE HONGO (
    ID SERIAL PRIMARY KEY,
    Nombre VARCHAR(50),
    Descripcion TEXT
);
CREATE TABLE USUARIO (
    ID SERIAL PRIMARY KEY,
    Nombre VARCHAR(60),
    Ci INT,
    Direccion VARCHAR(60),
    Email VARCHAR(60),
    FechaNacimiento DATE,
    Telefono VARCHAR(20)
);
CREATE TABLE PREGUNTA_USUARIO (
    ID SERIAL PRIMARY KEY,
    Pregunta TEXT,
    Fecha DATE,
    Hora TIME,
    UsuarioID INT,
	FOREIGN KEY (UsuarioID) REFERENCES USUARIO(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE COMPRA (
    ID SERIAL PRIMARY KEY,
    Fecha DATE,
    Total NUMERIC(10, 2),
    UsuarioID INT REFERENCES USUARIO(ID)
);

CREATE TABLE SUPERFICIE (
    SitioHongo VARCHAR(60) NOT NULL,
    UsuarioID INT,
    HongoID INT,
    PRIMARY KEY (UsuarioID, HongoID),
    FOREIGN KEY (UsuarioID) REFERENCES USUARIO(ID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (HongoID) REFERENCES HONGO(ID) ON UPDATE CASCADE ON DELETE CASCADE
);





CREATE TABLE AMBIENTE_FAVORABLE (
    ID SERIAL PRIMARY KEY,
    Nombre VARCHAR(100)
);
CREATE TABLE DESARROLLA (
    HongoID INT,
    AmbienteID INT,
    Descripcion TEXT,
    PRIMARY KEY (HongoID, AmbienteID),
    FOREIGN KEY (HongoID) REFERENCES HONGO(ID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (AmbienteID) REFERENCES AMBIENTE_FAVORABLE(ID) ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE SINTOMA (
    ID SERIAL PRIMARY KEY,
    Nombre VARCHAR(100)
);
CREATE TABLE PRODUCE (
    HongoID INT,
    SintomaID INT,
    PRIMARY KEY (HongoID, SintomaID),
    FOREIGN KEY (HongoID) REFERENCES HONGO(ID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (SintomaID) REFERENCES SINTOMA(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE PRODUCTO (
    ID SERIAL PRIMARY KEY,
    Nombre VARCHAR(255),
    Descripcion TEXT,
    Precio NUMERIC(10, 2),
    EsNuevo BOOLEAN
);
CREATE TABLE DETALLE_COMPRA (
    Cantidad INT,
	CompraID INT,
	ProductoID INT,
	PRIMARY KEY (CompraID, ProductoID),
    FOREIGN KEY (CompraID) REFERENCES COMPRA(ID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (ProductoID) REFERENCES PRODUCTO(ID) ON UPDATE CASCADE ON DELETE CASCADE
);
CREATE TABLE OFERTA (
    ID SERIAL PRIMARY KEY,
    PrecioOferta NUMERIC(10, 2),
    Descripcion TEXT,
    ProductoID INT REFERENCES PRODUCTO(ID)
);
CREATE TABLE ANTIBIOTICO (
    PRODUCTOID INT,
    HongoID INT,
    PRIMARY KEY (PRODUCTOID, HongoID),
    FOREIGN KEY (PRODUCTOID) REFERENCES PRODUCTO(ID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (HongoID) REFERENCES HONGO(ID) ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE PATRON_CRECIENTO (
    ID SERIAL PRIMARY KEY,
    Nombre VARCHAR(60)
);
CREATE TABLE FORMA (
    Descripcion TEXT,
	HongoID INT,
    PATRON_CRECIENTOID INT,
    PRIMARY KEY (HongoID, PATRON_CRECIENTOID),
    FOREIGN KEY (HongoID) REFERENCES HONGO(ID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (PATRON_CRECIENTOID) REFERENCES PATRON_CRECIENTO(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE TEXTURA (
    ID SERIAL PRIMARY KEY,
    Nombre VARCHAR(100)
);
CREATE TABLE PRESENTA (
    HongoID INT,
    TexturaID INT,
    PRIMARY KEY (HongoID, TexturaID),
    FOREIGN KEY (HongoID) REFERENCES HONGO(ID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (TexturaID) REFERENCES TEXTURA(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE COLOR (
    ID SERIAL PRIMARY KEY,
    Nombre VARCHAR(100)
);
CREATE TABLE CORRESPONDE (
    ColorID INT,
    EtapaDesarrollo VARCHAR(100),
	HongoID INT,
    PRIMARY KEY (HongoID, ColorID),
    FOREIGN KEY (HongoID) REFERENCES HONGO(ID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (ColorID) REFERENCES COLOR(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Imagen (
    id SERIAL PRIMARY KEY,
    imagen_base64 TEXT,
	HongoID INT,
    FOREIGN KEY (HongoID) REFERENCES HONGO(ID) ON UPDATE CASCADE ON DELETE CASCADE
);




















INSERT INTO HONGO (Nombre, Descripcion) VALUES
('Aspergillus', 'Hongo común en paredes húmedas y techos. Puede causar problemas respiratorios.'),
('Cladosporium', 'Hongo que crece en materiales de construcción húmedos como madera y yeso.'),
('Stachybotrys', 'Conocido como moho negro, crece en superficies muy húmedas y puede ser tóxico.'),
('Penicillium', 'Hongo que se encuentra en paredes dañadas por el agua y produce esporas verdes o azules.'),
('Alternaria', 'Crece en paredes y techos donde hay humedad persistente. Puede causar alergias.'),
('Fusarium', 'Hongo que crece en superficies húmedas y puede infectar plantas y animales.'),
('Chaetomium', 'Hongo que se encuentra en materiales de construcción húmedos y produce manchas negras.'),
('Mucor', 'Hongo que crece en paredes húmedas y produce esporas blancas o grises.'),
('Ulocladium', 'Hongo que crece en superficies de yeso y madera que han sido expuestas al agua.'),
('Aureobasidium', 'Hongo que aparece como manchas negras en paredes y techos húmedos.');


INSERT INTO USUARIO (Nombre, Ci, Direccion, Email, FechaNacimiento, Telefono) VALUES 
('Ana Martínez', 1234567, 'Calle 123, Ciudad ABC', 'ana@example.com', '1990-05-15', '+1234567890'),
('Juan López', 9876543, 'Av. Principal, Ciudad XYZ', 'juan@example.com', '1985-08-20', '+987654321'),
('María Rodríguez', 5555555, 'Carrera 456, Pueblo XYZ', 'maria@example.com', '1992-10-10', '+555555555');

INSERT INTO SUPERFICIE (SitioHongo, UsuarioID, HongoID) VALUES
('Pared del baño', 1, 1),  
('Techo de la cocina', 1, 2),  
('Pared', 2, 3),  
('Techo', 2, 4), 
('Pared de la cocina', 3, 5),  
('Techo del comedor', 3, 6);  

INSERT INTO PATRON_CRECIENTO (Nombre) VALUES
('Circular'),
('Irregular'),
('Ramificado'),
('Filamentoso'),
('Compacto');

INSERT INTO FORMA (Descripcion, HongoID, PATRON_CRECIENTOID) VALUES
('Colonias circulares y compactas', 1, 1),  
('Crecimiento irregular y disperso', 2, 2),  
('Estructura ramificada con esporas', 3, 3), 
('Formaciones filamentosas', 4, 4),  
('Colonias compactas y elevadas', 5, 5),  
('Colonias circulares y dispersas', 6, 1),  
('Crecimiento irregular con manchas', 7, 2),  
('Estructura filamentosa blanca', 8, 4), 
('Crecimiento ramificado en superficies expuestas', 9, 3),  
('Colonias compactas y negras', 10, 5); 

INSERT INTO TEXTURA (Nombre) VALUES
('Aterciopelada'),
('Algodonosa'),
('Pulverulenta'),
('Crestada'),
('Lisa');


INSERT INTO PRESENTA (HongoID, TexturaID) VALUES
(1, 1),  
(2, 2),  
(3, 3), 
(4, 4),  
(5, 5), 
(6, 1),  
(7, 2), 
(8, 3), 
(9, 4), 
(10, 5); 

INSERT INTO Imagen (imagen_base64, HongoID) VALUES
('iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAYAAAA10dzkAA...', 1),  -- Imagen para Aspergillus
('iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAYAAAA10dzkAB...', 2),  -- Imagen para Cladosporium
('iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAYAAAA10dzkAC...', 3),  -- Imagen para Stachybotrys
('iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAYAAAA10dzkAD...', 4),  -- Imagen para Penicillium
('iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAYAAAA10dzkAE...', 5),  -- Imagen para Alternaria
('iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAYAAAA10dzkAF...', 6),  -- Imagen para Fusarium
('iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAYAAAA10dzkAG...', 7),  -- Imagen para Chaetomium
('iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAYAAAA10dzkAH...', 8),  -- Imagen para Mucor
('iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAYAAAA10dzkAI...', 9),  -- Imagen para Ulocladium
('iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAYAAAA10dzkAJ...', 10); -- Imagen para Aureobasidium

INSERT INTO COLOR (Nombre) VALUES
('Verde'),
('Negro'),
('Azul'),
('Blanco'),
('Amarillo');

INSERT INTO CORRESPONDE (ColorID, EtapaDesarrollo, HongoID) VALUES
(1, 'Crecimiento inicial', 1),  -- Aspergillus con color Verde en etapa inicial
(2, 'Crecimiento medio', 1),    -- Aspergillus con color Negro en etapa media
(3, 'Crecimiento avanzado', 1), -- Aspergillus con color Azul en etapa avanzada
(1, 'Crecimiento inicial', 2),  -- Cladosporium con color Verde en etapa inicial
(3, 'Crecimiento medio', 2),    -- Cladosporium con color Azul en etapa media
(4, 'Crecimiento avanzado', 2), -- Cladosporium con color Blanco en etapa avanzada
(2, 'Crecimiento inicial', 3),  -- Stachybotrys con color Negro en etapa inicial
(5, 'Crecimiento medio', 3),    -- Stachybotrys con color Amarillo en etapa media
(1, 'Crecimiento avanzado', 3), -- Stachybotrys con color Verde en etapa avanzada
(4, 'Crecimiento inicial', 4),  -- Penicillium con color Blanco en etapa inicial
(1, 'Crecimiento medio', 4),    -- Penicillium con color Verde en etapa media
(3, 'Crecimiento avanzado', 4), -- Penicillium con color Azul en etapa avanzada
(5, 'Crecimiento inicial', 5),  -- Alternaria con color Amarillo en etapa inicial
(2, 'Crecimiento medio', 5),    -- Alternaria con color Negro en etapa media
(4, 'Crecimiento avanzado', 5), -- Alternaria con color Blanco en etapa avanzada
(3, 'Crecimiento inicial', 6),  -- Fusarium con color Azul en etapa inicial
(1, 'Crecimiento medio', 6),    -- Fusarium con color Verde en etapa media
(2, 'Crecimiento avanzado', 6), -- Fusarium con color Negro en etapa avanzada
(5, 'Crecimiento inicial', 7),  -- Chaetomium con color Amarillo en etapa inicial
(4, 'Crecimiento medio', 7),    -- Chaetomium con color Blanco en etapa media
(2, 'Crecimiento avanzado', 7), -- Chaetomium con color Negro en etapa avanzada
(4, 'Crecimiento inicial', 8),  -- Mucor con color Blanco en etapa inicial
(3, 'Crecimiento medio', 8),    -- Mucor con color Azul en etapa media
(1, 'Crecimiento avanzado', 8), -- Mucor con color Verde en etapa avanzada
(1, 'Crecimiento inicial', 9),  -- Ulocladium con color Verde en etapa inicial
(4, 'Crecimiento medio', 9),    -- Ulocladium con color Blanco en etapa media
(3, 'Crecimiento avanzado', 9), -- Ulocladium con color Azul en etapa avanzada
(5, 'Crecimiento inicial', 10), -- Aureobasidium con color Amarillo en etapa inicial
(3, 'Crecimiento medio', 10),   -- Aureobasidium con color Azul en etapa media
(2, 'Crecimiento avanzado', 10);-- Aureobasidium con color Negro en etapa avanzada

INSERT INTO AMBIENTE_FAVORABLE (Nombre) VALUES
('Alta humedad'),
('Poca ventilación'),
('Superficie porosa'),
('Materiales orgánicos'),
('Temperaturas cálidas');

INSERT INTO DESARROLLA (HongoID, AmbienteID, Descripcion) VALUES
(1, 1, 'Aspergillus se desarrolla bien en ambientes con alta humedad.'),
(1, 2, 'Aspergillus prefiere áreas con poca ventilación.'),
(2, 1, 'Cladosporium crece en ambientes con alta humedad.'),
(2, 3, 'Cladosporium prospera en superficies porosas.'),
(3, 1, 'Stachybotrys necesita alta humedad para desarrollarse.'),
(3, 4, 'Stachybotrys se desarrolla en materiales orgánicos húmedos.'),
(4, 2, 'Penicillium se encuentra en áreas con poca ventilación.'),
(4, 5, 'Penicillium crece en temperaturas cálidas.'),
(5, 1, 'Alternaria prospera en ambientes con alta humedad.'),
(5, 3, 'Alternaria se desarrolla en superficies porosas.'),
(6, 4, 'Fusarium necesita materiales orgánicos para crecer.'),
(6, 5, 'Fusarium prefiere temperaturas cálidas.'),
(7, 1, 'Chaetomium prospera en ambientes con alta humedad.'),
(7, 3, 'Chaetomium crece en superficies porosas.'),
(8, 2, 'Mucor se encuentra en áreas con poca ventilación.'),
(8, 5, 'Mucor prefiere temperaturas cálidas.'),
(9, 1, 'Ulocladium necesita alta humedad para desarrollarse.'),
(9, 3, 'Ulocladium prospera en superficies porosas.'),
(10, 4, 'Aureobasidium crece en materiales orgánicos húmedos.'),
(10, 5, 'Aureobasidium se desarrolla en temperaturas cálidas.');

INSERT INTO SINTOMA (Nombre) VALUES
('Problemas respiratorios'),
('Alergias'),
('Irritación en la piel'),
('Dolor de cabeza'),
('Fatiga'),
('Congestión nasal'),
('Tos'),
('Estornudos'),
('Irritación ocular'),
('Infecciones');

INSERT INTO PRODUCE (HongoID, SintomaID) VALUES
(1, 1),  -- Aspergillus - Problemas respiratorios
(1, 2),  -- Aspergillus - Alergias
(2, 2),  -- Cladosporium - Alergias
(2, 3),  -- Cladosporium - Irritación en la piel
(3, 4),  -- Stachybotrys - Dolor de cabeza
(3, 5),  -- Stachybotrys - Fatiga
(4, 6),  -- Penicillium - Congestión nasal
(4, 7),  -- Penicillium - Tos
(5, 2),  -- Alternaria - Alergias
(5, 8),  -- Alternaria - Estornudos
(6, 9),  -- Fusarium - Irritación ocular
(6, 10), -- Fusarium - Infecciones
(7, 2),  -- Chaetomium - Alergias
(7, 3),  -- Chaetomium - Irritación en la piel
(8, 1),  -- Mucor - Problemas respiratorios
(8, 6),  -- Mucor - Congestión nasal
(9, 2),  -- Ulocladium - Alergias
(9, 9),  -- Ulocladium - Irritación ocular
(10, 3), -- Aureobasidium - Irritación en la piel
(10, 7); -- Aureobasidium - Tos


INSERT INTO PRODUCTO (Nombre, Descripcion, Precio, EsNuevo) VALUES
('HG Antimoho', 'Este limpiador de moho de HG elimina con rapidez el moho de las zonas húmedas, tanto interiores como exteriores. Ideal para limpiar azulejas y juntas en cualquier estancia. Tambíen apto para fachadas, balcones y ornamentos de jardín.',40.99, FALSE),
('Muffyxid', 'Faren MUFFYXID, Limpiador de Moho de Acción Rápida, Eliminación Eficaz de Hongos y Algas, Higienizante Potente, 500 ml (500ml X 2)',30.50, FALSE),
('SaniCentro eliminador de moho', 'impiador multi-desinfección con cloro que está especialmente indicado para la limpieza y eliminación del moho, humedad y mugre, producidas en baños y cocinas. ',19.99, FALSE),
('Idroless 2 Lts','Limpiador para Tejados, Fachadas y Suelos Antihumedades.', 14.75, FALSE),
('Spray limpiador y eliminador de moho y verdin', 'Eliminador de moho y verdín es un potente limpiador alcalino, específicamente diseñado para eliminar mohos, verdines y musgos sobre todo tipo de superficies lavables.',30.25, FALSE),
('MPL limpiador antimoho 500ml', 'Limpia las manchas más complicadas provocadas por el moho o la humedad. Además, ayuda a retrasar la aparición de nuevas manchas.',50, FALSE),
('Limpiador Antihongos great Value de 1L', 'Elimina hongos  y bacterias  causantes del mal olor',60, FALSE),
('LIMPIADOR DE MOHO 85 GLADIO FM CON PULVERIZADOR 500 ML', 'Limpiador de moho GLADIO 85 es un limpiador de moho, hongos y musgo en paredes y techos de fácil usabililidad y efectivo.',100, FALSE),
('NUNCAS Spray Antimoho', 'Acción Anti Moho de Nuncas es un producto innovador que resuelve de modo profesional y definitivo el problema del moho en casa.',25, FALSE),
('HARPIC Limpiador Líquido Baños Antihongos', 'arpic® Anti-Hongos con Cloro es un líquido limpiador que contiene una potente fórmula, la cual es capaz de matar gérmenes que se encuentran en azulejos, mosaicos, paredes, cortinas y canceles de baño. ',20.99, FALSE),
('SPRAY ANTIMOHO STOP JUNTAS NEGRAS', '¡STOP MOHO, STOP JUNTAS NEGRAS! Juntas limpias y sin moho durante más tiempo. Gracias a su tecnología STOP&BLOCK libera el biocida solo cuando se dan las condiciones propicias para el crecimiento del moho, con lo que no ennegrece y permanece limpia y sin moho 5 veces más tiempo que una silicona normal cocinas y baños.',20.99, FALSE),
('Aerosol Antimoho W, Limpiador De Moho, Limpieza Antimoho Cz8', 'Spray antimoho de 60 ml, limpiador de moho, espuma limpiadora antimoho, potente limpiador de espuma multiusos, elimina las manchas de paredes, azulejos, sellos de silicona y más 60 ml',29.99, TRUE),
('Spray Antimoho Tixol', 'Este spray fungicida de acción rápida limpia, elimina y previene las manchas de moho como el musgo y el verdín. Además, este limpiador de moho destaca también por sus propiedades: Actúa con gran rapidez y rotundidad.',25.99, FALSE),
('ANTIMOHO Para superficies afectadas por humedad', 'Por su composición, que incluye un fungicida, la pintura antimoho destruye los hongos que se desarrollan con la humedad, que son nefastos para las superficies y nocivos para la salud.',20, FALSE),
('FILA Solutions Antimoho', 'Antimoho NOMOLD DEFENSE de Fila Solutions que evita la formación de moho en todo tipo de superficies. Antimoho pintura, pavimentos, revestimientos y juntas. Evita el ennegrecimiento por humedad en paredes interiores. Ideal como protector anti-moho antes de pintar. Ideal para piedra natural, cerámica, paredes pintadas, cemento, barro y juntas. Envase de 500ml.',35, TRUE),
('RIMUOVI MUFFA antimoho', 'FAREN Muffyxid - Eliminar moho, antimoho, limpiador de moldes de acción rápida, desinfectante, elimina rápidamente moho, hongos, musgos y algas, retrasa la reaparición, 5 litros (2)',120, TRUE),
('Limpiador antimoho', 'Antimoho, que limpia manchas negras de las juntas de silicona, lechada, yeso y baldosas. Efecto higienizante sin olor, recomendado para limpieza de interiores por no dejar ningún olor tras ser aplicado.',30.99, TRUE),
('CVR Limpiador antimoh', 'Líquido transparente desinfectante contra hongos',50.99, TRUE);

INSERT INTO ANTIBIOTICO (PRODUCTOID, HongoID) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 2),
(5, 2),
(6, 2),
(7, 3),
(8, 3),
(9, 3),
(10, 4),
(11, 4),
(12, 4),
(12, 5),
(13, 5),
(11, 5),
(16, 6),
(14, 6),
(15, 6),
(16, 7),
(17, 7),
(18, 7),
(7, 8),
(13, 8),
(11, 8),
(3, 9),
(6, 9),
(9, 9),
(1, 10),
(6, 10),
(11, 10);

INSERT INTO OFERTA (PrecioOferta, Descripcion, ProductoID) VALUES
(36.89, '¡Oferta especial! Limpia, elimina y previene el moho con este spray antimoho de alta eficacia.', 1), -- HG Antimoho
(27.45, '¡Oferta imperdible! Limpia y elimina el moho de forma rápida y efectiva.', 2), -- Muffyxid
(17.99, '¡Gran descuento! Desinfecta y elimina el moho de baños y cocinas con este limpiador.', 3), -- SaniCentro eliminador de moho
(13.27, '¡Precio especial! Elimina el moho de tejados y suelos de forma eficaz.', 4), -- Idroless 2 Lts
(27.23, '¡Oferta limitada! Elimina mohos, verdines y musgos de todo tipo de superficies lavables.', 5), -- Spray limpiador y eliminador de moho y verdin
(45.00, '¡Gran oferta! Limpia las manchas más complicadas provocadas por el moho o la humedad.', 6), -- MPL limpiador antimoho 500ml
(54.00, '¡Oferta increíble! Elimina hongos y bacterias causantes del mal olor de forma eficaz.', 7), -- Limpiador Antihongos great Value de 1L
(90.00, '¡Precio especial por tiempo limitado! Limpia de forma efectiva moho, hongos y musgo en paredes y techos.', 8), -- LIMPIADOR DE MOHO 85 GLADIO FM CON PULVERIZADOR 500 ML
(22.50, '¡Oferta exclusiva! Resuelve de modo profesional y definitivo el problema del moho en casa.', 9); -- NUNCAS Spray Antimoho



-- Inserción en la tabla COMPRA
INSERT INTO COMPRA (Fecha, Total, UsuarioID) VALUES
('2024-06-01', 92.49, 1),  -- Compra 1 de Ana Martínez
('2024-06-02', 65.75, 1),  -- Compra 2 de Ana Martínez
('2024-06-03', 79.98, 2),  -- Compra 1 de Juan López
('2024-06-04', 89.50, 2),  -- Compra 2 de Juan López
('2024-06-05', 110.98, 3), -- Compra 1 de María Rodríguez
('2024-06-06', 75.49, 3);  -- Compra 2 de María Rodríguez

-- Inserción en la tabla DETALLE_COMPRA
INSERT INTO DETALLE_COMPRA (Cantidad, CompraID, ProductoID) VALUES
(1, 1, 1),   -- 1 unidad de HG Antimoho en la compra 1 de Ana Martínez
(2, 1, 2),   -- 2 unidades de Muffyxid en la compra 1 de Ana Martínez
(1, 2, 3),   -- 1 unidad de SaniCentro eliminador de moho en la compra 2 de Ana Martínez
(2, 2, 4),   -- 2 unidades de Idroless 2 Lts en la compra 2 de Ana Martínez
(1, 3, 5),   -- 1 unidad de Spray limpiador y eliminador de moho y verdin en la compra 1 de Juan López
(2, 3, 6),   -- 2 unidades de MPL limpiador antimoho 500ml en la compra 1 de Juan López
(1, 4, 7),   -- 1 unidad de Limpiador Antihongos great Value de 1L en la compra 2 de Juan López
(1, 4, 8),   -- 1 unidad de LIMPIADOR DE MOHO 85 GLADIO FM CON PULVERIZADOR 500 ML en la compra 2 de Juan López
(1, 5, 9),   -- 1 unidad de NUNCAS Spray Antimoho en la compra 1 de María Rodríguez
(2, 5, 10),  -- 2 unidades de HARPIC Limpiador Líquido Baños Antihongos en la compra 1 de María Rodríguez
(1, 6, 11),  -- 1 unidad de SPRAY ANTIMOHO STOP JUNTAS NEGRAS en la compra 2 de María Rodríguez
(1, 6, 12);  -- 1 unidad de Aerosol Antimoho W, Limpiador De Moho, Limpieza Antimoho Cz8 en la compra 2 de María Rodríguez





"""