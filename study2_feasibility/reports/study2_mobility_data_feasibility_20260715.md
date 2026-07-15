# Study 2 机构流动与首次 AP 晋升时间：数据可行性审计

审计日期：2026-07-15（Asia/Tokyo）  
数据源：ClickHouse `cna`，只读实时查询。

## 结论

Study 2 在数据规模上可行。博士年份、性别与职业记录的初步联结人口为 58,610 人；在尚未执行全部职业史覆盖排除规则前，可用首次 AP 事件约 21,860，另有约 32,025 名没有观察到 AP 的删失候选。主模型可以研究既往机构流动次数与首次 AP 晋升时间的关联，并检验性别交互。

可行不等于可以直接建模。机构代码、职级文本、并行任职和首次观察即 AP 必须先处理。特别是：35.66% 的职业记录使用未知机构代码 `9999999999`；40.83% 的记录没有专门的日英职称字段；按保守宽职级规则仍有 46.51% 无法映射。年度层面的重叠任职很多，因此“机构移动”必须基于标准化主要机构序列，而不能简单对原始记录计数。

## 一、相关表和字段

| 功能 | 实时表或视图 | 关键字段 | 判断 |
|---|---|---|---|
| 研究者基本信息 | `jp_researchers` | `user_id`, 姓名字段, `created`, `modified` | `user_id` 是研究主键 |
| 性别 | `jp_researchers_extra` | `user_id`, `gender` | 无原生 `gender_source` |
| 教育与博士学位 | `jp_researchers_degrees`; `v_jp_researchers_degree_of_doctor`; `v_jp_researchers_degree_of_doctor_detail` | `degree_date`, `degreeType`, `degree_institute`, `discipline` | `phd_year` 为派生字段 |
| 职业/研究经历 | `jp_researchers_research_experience` | `rm_id`, `from_date`, `to_date`, `rm_institution_code`, affiliation/section/job 日英字段, `address_country`, `modified` | Study 2 核心来源 |
| 当前所属 | `jp_researchers_affiliations` | affiliation/section/job 日英字段, `rm_institution_code` | 无任职起止日期，不替代职业史 |
| 机构标准化 | `jp_researchers_institute_property` | `original_institute`, `college`, `college_country` | 基于字符串映射；不是稳定机构 ID 横表 |
| 职称标准化 | **没有独立表** | 从 research experience 的 job 与 affiliation 文本派生 | 必须生成职称审计表 |
| 机构属性 | `jp_researchers_institute_property` | `zone`, `operation_type`, `college_type` | 三列当前全部为空 |
| 学科分类 | `jp_researchers_research_areas`; doctor-detail view | `discipline_number`, `discipline_ja/en`, `research_field_ja/en`; `discipline` | 可构建研究领域及博士学科 |

## 二、重点字段存在性

原生存在或可直接别名：`researchmap_user_id` (`jp_researchers.user_id`)、`gender`、`career_record_id` (`rm_id`)、机构/职称原始文本、`from_date`、`to_date`、`country` (`address_country`)、`record_updated_at` (`modified`)。

需要派生：`researcher_id`（对 `user_id` 的分析别名）、`phd_year`、`degree_type`、`field`、`institution_name_standardized`、`institution_id`（使用 `rm_institution_code`，未知代码置空）、`rank_standardized`、开始/结束年月、`is_current`。

当前不存在或不能可靠构建：`gender_source` 原生字段、`primary_affiliation_flag`、`full_time_flag`、`prefecture`。`institution_type` 列存在，但当前 20,910 行中 `college_type`、`operation_type` 和 `zone` 全部为空，暂不可用于模型。

完整字段字典见 `data/study2_field_dictionary_20260715.csv`。
13 个相关表/视图的实时完整字段结构见 `data/study2_live_source_schema_20260715.csv`。

## 三、日期、排序和职业史解释

1. **日期精度。** `from_date` 中 230,826 行只有年份，585,382 行精确到年月，45,894 行为完整日期，43,204 行为空。`to_date` 对应为 327,762、426,556、33,542 和 117,446 行。另有 160,058 条结束年份为 `9999`，表示当前/开放区间。
2. **同年排序。** 148,316 个研究者-开始年份组合包含多条记录，只有 31,966 组可凭完整的不同月份/日期全部排序；116,350 组存在年内顺序歧义。可按月排序的记录可以排序，只有年份的记录必须标记为并列或顺序未知。
3. **主要与副所属。** 没有结构化标记。必须建立透明的主要任职选择规则，并保留并行所属数量。
4. **全职、兼职、访问、客座。** 没有结构化 employment-status 字段。部分信息出现在自由文本职称中，只能做低置信度文本分类，不能作为完整控制变量。
5. **机构别名。** `institute_property` 可把部分原始字符串映射到 `college`；17,110 个原始名称、446,728 条职业记录可精确匹配，行级覆盖为 49.35%。`rm_institution_code` 的已知代码覆盖为 64.34%。两者均不是完整历史别名系统。
6. **改名和合并。** 当前快照没有带生效日期的机构谱系表，不能可靠判断改名或合并是否沿用机构 ID。
7. **大学与下属单位。** 同一 `rm_institution_code` 常对应大量不同 affiliation 字符串，也存在大学、学部、研究科和附属医院的不同代码。不能预设全部共用一个 ID；需要建立 parent-institution crosswalk。
8. **空白职业年份。** 只能解释为“未观察到记录”，不能解释为没有任职或离开学术界。
9. **首次 AP。** 使用 `准教授`、`associate professor`、`associate prof` 在日英 job 与 affiliation 文本中识别。61,200 人出现 AP 文本，其中 59,262 人有有效开始年份；1,938 人缺少有效 AP 开始年份。13,631 人的 AP 只能从 job 字段以外的 affiliation 文本识别，需单独质量标记。
10. **首次观察已经 AP。** 可以识别：5,375 名职业史研究者的最早有效任职日期即为 AP 或与 AP 并列。初步博士-性别-职业联结人口中有 1,709 人属于这一情况，应从主风险集排除或单独做左截断敏感性分析。

## 四、核心汇总

| 指标 | 数量或比例 |
|---|---:|
| 研究者总数（唯一 `user_id`） | 259,889 |
| 有性别 | 241,056 |
| 有博士年份 | 78,208 |
| 有职业经历 | 162,275 |
| 至少两条职业经历 | 139,567 |
| 可识别有效首次 AP 年份 | 59,262 |
| 首次观察已为 AP | 5,375 |
| 全体研究者中无有效 AP 年份 | 200,627 |
| 有职业记录但无有效 AP 年份 | 103,013 |
| 职业记录总数 | 905,306 |
| 未知机构代码率（`9999999999`） | 35.66% |
| 原始 job 字段同时为空 | 40.83% |
| 保守宽职级无法映射 | 46.51% |
| 开始年份缺失率 | 4.77% |
| 结束年份缺失率 | 12.97% |
| 年度层面重叠任职研究者 | 134,652 |
| 年度层面多机构并行研究者 | 115,781 |

最后两项是基于原始开放区间和原始机构键的**上限诊断**，会受到 `9999` 开放结束日期、下属单位代码和重复/嵌套记录影响。它们不能直接当作真实多重任职比例。

### “重叠职业记录”具体指什么

这里的记录是 `jp_researchers_research_experience` 中的职业/研究经历条目。它通常描述任职、研究职位或组织角色，但也可能包括访问、客座、兼职、副所属、部门变化或用户录入的其他经历。因此，“同年重叠”只表示两条记录的起止区间覆盖同一个日历年，不等于已经确认同一时间存在两份全职任职。

在 78,208 名有明确博士年份的研究者中，61,735 人至少有一条带有效开始年份的职业记录。按年度宽口径，57,099 人有同年多记录，54,361 人有同年多个机构键。其中相当一部分只是年内连续换职：34,274 人存在“上一机构在某月结束、下一机构在同年稍后月份开始”的不同机构记录。这些是顺序移动，不是同时任职。

只保留起止月份均可解析且结束日期不是开放 `9999` 的封闭区间后，42,463 人可进行更严格检查；18,761 人仍有月份重叠，17,548 人的重叠记录使用不同机构键。这个数字更接近并行任职候选，但仍可能包含访问/客座、副所属、同一大学下属单位代码不同或记录边界按月重叠。数据库没有 `primary_affiliation_flag`、`full_time_flag` 或结构化兼职标记，因此不能把这 17,548 人直接称为“同时全职任职”。

完全相同内容的重复记录并不是主要来源：有效博士年份人群中只有 278 名研究者出现这种精确重复。真正需要处理的是开放区间、年内顺序、并行角色和机构父子关系。

## 五、建议的 Study 2 构造规则

主风险集从 `phd_year + 1` 开始，在首次有效 AP 年、删失年或观察终点结束。排除首次观察即 AP、AP 不晚于博士年份、无有效博士年份及职业覆盖不足的研究者。机构移动计数只使用 year t 之前已发生的移动。

主机构序列应先进行记录去重、机构标准化、并行记录优先级选择和年内顺序质量标记。主解释变量为截至 t-1 的累计机构移动次数。线性、分类和样条/二次项应分别检验，以允许正向、负向或非线性关联。性别与移动次数的交互通过预测概率或边际效应解释。流动方向和发生时点是次级分析，不与主变量竞争理论中心。

## 六、脱敏样例

`data/study2_anonymized_career_examples_20260715.csv` 提供八类真实结构、完全脱敏的职业轨迹：校内晋升、换机构晋升、同年换机构并晋升、多次流动未晋升、多重所属、职业经历缺失、机构名称变化和海外经历。研究者 ID 使用不可逆哈希，机构在每个案例内重标为 `Institution_A/B/...`，不包含姓名或真实机构名。

## 限制

本审计确认的是数据构造可行性，不是模型结果。AP 文本规则、机构父子关系、主要任职选择、开放区间及职业史覆盖仍需人工抽查和敏感性分析。空白职业史不能作为没有工作，机构移动也不能预设为有利或不利。
