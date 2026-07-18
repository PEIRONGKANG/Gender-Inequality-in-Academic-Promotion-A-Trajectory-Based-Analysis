-- Read-only field and coverage scan for the Study 2/Study 3 narrative.

SELECT table, position, name, type
FROM system.columns
WHERE database = 'cna'
  AND table IN (
    'jp_researchers', 'jp_researchers_extra',
    'v_jp_researchers_degree_of_doctor_detail',
    'jp_researchers_research_experience',
    'jp_researchers_institute_property',
    'jp_researchers_research_areas',
    'v_jp_researchers_kaken_project',
    'v_jp_researchers_kaken_project_member',
    'v_jp_researchers_kaken_project_annual_budget'
  )
ORDER BY table, position;

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

SELECT min(budget_year), max(budget_year), count(), uniqExact(kaken_id),
       countIf(isNull(direct_budget)), countIf(isNull(total_budget))
FROM cna.v_jp_researchers_kaken_project_annual_budget;
