create trigger movement_guard
before insert on movement
begin
    select case
        when new.kind is null or new.kind not in ('receipt', 'issue', 'scrap')
            then raise(abort, 'bad kind')
    end;

    select case
        when
            new.sku is null
            or typeof(new.sku) <> 'text'
            or instr(new.sku, char(0)) > 0
            or length(new.sku) not between 1 and 12
            or new.sku glob '*[^a-z0-9-]*'
            then raise(abort, 'bad sku')
    end;

    select case
        when
            new.day is null
            or typeof(new.day) <> 'text'
            or new.day not glob '????-??-??'
            or substr(new.day, 1, 4) glob '*[^0-9]*'
            or substr(new.day, 6, 2) glob '*[^0-9]*'
            or substr(new.day, 9, 2) glob '*[^0-9]*'
            or new.day < '1970-01-01'
            or new.day > '2999-12-31'
            or date(new.day, '+0 days') is not new.day
            then raise(abort, 'bad day')
    end;

    select case
        when
            new.qty is null
            or typeof(new.qty) <> 'integer'
            or new.qty not between 1 and 1000000
            then raise(abort, 'bad quantity')
    end;

    select case
        when new.kind = 'receipt' and new.unit_cents is null
            then raise(abort, 'receipt needs unit_cents')
        when
            new.kind = 'receipt'
            and (
                typeof(new.unit_cents) <> 'integer'
                or new.unit_cents not between 0 and 100000000
            )
            then raise(abort, 'bad unit_cents')
        when new.kind in ('issue', 'scrap') and new.unit_cents is not null
            then raise(abort, 'only receipts have unit_cents')
    end;
end;

create trigger movement_no_update
before update on movement
when
    exists (
        select 1 from movement
        where movement.id = old.id
    )
begin
    select raise(abort, 'movements are append-only');
end;

create trigger movement_no_delete
before delete on movement
when
    exists (
        select 1 from movement
        where movement.id = old.id
    )
begin
    select raise(abort, 'movements are append-only');
end;

create trigger item_guard
before insert on item
begin
    select case
        when
            new.reorder_level is null
            or typeof(new.reorder_level) <> 'integer'
            or new.reorder_level < 0
            then raise(abort, 'bad reorder_level')
    end;
end;

create trigger setting_guard
before insert on setting
begin
    select case
        when new.name is null or new.name not in ('as_of', 'cover_window')
            then raise(abort, 'unknown setting')
    end;

    select case
        when
            new.name = 'as_of'
            and (
                new.val is null
                or typeof(new.val) <> 'text'
                or new.val not glob '????-??-??'
                or substr(new.val, 1, 4) glob '*[^0-9]*'
                or substr(new.val, 6, 2) glob '*[^0-9]*'
                or substr(new.val, 9, 2) glob '*[^0-9]*'
                or new.val < '1970-01-01'
                or new.val > '2999-12-31'
                or date(new.val, '+0 days') is not new.val
            )
            then raise(abort, 'bad as_of')
    end;

    select case
        when
            new.name = 'cover_window'
            and (
                new.val is null
                or typeof(new.val) <> 'text'
                or new.val glob '*[^0-9]*'
                or cast(new.val as integer) not between 1 and 365
                or cast(cast(new.val as integer) as text) <> new.val
            )
            then raise(abort, 'bad cover_window')
    end;
end;
