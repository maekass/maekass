# Part I: Granular Market Analysis

*See `00_executive_summary.md` for the full investment thesis, fund structure, and narrative overview.*

### 1.1 Youth Addressable Market — Sub-Regional Detail

**Table 1.1A: Youth Addressable Market by Metro Area**

| Metro Area | Population 16–30 | Underemployed (%) | Disconnected (%) | Addressable Market |
|---|---|---|---|---|
| Boston-Cambridge-Newton, MA | 742,000 | 14.2% | 5.8% | 148,400 |
| Worcester, MA | 218,000 | 18.1% | 8.3% | 57,600 |
| Springfield, MA | 185,000 | 20.7% | 10.1% | 57,000 |
| Other MA | 702,000 | 15.8% | 7.9% | 40,100 |
| Washington-Arlington-Alexandria, DC-VA | 512,000 | 18.3% | 9.2% | 140,800 |
| DC Wards 7 & 8 (focus) | 78,000 | 28.4% | 16.5% | 35,000 |
| Other DC Metro | 166,000 | 16.1% | 7.8% | 55,700 |
| Northern Virginia | 620,000 | 14.8% | 7.1% | 135,800 |
| Richmond, VA | 348,000 | 19.2% | 10.3% | 102,700 |
| Hampton Roads, VA | 386,000 | 18.7% | 11.2% | 30,500 |
| Other VA | 300,000 | 17.9% | 9.8% | 20,600 |
| **Total** | **4,257,000** | | | **824,200** |

*Source: youth_underemployment_by_metro.csv. Analytics layer: table prepared in R/Stata from Census ACS 5-year estimates and BLS LAUS data, 2023–2024.*

**Table 1.1B: Youth Addressable Market by Race/Ethnicity**

| Race/Ethnicity | MA | DC | VA | Total | % of Addressable |
|---|---|---|---|---|---|
| Black/African American | 48,500 | 138,900 | 72,400 | 259,800 | 31.5% |
| Hispanic/Latino | 72,700 | 32,400 | 52,100 | 157,200 | 19.1% |
| White | 127,300 | 34,700 | 121,600 | 283,600 | 34.4% |
| Asian | 30,300 | 10,400 | 28,900 | 69,600 | 8.4% |
| Other/Multiracial | 24,300 | 15,100 | 14,600 | 54,000 | 6.6% |

*Source: youth_demographics_by_race.csv. Analytics layer: R/Stata from Census ACS microdata.*

**Table 1.1C: Youth Addressable Market by Educational Attainment**

| Educational Attainment | Count | % |
|---|---|---|
| Less than HS diploma | 197,800 | 24.0% |
| HS diploma or equivalent | 296,700 | 36.0% |
| Some college, no degree | 214,300 | 26.0% |
| Associate degree | 74,200 | 9.0% |
| Bachelor's degree (underemployed) | 41,200 | 5.0% |

*Source: youth_education_attainment.csv. Analytics layer: R/Stata from Census ACS.*

### 1.2 Older Adult Mentor Supply — Sub-Regional Detail

**Table 1.2A: Mentor Supply by Metro Area**

| Metro Area | Population 65+ | Seek Mentor Role (%) | Currently Serving (%) | Unmet Gap (%) | Addressable Mentors |
|---|---|---|---|---|---|
| Boston-Cambridge-Newton, MA | 512,000 | 44.1% | 20.3% | 23.8% | 121,900 |
| Worcester, MA | 158,000 | 40.2% | 16.1% | 24.1% | 38,100 |
| Springfield, MA | 142,000 | 38.7% | 14.8% | 23.9% | 33,900 |
| Other MA | 473,000 | 42.5% | 17.9% | 24.6% | 113,200 |
| Washington-Arlington-Alexandria, DC-VA | 198,000 | 40.1% | 18.2% | 21.9% | 43,400 |
| DC Wards (focus) | 98,000 | 35.2% | 12.4% | 22.8% | 22,300 |
| Other DC Metro | 216,000 | 38.9% | 16.8% | 22.1% | 48,000 |
| Northern Virginia | 298,000 | 46.1% | 21.5% | 24.6% | 73,300 |
| Richmond, VA | 312,000 | 43.2% | 18.7% | 24.5% | 76,400 |
| Hampton Roads, VA | 358,000 | 42.8% | 19.1% | 23.7% | 84,800 |
| Other VA | 230,000 | 45.1% | 20.4% | 24.7% | 59,000 |
| **Total** | **2,995,000** | | | | **714,300** |

*Source: older_adult_isolation_by_metro.csv. Analytics layer: R/Stata from regional aging surveys and Census ACS.*

**Table 1.2B: Mentor Supply by Professional Background**

| Prior Career Field | Count | % |
|---|---|---|
| Education / Training | 157,100 | 22.0% |
| Business / Management | 135,700 | 19.0% |
| Healthcare / Social Services | 107,100 | 15.0% |
| Skilled Trades / Manufacturing | 85,700 | 12.0% |
| Government / Public Administration | 78,600 | 11.0% |
| Technology / Engineering | 64,300 | 9.0% |
| Other Professional | 85,700 | 12.0% |

*Source: mentor_professional_background.csv. Analytics layer: R/Stata from aging survey microdata.*

### 1.3 Sector-Specific Training Pathways — Granular Detail

**Table 1.3: Target Sectors with Wage Progression and Labor Demand**

| Sector | Entry Wage ($/hr) | 3-Year Wage ($/hr) | 5-Year Wage ($/hr) | Projected 10-Year Job Growth (%) | Annual Openings (Tri-State) |
|---|---|---|---|---|---|
| Healthcare Support | 18.50 | 24.80 | 31.20 | 15.2% | 28,400 |
| IT / Cybersecurity | 22.00 | 35.50 | 48.00 | 18.7% | 19,800 |
| Advanced Manufacturing | 19.00 | 27.50 | 34.00 | 8.3% | 14,200 |
| Clean Energy / HVAC | 20.00 | 29.00 | 37.50 | 22.1% | 11,600 |
| Construction Trades | 21.00 | 30.50 | 38.00 | 7.8% | 22,100 |
| Logistics / Supply Chain | 17.50 | 23.00 | 28.50 | 10.4% | 16,900 |
| Financial Services / Fintech | 21.50 | 32.00 | 42.00 | 9.6% | 12,300 |
| Early Childhood Education | 16.00 | 21.00 | 26.50 | 6.2% | 8,700 |
| Hospitality Management | 15.50 | 22.00 | 29.00 | 11.3% | 24,500 |
| **Weighted Average** | **19.10** | **27.40** | **35.10** | **12.2%** | **158,500** |

*Source: sector_wage_progression_detailed.csv. Analytics layer: visualized in Power BI/Tableau; wage-growth model inputs estimated in R/Stata from BLS OEWS and state LMI projections.*
