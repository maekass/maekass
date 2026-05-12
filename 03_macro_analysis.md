# Part III: Macroeconomic Analysis

## 3.1 Labor Market Context

**Figure 3.1: Tri-State Labor Force Participation Trends (2014–2034 projected)**

| Year | MA LFPR (%) | DC LFPR (%) | VA LFPR (%) | US LFPR (%) |
|---|---|---|---|---|
| 2014 | 66.8 | 71.2 | 67.5 | 62.9 |
| 2019 | 67.9 | 71.8 | 66.8 | 63.1 |
| 2024 | 65.4 | 70.1 | 64.9 | 62.7 |
| 2029 (proj.) | 64.1 | 68.7 | 63.5 | 61.8 |
| 2034 (proj.) | 63.2 | 67.4 | 62.4 | 60.9 |

*Source: lfpr_projections.csv. Analytics layer: visualized in Power BI/Tableau; projections estimated in R/Stata from BLS and CBO long-term outlook.*

**Table 3.1B: Skills Gap Analysis — Top 10 In-Demand Occupations with Shortages**

| Occupation | Annual Openings | Qualified Applicants | Gap | Median Wage ($/hr) |
|---|---|---|---|---|
| Registered Nurses | 12,400 | 8,200 | 4,200 | 42.80 |
| Software Developers | 9,800 | 6,500 | 3,300 | 58.40 |
| Electricians | 6,200 | 3,800 | 2,400 | 32.50 |
| HVAC Technicians | 4,800 | 2,900 | 1,900 | 28.70 |
| Medical Assistants | 8,100 | 5,600 | 2,500 | 20.40 |
| Construction Managers | 3,200 | 2,100 | 1,100 | 48.90 |
| Data Analysts | 5,400 | 3,700 | 1,700 | 41.20 |
| CDL Drivers | 11,200 | 7,800 | 3,400 | 24.10 |
| CNC Machinists | 3,600 | 2,300 | 1,300 | 26.80 |
| Cybersecurity Analysts | 4,100 | 2,400 | 1,700 | 52.60 |

*Source: skills_gap_analysis.csv. Analytics layer: R/Stata from BLS OEWS, state LMI, and Burning Glass/Lightcast data.*

## 3.2 GDP and Fiscal Impact

**Table 3.2A: Direct GDP Contribution of Program Graduates**

| Metric | Year 5 | Year 10 | Year 20 (Steady State) |
|---|---|---|---|
| Cumulative graduates in workforce | 18,000 | 38,000 | 38,000 |
| Average annual earnings gain ($) | 7,800 | 7,800 | 7,800 |
| Total annual earnings gain ($M) | 140.4 | 296.4 | 296.4 |
| GDP multiplier (regional) | 1.4× | 1.4× | 1.4× |
| **Annual GDP contribution ($M)** | **196.6** | **415.0** | **415.0** |
| Cumulative GDP contribution ($M) | 590 | 2,490 | 6,640 |

*Source: gdp_impact_model.csv. Analytics layer: calculated in R/Stata using BEA RIMS II regional multipliers.*

**Table 3.2B: Fiscal Impact — Federal, State, and Local**

| Tax Revenue Stream | Annual at Steady State ($M) | 20-Year PV ($M) |
|---|---|---|
| Federal income tax | 44.5 | 578 |
| Federal payroll tax (FICA) | 22.7 | 295 |
| State income tax (MA/VA/DC blended) | 16.3 | 212 |
| State sales tax (consumption effect) | 8.9 | 116 |
| Local property tax (homeownership effect) | 3.6 | 47 |
| **Total fiscal revenue gain** | **96.0** | **1,248** |
| **Net fiscal position (revenue – cost)** | **+$683M** | |

*Source: fiscal_impact_model.csv. Analytics layer: calculated in R/Stata from IRS SOI, state DOR data, and CBO effective tax rate assumptions.*

## 3.3 Demographic and Dependency Ratio Analysis

**Table 3.3: Old-Age Dependency Ratio Projections (65+ per 100 working-age 20–64)**

| Region | 2024 | 2030 | 2040 | 2050 |
|---|---|---|---|---|
| Massachusetts | 28.4 | 32.1 | 38.7 | 42.3 |
| Washington DC | 22.1 | 25.8 | 31.2 | 34.8 |
| Virginia | 26.8 | 30.5 | 36.4 | 40.1 |
| United States | 28.5 | 32.8 | 38.1 | 41.6 |

*Source: dependency_ratio_projections.csv. Analytics layer: R/Stata from Census Bureau 2023 National Population Projections.*

**Implication:** As dependency ratios rise, programs that activate older adults as productive contributors (mentors) while boosting youth labor force attachment create a **double dividend** — reducing the effective dependency burden from both ends of the age distribution.

## 3.4 Opportunity Cost of Inaction

**Table 3.4: Cumulative Costs of Not Addressing Youth Disconnection**

| Cost Category | Annual per Disconnected Youth ($) | Tri-State Aggregate ($M/yr) |
|---|---|---|
| Foregone earnings | 15,600 | 5,140 |
| Public assistance utilization | 4,800 | 1,582 |
| Criminal justice system costs | 3,200 | 1,054 |
| Healthcare uncompensated care | 2,900 | 956 |
| Lost tax revenue (all levels) | 5,100 | 1,681 |
| **Total annual cost of inaction** | **31,600** | **10,413** |

*Source: cost_of_inaction.csv. Analytics layer: calculated in R/Stata from multiple federal administrative datasets (CPS ASEC, SNAP QC, NCVS, MEPS).*

## 3.5 Macroeconomic Scenario Analysis

**Table 3.5: Program Impact Under Alternative Macro Scenarios**

| Macro Scenario | Assumption | ROI Ratio | SROI Ratio | Breakeven Year |
|---|---|---|---|---|
| **Soft landing** | GDP +2.1%, UE 4.0% | 12.8:1 | 4.8:1 | Year 3 |
| **Base case** | GDP +1.8%, UE 4.5% | 11.4:1 | 4.2:1 | Year 4 |
| **Mild recession (2027)** | GDP -0.5%, UE 6.2% | 8.2:1 | 3.1:1 | Year 5 |
| **Strong growth** | GDP +3.0%, UE 3.2% | 15.1:1 | 5.4:1 | Year 3 |

*Source: macro_scenario_analysis.csv. Analytics layer: R/Stata using VAR model of regional labor market with CBO and FRB projections as exogenous inputs.*

## 3.6 Inflation and Real Wage Effects

**Table 3.6: Real vs. Nominal Wage Gains Under Inflation Scenarios**

| Inflation Scenario | Nominal 3-Year Wage ($/hr) | CPI Assumption | Real 3-Year Wage ($/hr, 2024$) | Real Gain (%) |
|---|---|---|---|---|
| Low inflation (2.0%) | 29.10 | 2.0% | 27.45 | 43.7% |
| Base (2.5%) | 29.10 | 2.5% | 27.05 | 41.6% |
| Elevated (3.5%) | 29.80 | 3.5% | 26.90 | 40.8% |
| Stagflation (4.5%) | 30.20 | 4.5% | 26.45 | 38.5% |

*Source: inflation_scenario_model.csv. Analytics layer: R/Stata. Note: nominal wages partially adjust to inflation with ~0.4 elasticity based on historical BLS data.*
