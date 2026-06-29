
-- ================================================
-- Sales Analytics Dashboard — KPI Queries
-- Dataset: Superstore Sales | Tool: SQLite
-- Author: Abdul
-- ================================================

-- 1. Overall business summary
SELECT
    COUNT(DISTINCT "Order ID")    AS Total_Orders,
    COUNT(DISTINCT "Customer ID") AS Total_Customers,
    ROUND(SUM(Sales), 2)          AS Total_Revenue,
    ROUND(SUM(Profit), 2)         AS Total_Profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Overall_Margin_Pct
FROM sales;

-- 2. Revenue and profit by year
SELECT Year, ROUND(SUM(Sales),2) AS Revenue,
    ROUND(SUM(Profit),2) AS Profit,
    ROUND(SUM(Profit)/SUM(Sales)*100,2) AS Margin_Pct
FROM sales GROUP BY Year ORDER BY Year;

-- 3. Performance by region
SELECT Region, ROUND(SUM(Sales),2) AS Revenue,
    ROUND(SUM(Profit),2) AS Profit
FROM sales GROUP BY Region ORDER BY Revenue DESC;

-- 4. Category and sub-category breakdown
SELECT Category, "Sub-Category",
    ROUND(SUM(Sales),2) AS Revenue,
    ROUND(SUM(Profit),2) AS Profit
FROM sales GROUP BY Category, "Sub-Category" ORDER BY Profit DESC;

-- 5. Discount impact on profit
SELECT
    CASE
        WHEN Discount = 0     THEN '0% - No discount'
        WHEN Discount <= 0.10 THEN '1-10%'
        WHEN Discount <= 0.20 THEN '11-20%'
        WHEN Discount <= 0.30 THEN '21-30%'
        ELSE 'Above 30%'
    END AS Discount_Band,
    ROUND(AVG(Profit),2) AS Avg_Profit,
    ROUND(SUM(Profit)/SUM(Sales)*100,2) AS Margin_Pct
FROM sales GROUP BY Discount_Band;
