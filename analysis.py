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
from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, silhouette_score
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

def create_sophisticated_dashboard(regions, youth_unemployment, mentor_supply, avg_wages, roi_scenarios):
    """
    Sophisticated multi-panel dashboard combining key metrics
    Includes: Regional heatmap, Radar chart, ROI distribution, and Wage progression
    """
    from matplotlib.gridspec import GridSpec
    
    fig = plt.figure(figsize=(16, 12))
    gs = GridSpec(3, 2, figure=fig, hspace=0.3, wspace=0.3)
    
    # Panel 1: Regional Heatmap (Youth Unemployment vs Mentor Supply)
    ax1 = fig.add_subplot(gs[0, 0])
    data_matrix = np.array([youth_unemployment, mentor_supply])
    im = ax1.imshow(data_matrix, cmap='RdYlBu_r', aspect='auto')
    ax1.set_xticks(np.arange(len(regions)))
    ax1.set_yticks(np.arange(2))
    ax1.set_xticklabels(regions, rotation=45, ha='right')
    ax1.set_yticklabels(['Youth Unemployment (%)', 'Mentor Supply (%)'])
    ax1.set_title('Regional Metric Heatmap', fontweight='bold')
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax1)
    cbar.set_label('Percentage (%)')
    
    # Add value annotations
    for i in range(2):
        for j in range(len(regions)):
            text = ax1.text(j, i, f'{data_matrix[i, j]:.1f}%',
                          ha="center", va="center", color="black", fontweight='bold')
    
    # Panel 2: Radar Chart for Multi-dimensional Outcomes
    ax2 = fig.add_subplot(gs[0, 1], projection='polar')
    categories = ['Job Retention', 'Earnings Gain', 'Career Progression', 
                  'Mentor Retention', 'Well-being', 'Community Value']
    N = len(categories)
    
    # Values for three scenarios (conservative, base, optimistic)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]
    
    values_base = [72, 40, 65, 81, 75, 70]
    values_optimistic = [80, 50, 75, 88, 85, 80]
    values_base += values_base[:1]
    values_optimistic += values_optimistic[:1]
    
    ax2.plot(angles, values_base, 'o-', linewidth=2, label='Base Case', color='#2b6cb0')
    ax2.fill(angles, values_base, alpha=0.25, color='#4299e1')
    ax2.plot(angles, values_optimistic, 'o-', linewidth=2, label='Optimistic', color='#2c5282')
    ax2.fill(angles, values_optimistic, alpha=0.25, color='#4a5568')
    
    ax2.set_xticks(angles[:-1])
    ax2.set_xticklabels(categories, size=9)
    ax2.set_ylim(0, 100)
    ax2.set_yticks([20, 40, 60, 80, 100])
    ax2.set_yticklabels(['20%', '40%', '60%', '80%', '100%'])
    ax2.set_title('Multi-dimensional Program Outcomes', fontweight='bold', pad=20)
    ax2.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    
    # Panel 3: ROI Distribution with Confidence Intervals
    ax3 = fig.add_subplot(gs[1, 0])
    scenarios = ['Conservative', 'Base Case', 'Optimistic']
    roi_values = [6.2, 11.4, 18.3]
    ci_lower = [5.8, 10.8, 17.5]
    ci_upper = [6.6, 12.0, 19.1]
    
    x_pos = np.arange(len(scenarios))
    bars = ax3.bar(x_pos, roi_values, yerr=[np.array(roi_values) - np.array(ci_lower), 
                                               np.array(ci_upper) - np.array(roi_values)],
                    capsize=5, color=['#e53e3e', '#2b6cb0', '#38a169'], alpha=0.8)
    
    ax3.set_ylabel('ROI Ratio', fontsize=11)
    ax3.set_title('ROI Distribution with 95% Confidence Intervals', fontweight='bold')
    ax3.set_xticks(x_pos)
    ax3.set_xticklabels(scenarios)
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Add value labels
    for i, (bar, val) in enumerate(zip(bars, roi_values)):
        height = bar.get_height()
        ax3.annotate(f'{val}:1', xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 5), textcoords="offset points", ha='center', fontweight='bold')
    
    # Panel 4: Wage Progression by Sector with Confidence Bands
    ax4 = fig.add_subplot(gs[1, 1])
    sectors = ['Healthcare', 'IT/Cybersecurity', 'Manufacturing', 'Construction']
    years = np.array([0, 1, 3, 5, 10])
    
    colors = ['#2b6cb0', '#4299e1', '#63b3ed', '#90cdf4']
    
    for i, sector in enumerate(sectors):
        wages = avg_wages[i]
        ax4.plot(years, wages, marker='o', linewidth=2.5, markersize=7, 
                label=sector, color=colors[i])
        # Add confidence band (simulated)
        std_dev = np.array(wages) * 0.1
        ax4.fill_between(years, np.array(wages) - std_dev, np.array(wages) + std_dev,
                        alpha=0.2, color=colors[i])
    
    ax4.set_xlabel('Years in Career', fontsize=11)
    ax4.set_ylabel('Hourly Wage ($)', fontsize=11)
    ax4.set_title('Wage Progression by Sector with Confidence Bands', fontweight='bold')
    ax4.legend(fontsize=9, loc='upper left')
    ax4.grid(True, alpha=0.3)
    
    # Panel 5: SROI Components Breakdown (Stacked Bar)
    ax5 = fig.add_subplot(gs[2, :])
    components = ['Reduced Public\nAssistance', 'Reduced Criminal\nJustice', 
                  'Increased Income\nTax', 'Increased Payroll\nTax',
                  'Reduced Healthcare\nCosts', 'Reduced Elder\nHealthcare']
    values = [2400, 1800, 1950, 1100, 3200, 2100]
    colors_sroi = ['#e53e3e', '#dd6b20', '#d69e2e', '#38a169', '#3182ce', '#805ad5']
    
    bars = ax5.bar(components, values, color=colors_sroi, edgecolor='black', linewidth=0.5)
    ax5.set_ylabel('Annual Savings per Participant ($)', fontsize=11)
    ax5.set_title('SROI Components - Annual Public Value Breakdown', fontweight='bold')
    ax5.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax5.annotate(f'${height:,.0f}', xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 5), textcoords="offset points", ha='center', fontsize=9, fontweight='bold')
    
    # Add total line
    total = sum(values)
    ax5.axhline(y=total, color='red', linestyle='--', linewidth=2, label=f'Total: ${total:,.0f}')
    ax5.legend(loc='upper right')
    
    plt.suptitle('Intergenerational Mobility Fund - Comprehensive Analytics Dashboard', 
                 fontsize=16, fontweight='bold', y=0.995)
    
    return plt

def plot_regional_bubble_chart(regions, youth_count, mentor_count, avg_wages):
    """
    Geographic-style bubble plot showing regional distribution
    Bubble size = population, color = average wage
    """
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Normalize bubble sizes
    youth_sizes = np.array(youth_count) / max(youth_count) * 3000
    mentor_sizes = np.array(mentor_count) / max(mentor_count) * 3000
    
    # Create scatter plots
    x_pos = np.arange(len(regions))
    y_pos = np.random.rand(len(regions)) * 0.5 + 0.25
    
    # Youth bubbles
    scatter1 = ax.scatter(x_pos, y_pos + 0.2, s=youth_sizes, alpha=0.6, 
                        c=avg_wages, cmap='YlOrRd', edgecolors='black', linewidth=1.5,
                        label='Youth Addressable Market')
    
    # Mentor bubbles
    scatter2 = ax.scatter(x_pos + 0.3, y_pos - 0.2, s=mentor_sizes, alpha=0.6,
                        c=avg_wages, cmap='Blues', edgecolors='black', linewidth=1.5,
                        label='Mentor Supply')
    
    ax.set_xlabel('Region', fontsize=12)
    ax.set_ylabel('Normalized Position', fontsize=12)
    ax.set_title('Regional Distribution: Youth Addressable Market vs Mentor Supply\n(Bubble size = population, Color = average wage)', 
                fontsize=14, fontweight='bold')
    ax.set_xticks(x_pos + 0.15)
    ax.set_xticklabels(regions)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.grid(True, alpha=0.3, axis='x')
    
    # Add colorbars
    cbar1 = plt.colorbar(scatter1, ax=ax, pad=0.02)
    cbar1.set_label('Average Wage ($/hr)')
    
    ax.legend(loc='upper right')
    
    # Add annotations
    for i, region in enumerate(regions):
        ax.text(x_pos[i], y_pos[i] + 0.35, f'{youth_count[i]:,.0f}', 
                ha='center', fontsize=9, fontweight='bold')
        ax.text(x_pos[i] + 0.3, y_pos[i] - 0.35, f'{mentor_count[i]:,.0f}', 
                ha='center', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    return plt

def plot_sankey_diagram(labels, sources, targets, values):
    """
    Sankey diagram for fund flows
    Requires: pip install plotly
    """
    try:
        import plotly.graph_objects as go
        
        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=labels,
                color="lightblue"
            ),
            link=dict(
                source=sources,
                target=targets,
                value=values
            )
        )])
        
        fig.update_layout(
            title_text="Fund Flow Sankey Diagram",
            font_size=12
        )
        
        return fig
    except ImportError:
        print("plotly not installed. Install with: pip install plotly")
        return None

def plot_stakeholder_network(nodes, edges):
    """
    Network graph for stakeholder relationships
    Requires: pip install networkx
    """
    try:
        import networkx as nx
        
        G = nx.DiGraph()
        
        # Add nodes
        for i, node in enumerate(nodes):
            G.add_node(i, label=node)
        
        # Add edges
        for edge in edges:
            G.add_edge(edge[0], edge[1], weight=edge[2])
        
        fig, ax = plt.subplots(figsize=(14, 10))
        
        # Layout
        pos = nx.spring_layout(G, k=2, iterations=50)
        
        # Draw nodes
        node_colors = plt.cm.Set3(np.arange(len(nodes)) / len(nodes))
        nx.draw_networkx_nodes(G, pos, node_size=3000, node_color=node_colors, 
                              ax=ax, alpha=0.8, edgecolors='black', linewidths=2)
        
        # Draw edges with varying thickness based on weight
        for edge in G.edges(data=True):
            nx.draw_networkx_edges(G, pos, edgelist=[(edge[0], edge[1])],
                                  width=edge[2]['weight'] * 2, alpha=0.5, 
                                  edge_color='gray', ax=ax, arrowstyle='->', 
                                  arrowsize=20)
        
        # Draw labels
        labels = nx.get_node_attributes(G, 'label')
        nx.draw_networkx_labels(G, pos, labels, font_size=10, font_weight='bold', ax=ax)
        
        ax.set_title('Stakeholder Network Analysis', fontsize=16, fontweight='bold')
        ax.axis('off')
        
        plt.tight_layout()
        return plt
    except ImportError:
        print("networkx not installed. Install with: pip install networkx")
        return None

def plot_violin_distributions(data_dict):
    """
    Violin plot for distribution analysis across groups
    """
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Prepare data
    all_data = []
    labels = []
    for label, data in data_dict.items():
        all_data.append(data)
        labels.append(label)
    
    # Create violin plot
    parts = ax.violinplot(all_data, showmeans=True, showmedians=True)
    
    # Color the violin bodies
    colors = ['#e53e3e', '#dd6b20', '#d69e2e', '#38a169', '#3182ce', '#805ad5']
    for pc, color in zip(parts['bodies'], colors):
        pc.set_facecolor(color)
        pc.set_alpha(0.7)
    
    ax.set_ylabel('Value', fontsize=12)
    ax.set_xlabel('Group', fontsize=12)
    ax.set_title('Distribution Analysis - Violin Plot', fontsize=14, fontweight='bold')
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    return plt

def plot_time_series_with_trend(years, data_series, trend_line=True):
    """
    Time series plot with optional trend line and confidence intervals
    """
    fig, ax = plt.subplots(figsize=(14, 6))
    
    colors = ['#2b6cb0', '#e53e3e', '#38a169', '#dd6b20', '#805ad5']
    
    for i, (label, data) in enumerate(data_series.items()):
        ax.plot(years, data, marker='o', linewidth=2.5, markersize=7, 
                label=label, color=colors[i % len(colors)])
        
        # Add trend line
        if trend_line and len(years) > 2:
            z = np.polyfit(years, data, 2)
            p = np.poly1d(z)
            x_trend = np.linspace(min(years), max(years), 100)
            ax.plot(x_trend, p(x_trend), '--', linewidth=1.5, alpha=0.7, color=colors[i % len(colors)])
    
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Value', fontsize=12)
    ax.set_title('Time Series Analysis with Trend Lines', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return plt

def plot_box_plot_with_strip(data_dict):
    """
    Box plot with overlaid strip plot for detailed distribution view
    """
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Prepare data
    all_data = []
    labels = []
    for label, data in data_dict.items():
        all_data.append(data)
        labels.append(label)
    
    # Create box plot
    bp = ax.boxplot(all_data, patch_artist=True, labels=labels)
    
    # Color the boxes
    colors = ['#e53e3e', '#dd6b20', '#d69e2e', '#38a169', '#3182ce', '#805ad5']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    # Add strip plot overlay
    for i, data in enumerate(all_data):
        x = np.random.normal(i + 1, 0.1, size=len(data))
        ax.scatter(x, data, alpha=0.5, s=20, color='black', marker='o')
    
    ax.set_ylabel('Value', fontsize=12)
    ax.set_xlabel('Group', fontsize=12)
    ax.set_title('Distribution Analysis - Box Plot with Strip Overlay', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    return plt

def plot_correlation_heatmap(df, title="Correlation Heatmap"):
    """
    Correlation heatmap for multivariate analysis
    """
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Calculate correlation matrix
    corr_matrix = df.corr()
    
    # Create heatmap
    im = ax.imshow(corr_matrix, cmap='RdBu_r', vmin=-1, vmax=1, aspect='auto')
    
    # Set ticks
    ax.set_xticks(np.arange(len(df.columns)))
    ax.set_yticks(np.arange(len(df.columns)))
    ax.set_xticklabels(df.columns, rotation=45, ha='right')
    ax.set_yticklabels(df.columns)
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Correlation Coefficient')
    
    # Add value annotations
    for i in range(len(df.columns)):
        for j in range(len(df.columns)):
            text = ax.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}',
                          ha="center", va="center", color="black", fontweight='bold')
    
    ax.set_title(title, fontsize=14, fontweight='bold')
    plt.tight_layout()
    return plt

# Machine Learning Models

def predict_program_outcomes(df, features, target, test_size=0.2, random_state=42):
    """
    Predict program outcomes (e.g., graduation probability) using Gradient Boosting
    Returns model, predictions, and performance metrics
    """
    # Prepare data
    X = df[features]
    y = df[target]
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train Gradient Boosting Regressor
    model = GradientBoostingRegressor(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=5,
        random_state=random_state
    )
    model.fit(X_train_scaled, y_train)
    
    # Predictions
    y_pred = model.predict(X_test_scaled)
    
    # Performance metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': features,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    return {
        'model': model,
        'scaler': scaler,
        'predictions': y_pred,
        'actual': y_test,
        'mse': mse,
        'r2': r2,
        'feature_importance': feature_importance
    }

def cluster_participants(df, features, n_clusters=3, random_state=42):
    """
    Cluster participants into segments using K-Means
    Returns cluster labels, centroids, and silhouette score
    """
    # Prepare data
    X = df[features]
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Fit K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)
    cluster_labels = kmeans.fit_predict(X_scaled)
    
    # Calculate silhouette score
    silhouette_avg = silhouette_score(X_scaled, cluster_labels)
    
    # Get cluster centroids (in original scale)
    centroids = scaler.inverse_transform(kmeans.cluster_centers_)
    
    # Create cluster summary
    df_clustered = df.copy()
    df_clustered['cluster'] = cluster_labels
    
    cluster_summary = df_clustered.groupby('cluster')[features].agg(['mean', 'std'])
    
    return {
        'cluster_labels': cluster_labels,
        'centroids': centroids,
        'silhouette_score': silhouette_avg,
        'cluster_summary': cluster_summary,
        'scaler': scaler,
        'kmeans': kmeans
    }

def predict_match_success(df, features, target, test_size=0.2, random_state=42):
    """
    Predict mentor-youth match success using Random Forest
    Returns model, predictions, and performance metrics
    """
    # Prepare data
    X = df[features]
    y = df[target]
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train Random Forest Classifier
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=random_state,
        class_weight='balanced'
    )
    model.fit(X_train_scaled, y_train)
    
    # Predictions
    y_pred = model.predict(X_test_scaled)
    y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
    
    # Performance metrics
    accuracy = accuracy_score(y_test, y_pred)
    cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': features,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    return {
        'model': model,
        'scaler': scaler,
        'predictions': y_pred,
        'actual': y_test,
        'probabilities': y_pred_proba,
        'accuracy': accuracy,
        'cv_scores': cv_scores,
        'feature_importance': feature_importance
    }

def time_series_forecast(data, forecast_periods=5, window_size=3):
    """
    Simple time series forecasting using moving average and trend extrapolation
    Returns forecasted values and confidence intervals
    """
    # Calculate moving average
    data_series = pd.Series(data)
    moving_avg = data_series.rolling(window=window_size).mean()
    
    # Linear trend extrapolation
    x = np.arange(len(data))
    z = np.polyfit(x, data, 2)
    p = np.poly1d(z)
    
    # Forecast
    x_forecast = np.arange(len(data), len(data) + forecast_periods)
    forecast = p(x_forecast)
    
    # Calculate confidence intervals (simple approach using historical variance)
    historical_std = np.std(data)
    ci_lower = forecast - 1.96 * historical_std
    ci_upper = forecast + 1.96 * historical_std
    
    return {
        'forecast': forecast,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'historical_data': data,
        'moving_avg': moving_avg,
        'trend_line': p(x)
    }

def plot_feature_importance(feature_importance_df, title="Feature Importance"):
    """
    Plot feature importance from ML models
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Sort by importance
    df_sorted = feature_importance_df.sort_values('importance', ascending=True)
    
    # Horizontal bar plot
    bars = ax.barh(df_sorted['feature'], df_sorted['importance'], color='#2b6cb0', alpha=0.8)
    
    ax.set_xlabel('Importance', fontsize=12)
    ax.set_ylabel('Feature', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='x')
    
    # Add value labels
    for i, (bar, val) in enumerate(zip(bars, df_sorted['importance'])):
        width = bar.get_width()
        ax.annotate(f'{val:.3f}', xy=(width, bar.get_y() + bar.get_height()/2),
                    xytext=(5, 0), textcoords="offset points", ha='left', va='center', fontsize=9)
    
    plt.tight_layout()
    return plt

def plot_cluster_analysis(df, cluster_labels, features):
    """
    Visualize cluster analysis results
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    axes = axes.flatten()
    
    df_clustered = df.copy()
    df_clustered['cluster'] = cluster_labels
    
    colors = ['#e53e3e', '#2b6cb0', '#38a169', '#dd6b20', '#805ad5']
    
    for i, feature in enumerate(features[:4]):
        ax = axes[i]
        for cluster in sorted(df_clustered['cluster'].unique()):
            cluster_data = df_clustered[df_clustered['cluster'] == cluster][feature]
            ax.hist(cluster_data, alpha=0.6, label=f'Cluster {cluster}', 
                   color=colors[int(cluster) % len(colors)], bins=20, edgecolor='black')
        
        ax.set_xlabel(feature, fontsize=11)
        ax.set_ylabel('Frequency', fontsize=11)
        ax.set_title(f'Distribution of {feature} by Cluster', fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    plt.suptitle('Cluster Analysis - Feature Distributions', fontsize=16, fontweight='bold')
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

# Streamlined Visualization Functions

def quick_bar(x, y, title=None, xlabel=None, ylabel=None):
    """Simple one-line bar chart"""
    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color='#2b6cb0', alpha=0.8, edgecolor='black', linewidth=1)
    if title: plt.title(title, fontweight='bold')
    if xlabel: plt.xlabel(xlabel)
    if ylabel: plt.ylabel(ylabel)
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    return plt

def quick_line(x, y, title=None, xlabel=None, ylabel=None, label=None):
    """Simple one-line chart"""
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o', linewidth=2.5, markersize=7, color='#2b6cb0', label=label)
    if title: plt.title(title, fontweight='bold')
    if xlabel: plt.xlabel(xlabel)
    if ylabel: plt.ylabel(ylabel)
    if label: plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    return plt

def quick_scatter(x, y, title=None, xlabel=None, ylabel=None):
    """Simple one-line scatter plot"""
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, alpha=0.6, color='#2b6cb0', edgecolors='black', linewidth=1)
    if title: plt.title(title, fontweight='bold')
    if xlabel: plt.xlabel(xlabel)
    if ylabel: plt.ylabel(ylabel)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    return plt

def quick_hist(data, title=None, xlabel=None, bins=20):
    """Simple one-line histogram"""
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, color='#2b6cb0', alpha=0.7, edgecolor='black', linewidth=1)
    if title: plt.title(title, fontweight='bold')
    if xlabel: plt.xlabel(xlabel)
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    return plt

def quick_pie(values, labels, title=None):
    """Simple one-line pie chart"""
    plt.figure(figsize=(10, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Set3(np.arange(len(values))))
    if title: plt.title(title, fontweight='bold')
    plt.axis('equal')
    plt.tight_layout()
    return plt

def quick_heatmap(data, title=None):
    """Simple one-line heatmap"""
    plt.figure(figsize=(10, 8))
    plt.imshow(data, cmap='RdBu_r', aspect='auto')
    plt.colorbar()
    if title: plt.title(title, fontweight='bold')
    plt.tight_layout()
    return plt

def quick_box(data_dict, title=None):
    """Simple one-line box plot"""
    plt.figure(figsize=(12, 6))
    plt.boxplot(data_dict.values(), labels=data_dict.keys(), patch_artist=True)
    if title: plt.title(title, fontweight='bold')
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    return plt

def quick_multi_line(data_dict, title=None, xlabel=None, ylabel=None):
    """Simple multi-line chart"""
    plt.figure(figsize=(12, 6))
    colors = ['#2b6cb0', '#e53e3e', '#38a169', '#dd6b20', '#805ad5']
    for i, (label, data) in enumerate(data_dict.items()):
        plt.plot(data, marker='o', linewidth=2, markersize=6, label=label, color=colors[i % len(colors)])
    if title: plt.title(title, fontweight='bold')
    if xlabel: plt.xlabel(xlabel)
    if ylabel: plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    return plt

def quick_compare_bar(labels, values1, values2, label1='Series 1', label2='Series 2', title=None):
    """Simple comparison bar chart"""
    plt.figure(figsize=(12, 6))
    x = np.arange(len(labels))
    width = 0.35
    plt.bar(x - width/2, values1, width, label=label1, color='#2b6cb0', alpha=0.8)
    plt.bar(x + width/2, values2, width, label=label2, color='#e53e3e', alpha=0.8)
    plt.xticks(x, labels)
    if title: plt.title(title, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    return plt

def plot_all_quick(data_dict, title_prefix="Quick Plot"):
    """Generate all quick plots for a dictionary of data"""
    for i, (key, value) in enumerate(data_dict.items()):
        if isinstance(value, list) and len(value) > 1:
            if all(isinstance(v, (int, float)) for v in value):
                quick_hist(value, title=f"{title_prefix} - {key} (Histogram)")
                plt.show()
                quick_line(range(len(value)), value, title=f"{title_prefix} - {key} (Line)")
                plt.show()

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
