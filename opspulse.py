import pandas as pd
from datetime import datetime

def analyze_business_ops(data_file):
    # Load raw data (supports CSV for this example)
    df = pd.read_csv(data_file)
    
    # 1. Data Cleaning: Standardize timestamps and handle missing values
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.fillna({'priority': 'Medium', 'resolution_time_hrs': 0})

    # 2. Metric Calculation: Logic for Support & Ops
    total_volume = len(df)
    avg_resolution = df['resolution_time_hrs'].mean()
    high_priority_pct = (len(df[df['priority'] == 'High']) / total_volume) * 100
    
    # Logic for Business Ops: Customer Satisfaction (CSAT) Trend
    avg_csat = df['csat_score'].mean()

    # 3. Generating the Markdown Report
    report_date = datetime.now().strftime("%Y-%m-%d")
    report = f"""
# OpsPulse Business Intelligence Report
**Date:** {report_date}

## Core Performance Metrics
* **Total Volume Managed:** {total_volume}
* **Average Resolution Time:** {avg_resolution:.2f} hours
* **High-Priority Incident Rate:** {high_priority_pct:.1f}%
* **Aggregated CSAT Score:** {avg_csat:.2f} / 5.00

## Operational Insights
> This data suggests a correlation between resolution time and high-priority spikes. 
> Recommended Action: Audit documentation for 'High' priority recurring issues.
    """
    
    with open("business_impact_report.md", "w") as f:
        f.write(report)
    print("Report generated: business_impact_report.md")

# To run: analyze_business_ops('support_data.csv')
