create table item (
    sku text primary key,
    name text not null,
    reorder_level integer not null default 0
);

create table movement (
    id integer primary key,
    sku text not null,
    day text not null,
    kind text not null,
    qty integer not null,
    unit_cents integer
);

create table setting (
    name text primary key,
    val text not null
);
