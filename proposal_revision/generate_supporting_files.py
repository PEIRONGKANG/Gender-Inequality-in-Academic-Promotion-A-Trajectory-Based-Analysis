#!/usr/bin/env python3
"""Generate proposal revision audits, bibliography, logs, and documentation."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = Path("/Users/darin/BaiduDriver/TU/JRM/jrm/Doctoral_Dissertation_Proposal_PEI_Rongkang_BH_0704_Claude_tracked_revision2.docx")


TERMS = [
    ("researchmap", "researchmap", "ResearchMap; research map", "Lowercase except official titles or sentence start"),
    ("KAKEN", "KAKEN", "Kaken; kaken", "Database/system label"),
    ("Grants-in-Aid for Scientific Research", "Grants-in-Aid for Scientific Research", "grant-in-aid", "Define KAKEN on first use"),
    ("Associate Professor", "Associate Professor", "associate professor; associate-professor", "Use AP only after definition"),
    ("Full Professor", "Full Professor", "full professor; full-professor", "Use FP only after definition"),
    ("AP", "AP", "A.P.; ap", "Abbreviation after first definition"),
    ("FP", "FP", "F.P.; fp", "Abbreviation after first definition"),
    ("PI", "PI", "P.I.; principal-investigator", "Project-year role"),
    ("Co-I", "Co-I", "CO-I; CoI; coi", "Project-year role; define once"),
    ("KAKEN access", "KAKEN access", "funding access when participation only", "Observed participation measure"),
    ("KAKEN project category", "KAKEN project category", "grant tier as category", "Original research_category retained"),
    ("KAKEN-based collaboration networks", "KAKEN-based collaboration networks", "co-authorship network", "Formal project co-participation only"),
    ("career-relevant academic resources", "career-relevant academic resources", "academic capital", "Avoid implying pure merit"),
    ("promotion timeline", "promotion timeline", "promotion speed", "Elapsed duration between milestones"),
    ("promotion risk", "promotion risk", "promotion probability when hazard intended", "Annual transition risk"),
    ("first observed Associate Professor transition", "first observed Associate Professor transition", "first AP promotion", "Use when emphasizing observation"),
    ("researcher-year", "researcher-year", "researcher year", "Hyphenated unit"),
    ("event-history analysis", "event-history analysis", "event history analysis", "Hyphenated modifier"),
    ("event-time panel", "event-time panel", "event time panel", "Hyphenated modifier"),
    ("time-ordered association", "time-ordered association", "effect; impact", "Non-causal interpretation"),
    ("post-promotion trajectories", "post-promotion trajectories", "post promotion outcomes", "Hyphenated modifier"),
    ("cumulative advantage", "cumulative advantage", "Matthew effect when generic", "Theory label"),
    ("institutional mobility", "institutional mobility", "job switching; school hopping", "Organizational boundary changes"),
    ("institutional move", "institutional move", "school change", "Canonical institution change"),
    ("institutional prestige", "institutional prestige", "university quality", "Status, not quality"),
    ("institutional size", "institutional size", "university quality", "Scale, not quality"),
    ("multichannel sequence analysis", "multichannel sequence analysis", "multi-channel sequence analysis", "Method name"),
    ("right-censoring", "right-censoring", "right censoring", "Hyphenated noun"),
    ("field-year standardized funding", "field-year standardized funding", "field adjusted funding", "Hyphenated modifier"),
    ("women and men", "women and men", "female and male researchers", "Use unless sex classification is intended"),
    ("gender differences", "gender differences", "gender effect", "Avoid causal implication"),
    ("associated with", "associated with", "influences; leads to; produces", "Use for observational estimates"),
]


CITATIONS = [
    ("acker1990", "Acker, Joan", "1990", "Hierarchies, jobs, bodies: A theory of gendered organizations", "Gender & Society", "10.1177/089124390004002002", "SAGE", "yes", "Gendered organizations and ideal-worker assumptions", "Study 2", "Publisher page checked", "", "acker1990"),
    ("allison_long1987", "Allison, Paul D.; Long, J. Scott", "1987", "Interuniversity mobility of academic scientists", "American Sociological Review", "10.2307/2095600", "JSTOR", "yes", "Academic mobility is patterned by productivity and institutional location", "Study 2", "Metadata and issue page checked", "", "allison_long1987"),
    ("bielby_bielby1992", "Bielby, William T.; Bielby, Denise D.", "1992", "I will follow him: Family ties, gender-role beliefs, and reluctance to relocate for a better job", "American Journal of Sociology", "10.1086/229901", "Crossref", "yes", "Household relocation decisions are gendered", "Study 2", "Metadata checked", "", "bielby_bielby1992"),
    ("canibano2016", "Cañibano, Carolina; Fox, Mary Frank; Otamendi, F. Javier", "2016", "Gender and patterns of temporary mobility among researchers", "Science and Public Policy", "10.1093/scipol/scv042", "Oxford Academic", "yes", "Gender differences in timing, frequency, duration, and distance of research mobility", "Study 2", "Publisher abstract checked", "", "canibano2016"),
    ("fernandez_zubieta2016", "Fernández-Zubieta, Ana; Geuna, Aldo; Lawson, Cornelia", "2016", "Productivity pay-offs from academic mobility: Should I stay or should I go?", "Industrial and Corporate Change", "10.1093/icc/dtv034", "Oxford Academic", "yes", "Direction of mobility matters more than mobility per se", "Study 2", "Publisher abstract checked", "", "fernandez_zubieta2016"),
    ("gauthier2010", "Gauthier, Jacques-Antoine; Widmer, Eric D.; Bucher, Philipp; Notredame, Cédric", "2010", "Multichannel sequence analysis applied to social science data", "Sociological Methodology", "10.1111/j.1467-9531.2010.01227.x", "Crossref", "yes", "Methodological basis for separate sequence channels", "Study 2", "Metadata checked", "", "gauthier2010"),
    ("abbott_tsay2000", "Abbott, Andrew; Tsay, Angela", "2000", "Sequence analysis and optimal matching methods in sociology: Review and prospect", "Sociological Methods & Research", "10.1177/0049124100029001001", "SAGE", "yes", "Optimal Matching and sociological sequence analysis", "Study 2", "Metadata checked", "", "abbott_tsay2000"),
    ("clauset2015", "Clauset, Aaron; Arbesman, Samuel; Larremore, Daniel B.", "2015", "Systematic inequality and hierarchy in faculty hiring networks", "Science Advances", "10.1126/sciadv.1400005", "Science", "yes", "Faculty hiring markets are prestige-hierarchical", "Study 2/3", "Publisher page checked", "", "clauset2015"),
    ("wapman2022", "Wapman, K. Hunter; Zhang, Sam; Clauset, Aaron; Larremore, Daniel B.", "2022", "Quantifying hierarchy and dynamics in US faculty hiring and retention", "Nature", "10.1038/s41586-022-05222-x", "Nature", "yes", "Institutional hierarchy and retention dynamics", "Study 2", "Publisher metadata checked", "", "wapman2022"),
    ("bol2018", "Bol, Thijs; de Vaan, Mathijs; van de Rijt, Arnout", "2018", "The Matthew effect in science funding", "Proceedings of the National Academy of Sciences", "10.1073/pnas.1719557115", "PNAS/Crossref", "yes", "Early funding success is associated with later funding accumulation", "Study 3", "Publisher/news metadata checked", "", "bol2018"),
    ("wang2019", "Wang, Yang; Jones, Benjamin F.; Wang, Dashun", "2019", "Early-career setback and future career impact", "Nature Communications", "10.1038/s41467-019-12189-3", "Nature", "yes", "Near-miss funding outcomes relate to later participation and impact", "Study 3", "Full publisher page checked", "", "wang2019"),
    ("li2019", "Li, Wei; Aste, Tomaso; Caccioli, Fabio; Livan, Giacomo", "2019", "Early coauthorship with top scientists predicts success in academic careers", "Nature Communications", "10.1038/s41467-019-13130-4", "Nature", "yes", "Early relational position predicts later career outcomes in another network context", "Study 3", "Full publisher page checked", "", "li2019"),
    ("diprete_eirich2006", "DiPrete, Thomas A.; Eirich, Gregory M.", "2006", "Cumulative advantage as a mechanism for inequality", "Annual Review of Sociology", "10.1146/annurev.soc.32.061604.123127", "Crossref", "yes", "Cumulative-advantage theory", "Study 3", "Metadata checked", "", "diprete_eirich2006"),
    ("merton1968", "Merton, Robert K.", "1968", "The Matthew effect in science", "Science", "10.1126/science.159.3810.56", "Crossref", "yes", "Foundational cumulative-advantage account", "Study 3", "Metadata checked", "", "merton1968"),
    ("nielsen2016", "Nielsen, Mathias W.", "2016", "Limits to meritocracy? Gender in academic recruitment and promotion processes", "Science and Public Policy", "10.1093/scipol/scv052", "Zotero/Crossref", "yes", "Gendered evaluation persists in formalized procedures", "Shared theory", "Metadata and Zotero duplicate checked", "GVFNLQ7L", "nielsen2016"),
    ("pei2026", "Pei, Rongkang; Lyu, Zeyu; Wang, Guolong; Wang, Zhichao; Ye, Maoxin; Fan, Xiaoguang", "2026", "Gender inequality in academic promotion trajectories in Japan", "Scientific Reports", "10.1038/s41598-026-54562-5", "Nature", "yes", "Official Study 1 sample and findings", "Study 1", "Publisher page checked", "", "pei2026"),
    ("takahashi2015", "Takahashi, Ana Maria; Takahashi, Shingo", "2015", "Gender promotion differences in economics departments in Japan: A duration analysis", "Journal of Asian Economics", "10.1016/j.asieco.2015.09.002", "Zotero/Crossref", "yes", "Japanese promotion duration evidence", "Study 1/context", "Metadata checked", "DU64M49W", "takahashi2015"),
    ("nagano2022", "Nagano, Natsuko; Watari, Takashi; Tamaki, Yukihisa; Onigata, Kazumichi", "2022", "Japan's academic barriers to gender equality as seen in a comparison of public and private medical schools", "Women's Health Reports", "10.1089/whr.2021.0082", "Zotero/Crossref", "yes", "Gendered rank inequality in Japanese medical academia", "Context", "Metadata checked", "6FZ8VN3X", "nagano2022"),
    ("watanabe2025", "Watanabe, Megumi", "2025", "Gender inequality in international research engagement amid transformation to global and neoliberal academia: The case of Japan", "Gender, Work & Organization", "10.1111/gwao.13224", "Zotero/Crossref", "yes", "Gendered international engagement in Japan", "Context/Study 2", "Metadata checked", "GNUIKBTM", "watanabe2025"),
    ("huang2020", "Huang, Junming; Gates, Alexander J.; Sinatra, Roberta; Barabási, Albert-László", "2020", "Historical comparison of gender inequality in scientific careers across countries and disciplines", "PNAS", "10.1073/pnas.1914221117", "Zotero/Crossref", "yes", "Cross-national longitudinal career inequality", "Context", "Metadata checked", "PHUXQUAJ", "huang2020"),
    ("lawson_shibayama2015", "Lawson, Cornelia; Shibayama, Sotaro", "2015", "International research visits and careers: An analysis of bioscience academics in Japan", "Science and Public Policy", "10.1093/scipol/scu084", "Crossref", "yes", "International mobility in Japanese academic careers", "Study 2", "Metadata checked", "", "lawson_shibayama2015"),
    ("moher2018", "Moher, David et al.", "2018", "Assessing scientists for hiring, promotion, and tenure", "PLOS Biology", "10.1371/journal.pbio.2004089", "Crossref", "yes", "Limits of narrow evaluation metrics", "Shared theory", "Metadata checked", "", "moher2018"),
    ("schimanski2018", "Schimanski, Lesley A.; Alperin, Juan Pablo", "2018", "The evaluation of scholarship in academic promotion and tenure processes", "F1000Research", "10.12688/f1000research.16493.1", "Crossref", "yes", "Promotion evaluation practices", "Shared theory", "Metadata checked", "", "schimanski2018"),
    ("sato2021", "Sato, Sayaka; Gygax, Pascal M.; Randall, Julian; Schmid Mast, Marianne", "2021", "The leaky pipeline in research grant peer review and funding decisions", "Higher Education", "10.1007/s10734-020-00626-y", "PMC/Springer", "yes", "Mixed evidence on gender in grant review", "Study 3", "Full text checked", "", "sato2021"),
    ("jst2026", "Japan Science and Technology Agency", "2026", "About the researchmap project", "Official website", "", "researchmap/JST", "official", "researchmap governance and scope", "Data", "Official page checked", "CZ4DWNVN", "jst2026"),
    ("jsps2026a", "Japan Society for the Promotion of Science", "2026", "KAKENHI: Types of grants programs", "Official website", "", "JSPS", "official", "KAKEN category purposes and funding ranges", "Study 3", "Official page checked", "", "jsps2026a"),
    ("jsps2026b", "Japan Society for the Promotion of Science", "2026", "KAKENHI award trends", "Official website", "", "JSPS", "official", "KAKEN application and award context", "Study 3", "Official page checked", "", "jsps2026b"),
    ("statistics_japan2025", "Statistics Bureau of Japan", "2025", "Statistical handbook of Japan 2025", "Official statistics", "", "Statistics Bureau", "official", "Women represented 18.5% of researchers in 2024", "Context", "Official PDF/page checked", "", "statistics_japan2025"),
]


def write_csv(path: Path, headers: list[str], rows: list[tuple]) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def bib_escape(value: str) -> str:
    return value.replace("&", r"\&").replace("%", r"\%")


def build_bib() -> str:
    entries = []
    for key, authors, year, title, venue, doi, source, peer, claim, relevance, fulltext, zotero, bibkey in CITATIONS:
        kind = "misc" if peer == "official" else "article"
        fields = [f"  title = {{{bib_escape(title)}}}", f"  author = {{{bib_escape(authors.replace(';', ' and'))}}}", f"  year = {{{year}}}"]
        if kind == "article":
            fields.append(f"  journal = {{{bib_escape(venue)}}}")
        else:
            fields.append(f"  howpublished = {{{bib_escape(venue)}}}")
        if doi:
            fields.append(f"  doi = {{{doi}}}")
            fields.append(f"  url = {{https://doi.org/{doi}}}")
        elif key == "jst2026":
            fields.append("  url = {https://researchmap.jp/public/about/operations}")
        elif key == "jsps2026a":
            fields.append("  url = {https://www.jsps.go.jp/english/e-grants/grants01.html}")
        elif key == "jsps2026b":
            fields.append("  url = {https://www.jsps.go.jp/english/e-grants/award_trends.html}")
        elif key == "statistics_japan2025":
            fields.append("  url = {https://www.stat.go.jp/english/data/handbook/}")
        entries.append(f"@{kind}{{{bibkey},\n" + ",\n".join(fields) + "\n}")
    return "\n\n".join(entries) + "\n"


def main() -> None:
    source_sha = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    write_csv(ROOT / "terminology_control_table.csv",
              ["protected_term", "preferred_form", "disallowed_or_review_form", "usage_rule"], TERMS)
    write_csv(ROOT / "citation_audit.csv",
              ["record_id", "authors", "year", "title", "journal_or_source", "doi", "database_source",
               "peer_reviewed_status", "exact_claim_supported", "study_relevance", "full_text_or_page_checked",
               "zotero_item_key", "bibtex_key"], CITATIONS)
    (ROOT / "references.bib").write_text(build_bib(), encoding="utf-8")
    (ROOT / "literature_search_log.md").write_text(f"""# Literature Search Log

## Scope and date

Searches were conducted on 10–11 July 2026 for the Study 2 institutional-mobility reframing and the Study 3 KAKEN-resource design. Metadata were verified before use. The source-proposal SHA-256 is `{source_sha}`.

## Zotero workflow

- Zotero 9.0.4 local API and connector returned HTTP 200.
- Inventory: 62 top-level BibTeX entries; relevant collection `Japan Research Map`.
- Focused queries: academic mobility gender; gendered organizations; linked lives mobility; dual career academic mobility; KAKEN gender; research funding academic promotion; collaboration networks academic careers; sequence analysis careers.
- Exact phrase searches returned no additional local matches; broader inventory review identified Study 1, Japanese academia, meritocracy, and gender-career sources.
- Zotero item keys and BibTeX keys remain separate in `citation_audit.csv`.
- No web-discovered records were imported into Zotero. Verified web records were staged in `references.bib` only.

## Web discovery and verification

1. Publisher searches: SAGE, Oxford Academic, Nature, Science, PNAS, Springer/PMC, J-STAGE.
2. Official sources: JST/researchmap, JSPS/KAKENHI, Statistics Bureau of Japan.
3. DOI verification: Crossref API metadata for 28 candidate DOIs; the malformed Sato DOI was corrected from a non-resolving suffix to `10.1007/s10734-020-00626-y`; Allison and Long was corrected to `10.2307/2095600`.
4. Full publisher pages or abstracts were checked for the claims assigned in `citation_audit.csv`. Full attachments were not retrieved indiscriminately.

## Search blocks retained for reproduction

- `academic mobility gender career advancement`
- `institutional mobility academic careers`
- `faculty mobility institutional prestige`
- `gendered organizations academic careers`
- `linked lives geographic mobility careers`
- `dual-career couples academic mobility`
- `sequence analysis academic career mobility`
- `research funding academic promotion gender`
- `KAKEN gender funding Japan`
- `collaboration networks academic promotion`
- `cumulative advantage research funding`

## Inclusion rules

Peer-reviewed articles, major reviews, established theoretical work, and official institutional/statistical sources were prioritized. Search snippets, Wikipedia, generic blogs, and unverifiable references were excluded. A source entered the manuscript only after title, authors, year, and DOI or official URL were checked.
""", encoding="utf-8")
    (ROOT / "unresolved_issues.md").write_text("""# Unresolved Issues

1. **Institution properties:** `jp_researchers_institute_property` is not yet available to the analysis account. Current institution-type and elite-tie string heuristics must be replaced and compared with official properties once access is granted.
2. **Institution geography:** prefecture, region, coordinates, and distance require a validated institution crosswalk. No geographic mobility variable is currently claimed as available.
3. **Rankings:** THE, QS, and ARWU historical files and institution crosswalks have not yet been assembled. Coverage varies by year and cannot be projected backward.
4. **Institution size:** historical student and full-time-faculty counts require an institution-year source and crosswalk. Student counts will measure scale, not quality.
5. **AP chronology:** first AP year must continue to be validated against raw research-experience titles; already-AP-at-first-observation and ambiguous chronology require separate flags.
6. **KAKEN linkage:** the KAKEN website user ID and JPR `userId` remain distinct. Unlinked members must remain in fractional denominators.
7. **Private mobility costs:** partnership, fertility, childcare, eldercare, and relocation costs are theoretically relevant but not observed in the current data.
8. **Career exit:** missing researchmap history does not identify academic exit. Exit outcomes require direct evidence.
9. **Tracked changes granularity:** because the proposal was comprehensively restructured, the tracked copy marks the revised body as insertions rather than representing every deleted source paragraph one by one. Accepting all changes yields the clean copy exactly.
10. **Table of Contents:** the reading copy uses a verified static contents list. Word page-number fields should be refreshed in the university's final submission environment if page-numbered TOC entries are required.
""", encoding="utf-8")
    (ROOT / "proposal_structure_map.md").write_text("""# Proposal Structure Map

| Section | Role | Population/unit | Primary outcome or target | Method | Interpretation boundary |
|---|---|---|---|---|---|
| Abstract | Three-study synthesis | Dissertation | timing → mobility → resources | Summary | Descriptive and associational |
| 1. Introduction | Gap and questions | Japanese academic careers | Overarching RQ | Linked longitudinal design | No causal claim |
| 2. Literature | Theory-variable bridge | Prior evidence | Mobility/resources mechanisms | Structured review | Unobserved mechanisms labelled |
| 3. Study 1 | Completed diagnostic study | Official researchmap samples | Promotion timeline | Duration/survival analyses | Completed-transition selection and censoring |
| 4. Study 2 | Gendered mobility strategy | Researcher-year and career sequence | AP transition; mobility pathways | Cloglog/logit/Cox; multichannel sequence analysis | Mobility-career associations |
| 5. Study 3 | KAKEN access and relational resources | Researcher-year; AP event-time panel | AP transition; KAKEN trajectories | Resource descriptions; cloglog/logit/Cox; event-time extension | Time-ordered associations, not causal returns |
| 6. Data | Shared architecture | Researcher, institution, project, year | Validated linked panels | Reproducible ETL and audits | Coverage/linkage separated from zero |
| 7. Contributions | Division of labour and schedule | Dissertation | Four contributions | Synthesis | Claims bounded by observation |
| Appendix A | Operational definitions | Variable level | Construction and validation | Formal tables | Limitations and robustness explicit |

## Research-question coverage

- RQ1 → Section 3: observed timing, transition entry, and right-censoring.
- RQ2a–c → Sections 4.3–4.6: mobility incidence, direction, and gender interactions.
- RQ2d → Section 4.7: multichannel pathway typology.
- RQ2e → Section 4.8: equal-destination comparison.
- RQ3a → Sections 5.3–5.5: resource-access descriptions.
- RQ3b–c → Sections 5.2 and 5.5: lagged promotion-risk models and selected interactions.
- RQ3d → Section 5.6: secondary post-AP event-time extension.
""", encoding="utf-8")
    (ROOT / "proposal_revision_memo.md").write_text("""# Proposal Revision Memo

## A. Executive summary

The proposal has been reorganized from **Study 2 = KAKEN promotion-risk analysis** and **Study 3 = post-AP resource trajectories** to **Study 2 = institutional mobility as a gendered career strategy** and **Study 3 = gendered access to and returns from KAKEN resources and project-based networks**. Study 1 remains the completed diagnostic promotion-timeline study. The resulting logic is: **timing → mobility pathways → academic resources and returns**.

The Abstract, Introduction, research questions, dissertation structure, literature review, Studies 2 and 3, shared data architecture, contributions, work plan, conclusion, and appendix were rewritten. Study 1's official sample and reported descriptive results were preserved, while its interpretation now emphasizes selection into observed transitions and right-censoring.

## B. Research contribution

Study 1 identifies when gender differences appear. Study 2 asks how researchers move among organizations and whether the ability to move is an unequally distributed career resource. Study 3 examines access to KAKEN participation, leadership, funding intensity, category, and formal project-network positions. This division prevents mobility, funding, and post-promotion accumulation from being compressed into one ambiguous resource model.

Study 2 now engages career mobility, status attainment, segmented labour markets, gendered organizations, linked lives, and dual-career constraints. Study 3 engages sociology of science through cumulative advantage, competitive funding, project roles, and formal relational positions. Both designs remain descriptive and associational.

## C. Variable rationale

- **Move count and move rate** measure mobility frequency while adjusting for observation length.
- **Upward/lateral/downward mobility** distinguishes status direction using lagged within-ranking percentiles rather than treating all moves alike.
- **Prestige percentile and tier** separate annual relative status from broad sequence states; THE, QS, and ARWU are not averaged as raw ranks.
- **Institution size and doctoral enrolment** measure organizational scale and research-training capacity, not quality.
- **Institutional stability** separates long attachment, concentration, and repeated short spells from simple move counts.
- **KAKEN access** identifies observed entry into the funding system and remains distinct from linkage failure.
- **PI and Co-I roles** measure project-year leadership and participation; cumulative histories capture progression.
- **Funding** uses a two-part access/intensity design with full and fractional allocations; all identifiable members remain in denominators.
- **KAKEN project category** comes from `v_jp_researchers_kaken_project.research_category` and remains uncollapsed in the main data.
- **Degree, PI outdegree, and PI indegree** measure formal project-based breadth, leadership reach, and inclusion. They are not co-authorship or mentoring measures.

## D. Theory dialogue

The revised Study 2 treats institutional mobility as an organizationally structured option. Gendered-organization theory explains why geographic flexibility may be rewarded; linked-lives theory locates moving within households; segmented-labour-market and status-attainment perspectives explain why origin, destination, and direction matter. The proposal explicitly separates observed mobility from hypothesized family and private costs.

Study 3 treats KAKEN roles, funding, category, and networks as career-relevant academic resources rather than pure merit. Cumulative-advantage theory motivates prior exposure and post-AP trajectories, while the analysis avoids claiming that KAKEN or AP promotion causes later advantage.

## E. Remaining gaps

Official institution properties, validated geography, historical rankings, institution student-year data, and some AP chronology checks remain incomplete. Their required sources and validation steps are listed in `unresolved_issues.md`. These gaps are represented as unavailable or unresolved; no value is fabricated.

## Title review

- **Current title:** Identifying Gendered Patterns in Japanese Academic Careers: Promotion Timeline, KAKEN Resources, Collaboration Networks, and Post-Promotion Trajectories.
- **Minimal-change option:** Identifying Gendered Patterns in Japanese Academic Careers: Promotion Timelines, Institutional Mobility, KAKEN Resources, and Collaboration Networks.
- **Stronger option:** Gendered Academic Careers in Japan: Promotion Timing, Institutional Mobility, and Access to KAKEN Resources.
- **Recommendation:** Use the minimal-change option. It preserves the proposal's existing identity while accurately naming all three studies and avoiding a stronger causal or explanatory claim than the design supports.
""", encoding="utf-8")
    (ROOT / "source_manifest.md").write_text(f"""# Source Manifest

- Source file: `{SOURCE}`
- SHA-256: `{source_sha}`
- Source overwritten: **no**
- Revision date: 2026-07-11
- Source OOXML inventory: 243 paragraphs, 3 tables, 7 inline images, 4 comments, 100 insertions, 6 deletions.
- Output builder: `proposal_revision/build_proposal.py`
- Supporting-file builder: `proposal_revision/generate_supporting_files.py`
""", encoding="utf-8")


if __name__ == "__main__":
    main()
