CREATE TABLE product (
    id          INTEGER        PRIMARY KEY AUTOINCREMENT,
    title       VARCHAR (50)   NOT NULL,
    description TEXT           NOT NULL,
    price       DECIMAL (5, 2) NOT NULL,
    is_sale     BOOLEAN        DEFAULT (false),
    stock       INTEGER        NOT NULL
);

CREATE TABLE customer (
    id        INTEGER      PRIMARY KEY AUTOINCREMENT,
    firstname VARCHAR (50) NOT NULL,
    lastname  VARCHAR (50) NOT NULL,
    phone     VARCHAR (15)
);

CREATE TABLE address (
    id          INTEGER      PRIMARY KEY AUTOINCREMENT,
    street      VARCHAR (50) NOT NULL,
    number      VARCHAR (5)  NOT NULL,
    postcode    VARCHAR (10) NOT NULL,
    customer_id INTEGER      NOT NULL
                             REFERENCES customer (id)
);

CREATE TABLE [order] (
    id          INTEGER      PRIMARY KEY AUTOINCREMENT,
    date        DATETIME     NOT NULL
                             DEFAULT (CURRENT_TIMESTAMP),
    status      VARCHAR (10) NOT NULL,
    customer_id INTEGER      REFERENCES customer (id)
                             NOT NULL
);

CREATE TABLE order_item (
    order_id   INTEGER REFERENCES [order] (id)
                       NOT NULL,
    product_id INTEGER REFERENCES product (id)
                       NOT NULL,
    quantity   INTEGER NOT NULL
                       DEFAULT (0)
);
