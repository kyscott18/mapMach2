PRAGMA foreign_keys = ON;

CREATE TABLE points(
    pointid INTEGER NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    PRIMARY KEY(pointid),
);

CREATE TABLE routes (
    routeid INTEGER NOT NULL, 
    template VARCHAR(64) NOT NULL,
    PRIMARY KEY(routeid),
);

CREATE TABLE loops(
    routeid INTEGER NOT NULL, 
    created DATETIME NOT NULL, 
    pointid INTEGER NOT NULL, 
    heading REAL NOT NULL,
    PRIMARY KEY(routeid, created, pointid),
    FOREIGN KEY(routeid) REFERENCES routes(routeid),
    FOREIGN KEY(pointid) REFERENCES points(pointid), 
);

