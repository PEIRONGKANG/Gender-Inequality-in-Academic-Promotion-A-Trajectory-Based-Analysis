-- Complete field inventory for the live ClickHouse cna database.
-- Read-only snapshot exported on 2026-07-24 (Asia/Tokyo).

SELECT
    c.database AS database_name,
    c.table AS source_object,
    if(t.engine = 'View', 'VIEW', 'TABLE') AS object_type,
    t.engine AS object_engine,
    t.total_rows AS object_total_rows,
    t.metadata_modification_time AS object_modified_at,
    t.comment AS object_comment,
    c.position AS field_position,
    c.name AS field_name,
    c.type AS field_type,
    startsWith(c.type, 'Nullable(') AS is_nullable,
    c.default_kind,
    c.default_expression,
    c.comment AS field_comment,
    c.is_in_partition_key,
    c.is_in_sorting_key,
    c.is_in_primary_key,
    c.is_in_sampling_key,
    c.compression_codec,
    c.serialization_hint
FROM system.columns AS c
LEFT JOIN system.tables AS t
    ON c.database = t.database
    AND c.table = t.name
WHERE c.database = 'cna'
ORDER BY c.table, c.position
FORMAT CSVWithNames;
