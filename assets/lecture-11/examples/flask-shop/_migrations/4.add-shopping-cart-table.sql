BEGIN TRANSACTION;

DROP TABLE IF EXISTS shopping_cart_item;

CREATE TABLE shopping_cart_item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL REFERENCES customer (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    product_id INTEGER NOT NULL REFERENCES product (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    quantity INTEGER NOT NULL DEFAULT (1)
);

COMMIT TRANSACTION;
