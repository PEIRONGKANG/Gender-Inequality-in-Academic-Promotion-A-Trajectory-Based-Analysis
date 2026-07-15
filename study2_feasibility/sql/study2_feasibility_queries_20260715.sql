-- Read-only ClickHouse feasibility audit for Study 2.
-- Database: cna. Credentials are supplied through JRM_CLICKHOUSE_PASSWORD.

-- Live source inventory.
SELECT name, engine, total_rows, metadata_modification_time
FROM system.tables
WHERE database = 'cna'
  AND (lower(name) LIKE '%researcher%' OR lower(name) LIKE '%institute%')
ORDER BY name;

-- Career date precision.
SELECT
  multiIf(empty(from_date), 'EMPTY',
          match(from_date, '^[0-9]{4}$'), 'YEAR',
          match(from_date, '^[0-9]{4}-[0-9]{1,2}$'), 'YEAR_MONTH',
          match(from_date, '^[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}$'), 'FULL_DATE',
          'OTHER') AS precision,
  count()
FROM cna.jp_researchers_research_experience
GROUP BY precision;

-- AP definition: do not use assistant-professor views.
-- Apply this expression to combined job and affiliation text:
-- position(lower_text, '准教授') > 0
-- OR match(lower_text, 'associate[ -]?prof(essor)?')

-- Unknown institution codes must be treated as missing.
SELECT rm_institution_code, count()
FROM cna.jp_researchers_research_experience
GROUP BY rm_institution_code
ORDER BY count() DESC;

-- Institution-property completeness.
SELECT
  count() AS rows,
  countIf(empty(college)) AS empty_college,
  countIf(empty(college_country)) AS empty_country,
  countIf(empty(zone)) AS empty_zone,
  countIf(empty(operation_type)) AS empty_operation_type,
  countIf(empty(college_type)) AS empty_college_type
FROM cna.jp_researchers_institute_property;

-- Exact standardization coverage.
SELECT
  count() AS career_rows,
  countIf(if(notEmpty(affiliation_ja), affiliation_ja, affiliation_en)
          IN (SELECT original_institute FROM cna.jp_researchers_institute_property)) AS matched_rows
FROM cna.jp_researchers_research_experience;

-- The report records additional CTE-based aggregate queries for first AP,
-- preliminary risk-set linkage, same-year ordering, and year-level overlaps.
-- All overlap figures are diagnostics before canonical primary-affiliation selection.

-- Follow-up overlap audit for the 78,208-researcher valid-PhD population:
-- 1. Expand valid career intervals to calendar years for an upper-bound overlap count.
-- 2. Restrict to month-precise, closed intervals and expand to months for a stricter count.
-- 3. Identify consecutive different-institution records where the previous record ends
--    before the next begins within the same year; these are sequential moves, not concurrency.
-- 4. Count exact duplicate content separately. Results are recorded in the summary CSV
--    and the report section “重叠职业记录具体指什么”.
