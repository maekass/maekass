"""
Intergenerational Mobility Fund - Data Analysis Scripts
Python equivalents for R/Stata analysis
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

def load_data(filepath):
    """Load CSV data"""
    return pd.read_csv(filepath)

def descriptive_statistics(df, group_by=None):
    """
    Generate descriptive statistics
    Equivalent to R/Stata summary()
    """
    if group_by:
        return df.groupby(group_by).describe()
    return df.describe()

def calculate_addressable_market(df, population_col, underemployed_col, disconnected_col):
    """
    Calculate addressable market
    Input: DataFrame with population, underemployment %, disconnection %
    """
    df['addressable_market'] = df[population_col] * (
        df[underemployed_col] + df[disconnected_col]
    )
    return df

def wage_regression(df, log_wage_col, predictors):
    """
    Log-linear wage regression
    Equivalent to R: lm(log(wage) ~ predictors)
    """
    X = df[predictors]
    X = sm.add_constant(X)
    y = df[log_wage_col]
    
    model = sm.OLS(y, X).fit()
    return model

def logistic_regression_match_retention(df, predictors, outcome):
    """
    Logistic regression for match retention
    Equivalent to R: glm(match_retention ~ predictors, family=binomial)
    """
    X = df[predictors]
    y = df[outcome]
    
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    
    # Calculate odds ratios and confidence intervals
    coef = model.coef_[0]
    odds_ratios = np.exp(coef)
    
    # Add intercept
    intercept_odds = np.exp(model.intercept_[0])
    
    return model, odds_ratios, intercept_odds

def roi_calculator(annual_earnings_gain, working_years, discount_rate, program_cost):
    """
    Calculate ROI metrics
    Equivalent to R/Stata NPV calculations
    """
    years = np.arange(1, working_years + 1)
    discount_factors = 1 / (1 + discount_rate) ** years
    pv_earnings = annual_earnings_gain * discount_factors.sum()
    npv = pv_earnings - program_cost
    roi_ratio = pv_earnings / program_cost
    
    return {
        'pv_lifetime_gain': pv_earnings,
        'npv': npv,
        'roi_ratio': roi_ratio
    }

def sensitivity_analysis(base_cost, base_earnings, cost_variations, earnings_variations):
    """
    Two-way sensitivity analysis for ROI
    Equivalent to R/Stata Monte Carlo simulation
    """
    results = pd.DataFrame(index=cost_variations, columns=earnings_variations)
    
    for cost_var in cost_variations:
        for earnings_var in earnings_variations:
            adjusted_cost = base_cost * (1 + cost_var)
            adjusted_earnings = base_earnings * (1 + earnings_var)
            roi = roi_calculator(adjusted_earnings, 35, 0.03, adjusted_cost)['roi_ratio']
            results.loc[cost_var, earnings_var] = roi
    
    return results

def monte_carlo_simulation(base_cost, base_earnings, n_simulations=10000):
    """
    Monte Carlo simulation for ROI uncertainty analysis
    """
    # Assume triangular distributions
    cost_samples = np.random.triangular(
        base_cost * 0.8, base_cost, base_cost * 1.2, n_simulations
    )
    earnings_samples = np.random.triangular(
        base_earnings * 0.8, base_earnings, base_earnings * 1.2, n_simulations
    )
    
    roi_samples = []
    for cost, earnings in zip(cost_samples, earnings_samples):
        roi = roi_calculator(earnings, 35, 0.03, cost)['roi_ratio']
        roi_samples.append(roi)
    
    roi_samples = np.array(roi_samples)
    
    return {
        'mean': np.mean(roi_samples),
        'median': np.median(roi_samples),
        'std': np.std(roi_samples),
        'percentile_10': np.percentile(roi_samples, 10),
        'percentile_90': np.percentile(roi_samples, 90),
        'samples': roi_samples
    }

def effect_size_meta_analysis(studies):
    """
    Meta-analysis of effect sizes
    Equivalent to R metafor package
    Input: DataFrame with study_name, effect_size, se, n
    """
    # Fixed-effects meta-analysis
    weights = 1 / (studies['se'] ** 2)
    weighted_effect = np.sum(studies['effect_size'] * weights) / np.sum(weights)
    se_pooled = np.sqrt(1 / np.sum(weights))
    
    # Calculate confidence intervals
    ci_lower = weighted_effect - 1.96 * se_pooled
    ci_upper = weighted_effect + 1.96 * se_pooled
    
    return {
        'pooled_effect': weighted_effect,
        'se': se_pooled,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'weights': weights
    }

def equity_analysis(df, subgroup_col, outcome_cols):
    """
    Analyze outcomes by subgroup
    Equivalent to R/Stata subgroup analysis
    """
    results = df.groupby(subgroup_col)[outcome_cols].agg(['mean', 'std', 'count'])
    return results

def gdp_impact_model(graduates, avg_earnings_gain, multiplier):
    """
    Calculate GDP impact using regional multipliers
    Equivalent to R/Stata GDP impact calculations
    """
    total_earnings_gain = graduates * avg_earnings_gain
    gdp_contribution = total_earnings_gain * multiplier
    return gdp_contribution

def fiscal_impact_model(earnings_gain, tax_rates):
    """
    Calculate fiscal impact by tax type
    Input: tax_rates dict with federal_income, payroll, state_income, sales, property
    """
    fiscal_revenue = {}
    for tax_type, rate in tax_rates.items():
        fiscal_revenue[tax_type] = earnings_gain * rate
    
    return fiscal_revenue

def plot_wage_progression(df, sectors, year_cols):
    """
    Plot wage progression by sector
    Equivalent to R ggplot2 visualization
    """
    plt.figure(figsize=(12, 6))
    
    for sector in sectors:
        sector_data = df[df['sector'] == sector]
        plt.plot(year_cols, sector_data['wage'], marker='o', label=sector)
    
    plt.xlabel('Year')
    plt.ylabel('Hourly Wage ($)')
    plt.title('Wage Progression by Sector')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    return plt

def plot_roi_distribution(mc_results):
    """
    Plot Monte Carlo ROI distribution
    """
    plt.figure(figsize=(10, 6))
    plt.hist(mc_results['samples'], bins=50, edgecolor='black', alpha=0.7)
    plt.axvline(mc_results['mean'], color='red', linestyle='--', label=f'Mean: {mc_results["mean"]:.2f}')
    plt.axvline(mc_results['median'], color='blue', linestyle='--', label=f'Median: {mc_results["median"]:.2f}')
    plt.xlabel('ROI Ratio')
    plt.ylabel('Frequency')
    plt.title('Monte Carlo ROI Distribution')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    return plt

def plot_mentor_supply_demand(regions, seeking_pct, serving_pct):
    """
    Figure 2: Older Adults (65+) - Mentor Role Seeking vs. Current Engagement
    Bar chart comparing those seeking mentor roles vs. currently serving
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    x = np.arange(len(regions))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, seeking_pct, width, label='Seeking Mentor Role', color='#2c5282')
    bars2 = ax.bar(x + width/2, serving_pct, width, label='Currently Serving', color='#4299e1')
    
    ax.set_xlabel('Region', fontsize=12)
    ax.set_ylabel('Percentage (%)', fontsize=12)
    ax.set_title('Figure 2: Older Adults (65+) - Mentor Role Seeking vs. Current Engagement', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(regions)
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for bar in bars1:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}%', xy=(bar.get_x() + bar.get_width()/2, height), 
                    xytext=(0, 3), textcoords="offset points", ha='center', fontsize=9)
    for bar in bars2:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}%', xy=(bar.get_x() + bar.get_width()/2, height), 
                    xytext=(0, 3), textcoords="offset points", ha='center', fontsize=9)
    
    plt.tight_layout()
    return plt

def plot_mentor_dosage_response(duration_months, graduation_prob):
    """
    Figure 5: Mentor Match Duration and Graduation Probability
    Line/area chart showing relationship between mentor match duration and graduation probability
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot the dosage-response curve
    ax.plot(duration_months, graduation_prob, marker='o', linewidth=3, markersize=8, 
            color='#2b6cb0', label='Graduation Probability')
    
    # Add shaded area under curve
    ax.fill_between(duration_months, graduation_prob, alpha=0.3, color='#4299e1')
    
    ax.set_xlabel('Mentor Match Duration (months)', fontsize=12)
    ax.set_ylabel('Graduation Probability (%)', fontsize=12)
    ax.set_title('Figure 5: Mentor Match Duration and Graduation Probability', fontsize=14, fontweight='bold')
    ax.set_ylim(0, 100)
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    # Add annotations for key points
    for i, (x, y) in enumerate(zip(duration_months, graduation_prob)):
        ax.annotate(f'{y:.0f}%', xy=(x, y), xytext=(0, 10), textcoords="offset points", 
                    ha='center', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    return plt

def generate_report_tables(df_dict, output_dir='tables'):
    """
    Generate all analysis tables for report
    """
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    for name, df in df_dict.items():
        df.to_csv(f'{output_dir}/{name}.csv', index=False)
        df.to_latex(f'{output_dir}/{name}.tex', index=False)
        df.to_html(f'{output_dir}/{name}.html', index=False)

# Example usage
if __name__ == "__main__":
    print("Intergenerational Mobility Fund - Python Analysis Scripts")
    print("=" * 60)
    
    # Example ROI calculation
    roi_result = roi_calculator(7800, 35, 0.03, 14850)
    print(f"\nROI Calculation:")
    print(f"  PV Lifetime Gain: ${roi_result['pv_lifetime_gain']:,.2f}")
    print(f"  NPV: ${roi_result['npv']:,.2f}")
    print(f"  ROI Ratio: {roi_result['roi_ratio']:.2f}:1")
    
    # Example sensitivity analysis
    cost_vars = [-0.20, 0, 0.20]
    earnings_vars = [-0.20, 0, 0.20]
    sens_results = sensitivity_analysis(14850, 7800, cost_vars, earnings_vars)
    print(f"\nSensitivity Analysis (ROI Ratios):")
    print(sens_results)
    
    # Example Monte Carlo simulation
    mc_results = monte_carlo_simulation(14850, 7800, n_simulations=1000)
    print(f"\nMonte Carlo Simulation (n=1000):")
    print(f"  Mean ROI: {mc_results['mean']:.2f}:1")
    print(f"  Median ROI: {mc_results['median']:.2f}:1")
    print(f"  Std Dev: {mc_results['std']:.2f}")
    print(f"  10th Percentile: {mc_results['percentile_10']:.2f}:1")
    print(f"  90th Percentile: {mc_results['percentile_90']:.2f}:1")
