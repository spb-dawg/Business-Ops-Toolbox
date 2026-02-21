-- 1. CUSTOMER CHURN RISK ANALYSIS
-- Goal: Identify users who have high support ticket volume but low platform activity.
-- Vital for: Customer Support Managers & BizOps.

WITH SupportVolume AS (
    SELECT 
        user_id, 
        COUNT(ticket_id) as total_tickets,
        AVG(csat_score) as avg_satisfaction
    FROM support_tickets
    WHERE created_at > CURRENT_DATE - INTERVAL '30 days'
    GROUP BY 1
),
PlatformActivity AS (
    SELECT 
        user_id, 
        COUNT(event_id) as login_count
    FROM user_logins
    WHERE login_date > CURRENT_DATE - INTERVAL '30 days'
    GROUP BY 1
)
SELECT 
    s.user_id,
    s.total_tickets,
    p.login_count,
    s.avg_satisfaction
FROM SupportVolume s
JOIN PlatformActivity p ON s.user_id = p.user_id
WHERE s.total_tickets > 5 AND p.login_count < 2
ORDER BY s.total_tickets DESC;


-- 2. REVENUE EXPANSION TRACKER (The "Upsell" Query)
-- Goal: Find accounts that are hitting their "usage limits" and are ripe for a higher tier.
-- Vital for: Affiliate Marketers (B12) & Revenue Ops (Allium).

SELECT 
    account_name,
    current_plan,
    usage_metric_count,
    plan_limit,
    (usage_metric_count::float / plan_limit) * 100 as limit_utilization_pct
FROM account_usage
WHERE (usage_metric_count::float / plan_limit) > 0.85
ORDER BY limit_utilization_pct DESC;


-- 3. SUPPORT IMPACT ON RETENTION
-- Goal: Calculate if customers who have their tickets resolved in < 2 hours have higher renewal rates.
-- Vital for: Product Support (Amplemarket/Equip).

SELECT 
    CASE WHEN resolution_time_hrs <= 2 THEN 'Fast Support' ELSE 'Standard Support' END as support_tier,
    COUNT(DISTINCT user_id) as total_customers,
    SUM(CASE WHEN status = 'Renewed' THEN 1 ELSE 0 END)::float / COUNT(*) as renewal_rate
FROM customer_lifecycle_data
GROUP BY 1;
