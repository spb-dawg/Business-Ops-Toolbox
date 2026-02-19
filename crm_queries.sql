-- 1. Identify Duplicate Leads (Common CRM issue)
-- This finds emails that appear more than once in the leads table.
SELECT email, COUNT(email)
FROM leads
GROUP BY email
HAVING COUNT(email) > 1;

-- 2. Calculate Conversion Rate by Lead Source
-- Useful for seeing which marketing channels actually work.
SELECT lead_source, 
       COUNT(*) as total_leads,
       SUM(CASE WHEN status = 'Closed Won' THEN 1 ELSE 0 END) as conversions,
       (SUM(CASE WHEN status = 'Closed Won' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) as conversion_rate
FROM sales_pipeline
GROUP BY lead_source
ORDER BY conversion_rate DESC;

-- 3. Find "Stale" Opportunities
-- Finds deals that haven't been touched in over 30 days.
SELECT opportunity_name, account_manager, last_activity_date
FROM opportunities
WHERE status = 'Open' 
AND last_activity_date < DATE('now', '-30 days');
