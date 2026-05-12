# Part II: Financial Models

## 2.1 Unit-Cost Model — Per Participant

**Table 2.1: Per-Participant Annual Cost Breakdown**

| Cost Category | Per Participant ($) | % of Total |
|---|---|---|
| **Direct Program Costs** | | |
| Sector training tuition / materials | 4,200 | 28.0% |
| Mentor stipend ($200/mo × 10 months) | 2,000 | 13.3% |
| Case management / coaching (1:40 ratio) | 2,500 | 16.7% |
| Transportation subsidy | 900 | 6.0% |
| Technology / device access | 600 | 4.0% |
| **Indirect / Overhead** | | |
| Program administration (15% of direct) | 1,530 | 10.2% |
| M&E / data infrastructure | 750 | 5.0% |
| Mentor recruitment & training | 500 | 3.3% |
| Employer partnership development | 520 | 3.5% |
| **Contingency (10%)** | 1,350 | 9.0% |
| **Total Per Participant** | **14,850** | **100%** |

*Source: unit_cost_model.csv. Analytics layer: calculated in R/Stata from comparable program benchmarks (Year Up, Per Scholas, iMentor, Experience Corps).*

## 2.2 Scale-Up Cost Projections

**Table 2.2: Multi-Year Scale-Up Budget ($M)**

| Year | Cohort Size | Direct Costs | Indirect Costs | Total | Cumulative |
|---|---|---|---|---|---|
| Year 1 (Pilot) | 500 | 5.25 | 2.18 | 7.43 | 7.43 |
| Year 2 | 1,500 | 15.75 | 6.53 | 22.28 | 29.71 |
| Year 3 | 3,000 | 31.50 | 13.05 | 44.55 | 74.26 |
| Year 4 | 5,000 | 52.50 | 21.75 | 74.25 | 148.51 |
| Year 5 | 8,000 | 84.00 | 34.80 | 118.80 | 267.31 |
| Year 6 | 10,000 | 105.00 | 43.50 | 148.50 | 415.81 |
| Year 7 | 10,000 | 105.00 | 43.50 | 148.50 | 564.31 |
| **Total (7 years)** | **38,000** | **399.00** | **165.31** | **564.31** | |

*Source: scale_up_budget.csv. Analytics layer: calculated in R/Stata. Assumes 10% efficiency gain from Year 4 onward via economies of scale.*

## 2.3 Return on Investment (ROI) Model

**Table 2.3A: Lifetime Earnings Gain per Participant**

| Scenario | Annual Earnings Gain ($) | Working Years | Discount Rate | PV Lifetime Gain ($) |
|---|---|---|---|---|
| Conservative (10th pctile) | 4,200 | 35 | 3.0% | 91,400 |
| Base Case (median) | 7,800 | 35 | 3.0% | 169,700 |
| Optimistic (90th pctile) | 12,500 | 35 | 3.0% | 272,000 |

*Source: lifetime_earnings_model.csv. Analytics layer: estimated in R/Stata using log-linear wage model with mentoring effect sizes from Table A3.*

**Table 2.3B: Aggregate ROI — 7-Year Cohort**

| Metric | Conservative | Base Case | Optimistic |
|---|---|---|---|
| Total participants (7 years) | 38,000 | 38,000 | 38,000 |
| Total program cost ($M) | 564.3 | 564.3 | 564.3 |
| PV lifetime earnings gain ($M) | 3,473 | 6,449 | 10,336 |
| Net present value ($M) | 2,909 | 5,884 | 9,772 |
| **ROI ratio** | **6.2:1** | **11.4:1** | **18.3:1** |
| Breakeven year | Year 6 | Year 4 | Year 3 |

*Source: aggregate_roi_model.csv. Analytics layer: calculated in R/Stata.*

## 2.4 Social Return on Investment (SROI)

**Table 2.4A: SROI Components — Public Sector Savings per Participant**

| Outcome | Annual Savings ($) | Source |
|---|---|---|
| Reduced public assistance (SNAP/TANF) | 2,400 | USDA/FNS, HHS ASPE |
| Reduced criminal justice involvement | 1,800 | DOJ, Vera Institute |
| Increased income tax revenue | 1,950 | IRS SOI, state tax schedules |
| Increased payroll tax revenue | 1,100 | SSA actuarial studies |
| Reduced healthcare costs (uninsured → insured) | 3,200 | Kaiser Family Foundation |
| Reduced elder healthcare costs (social engagement) | 2,100 | NIA, AARP studies |
| **Total annual public value per pair** | **12,550** | |

*Source: sroi_components.csv. Analytics layer: calculated in R/Stata from federal and state administrative data benchmarks.*

**Table 2.4B: Aggregate SROI — 7-Year Horizon**

| Metric | Value |
|---|---|
| Total public savings over 10 years ($M) | 2,385 |
| Total program cost ($M) | 564.3 |
| **SROI ratio** | **4.2:1** |
| Net public benefit ($M) | 1,821 |

*Source: aggregate_sroi_model.csv. Analytics layer: calculated in R/Stata.*

## 2.5 Pay-for-Success (PFS) / Outcomes-Based Financing Structure

**Table 2.5: Proposed PFS Structure**

| Element | Detail |
|---|---|
| **Outcome metric 1** | 12-month job retention ≥ 70% |
| **Outcome metric 2** | Earnings ≥ 150% of pre-program baseline at 24 months |
| **Outcome metric 3** | Mentor retention ≥ 80% at 12 months |
| **Outcome payer** | State workforce boards + philanthropic guarantors |
| **Upfront capital** | Social impact bonds / outcomes rate cards |
| **Evaluation design** | Quasi-experimental (propensity-score matched comparison group) |
| **Independent evaluator** | Urban Institute or MDRC |
| **Success payment cap** | 110% of per-participant cost ($16,335) |
| **Repayment trigger** | ≥ 2 of 3 outcome metrics met at p < 0.05 |

*Source: pfs_structure.csv. Analytics layer: R/Stata for power calculations and outcome threshold modeling.*

## 2.6 Blended Capital Stack

**Table 2.6: Proposed Funding Mix by Source**

| Capital Source | Amount ($M) | % of Total | Type | Terms |
|---|---|---|---|---|
| Philanthropic grants (pilot) | 30.0 | 5.3% | Grant | Unrestricted |
| Social impact bonds | 150.0 | 26.6% | Debt | 3–5% coupon, outcome-contingent |
| WIOA Title I funds | 120.0 | 21.3% | Federal pass-through | Formula + discretionary |
| State workforce appropriations | 100.0 | 17.7% | State appropriation | Annual renewal |
| SNAP E&T / TANF | 45.0 | 8.0% | Federal entitlement | Reimbursement-based |
| Corporate / employer co-investment | 60.0 | 10.6% | Direct contribution | Tax-credit eligible |
| Community Reinvestment Act (CRA) | 35.0 | 6.2% | Bank investment | CRA-qualified |
| Medicaid 1115 waiver (elder component) | 24.3 | 4.3% | Federal waiver | HCBS-adjacent |
| **Total** | **564.3** | **100%** | | |

*Source: blended_capital_stack.csv. Analytics layer: calculated in R/Stata from federal register, state budget documents, and CDFI fund data.*

## 2.7 Sensitivity Analysis — Key Financial Levers

**Table 2.7: Two-Way Sensitivity: ROI Ratio by Program Cost and Earnings Gain**

|  | Earnings Gain: -20% | Earnings Gain: Base | Earnings Gain: +20% |
|---|---|---|---|
| **Cost: -20%** | 9.7:1 | 14.3:1 | 22.9:1 |
| **Cost: Base** | 7.8:1 | 11.4:1 | 18.3:1 |
| **Cost: +20%** | 6.5:1 | 9.5:1 | 15.3:1 |

*Source: sensitivity_analysis.csv. Analytics layer: calculated in R/Stata using Monte Carlo simulation (n=10,000 draws from triangular distributions).*

## 2.8 Intergenerational Wealth Transfer Model

**Table 2.8: Estimated Intergenerational Wealth Effects**

| Channel | Annual per Pair ($) | Aggregate 20-Year ($M) |
|---|---|---|
| Youth earnings gain (direct) | 7,800 | 2,964 |
| Youth asset building (401k/homeownership) | 1,200 | 456 |
| Elder delayed care costs (social engagement) | 2,100 | 798 |
| Elder volunteer-to-paid transition value | 800 | 304 |
| Reduced youth debt / credit improvement | 600 | 228 |
| **Total intergenerational wealth effect** | **12,500** | **4,750** |

*Source: wealth_transfer_model.csv. Analytics layer: calculated in R/Stata from PSID and HRS longitudinal data.*
