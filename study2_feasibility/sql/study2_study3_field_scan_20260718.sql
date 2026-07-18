-- Read-only field and coverage scan for the Study 2/Study 3 field map.
-- Snapshot refreshed 2026-07-18 after the source-data update.

SELECT table, position, name, type
FROM system.columns
WHERE database = 'cna'
  AND table IN (
    'jp_researchers', 'jp_researchers_extra', 'jp_researchers_affiliations',
    'v_jp_researchers_degree_of_doctor_detail',
    'jp_researchers_research_experience',
    'jp_researchers_institute_property',
    'jp_researchers_research_areas',
    'v_jp_researchers_kaken_project',
    'v_jp_researchers_kaken_project_member',
    'v_jp_researchers_kaken_project_annual_budget'
  )
ORDER BY table, position;

SELECT count() AS rows,
       uniqExact(researcher_user_id) AS researchers,
       countIf(empty(from_date)) AS missing_from_date,
       countIf(empty(to_date)) AS missing_to_date,
       countIf(empty(job_ja) AND empty(job_en)) AS missing_job
FROM cna.jp_researchers_research_experience;

SELECT count() AS projects,
       countIf(isNull(research_category) OR empty(ifNull(research_category, ''))) AS missing_research_category,
       countIf(isNull(allocation_type) OR empty(ifNull(allocation_type, ''))) AS missing_allocation_type,
       countIf(isNull(research_field) OR empty(ifNull(research_field, ''))) AS missing_research_field,
       countIf(isNull(research_institution) OR empty(ifNull(research_institution, ''))) AS missing_research_institution
FROM cna.v_jp_researchers_kaken_project;

SELECT research_category, count() AS projects
FROM cna.v_jp_researchers_kaken_project
GROUP BY research_category
ORDER BY projects DESC;

SELECT count() AS member_rows,
       uniqExact(kaken_id) AS projects,
       uniqExactIf(user_id, notEmpty(ifNull(user_id, ''))) AS linked_researchers,
       countIf(notEmpty(ifNull(user_id, ''))) AS linked_rows,
       countIf(empty(ifNull(user_id, ''))) AS unlinked_rows,
       countIf(empty(ifNull(user_id, '')) AND notEmpty(ifNull(kaken_researcher_id, ''))) AS kaken_id_only_rows,
       countIf(notEmpty(ifNull(user_id, '')) AND empty(ifNull(kaken_researcher_id, ''))) AS researchmap_id_only_rows,
       countIf(notEmpty(ifNull(user_id, '')) AND notEmpty(ifNull(kaken_researcher_id, ''))) AS both_id_rows
FROM cna.v_jp_researchers_kaken_project_member;

SELECT role, role_detail, count() AS member_rows,
       uniqExact(kaken_id) AS projects,
       uniqExactIf(user_id, notEmpty(ifNull(user_id, ''))) AS linked_researchers,
       countIf(isNull(user_id) OR empty(ifNull(user_id, ''))) AS unlinked_member_rows
FROM cna.v_jp_researchers_kaken_project_member
GROUP BY role, role_detail
ORDER BY member_rows DESC;

SELECT count() AS rows,
       countIf(empty(college)) AS missing_college,
       countIf(empty(college_country)) AS missing_country,
       countIf(empty(admin1)) AS missing_admin1,
       countIf(isNull(admin2) OR empty(ifNull(admin2, ''))) AS missing_admin2,
       countIf(empty(operation_type)) AS missing_operation_type,
       countIf(empty(college_type)) AS missing_college_type
FROM cna.jp_researchers_institute_property;

SELECT min(budget_year) AS min_budget_year,
       max(budget_year) AS max_budget_year,
       count() AS project_year_rows,
       uniqExact(kaken_id) AS projects,
       countIf(isNull(budget_year)) AS missing_budget_year,
       countIf(isNull(direct_budget)) AS missing_direct_budget,
       countIf(isNull(total_budget)) AS missing_total_budget
FROM cna.v_jp_researchers_kaken_project_annual_budget;
