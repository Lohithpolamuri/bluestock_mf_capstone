-- Top 5 funds by return

SELECT scheme_name, return_1yr_pct
FROM scheme_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- Average NAV

SELECT AVG(nav) AS avg_nav
FROM nav_history;

-- Total transactions by type

SELECT transaction_type,
COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY transaction_type;

-- Total investment amount by state

SELECT state,
SUM(amount_inr) AS total_amount
FROM investor_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- Number of schemes by category

SELECT category,
COUNT(*) AS total_schemes
FROM fund_master
GROUP BY category;