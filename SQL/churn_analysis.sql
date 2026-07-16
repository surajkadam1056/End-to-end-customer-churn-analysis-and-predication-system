USE Datasciences_project;
SELECT DATABASE();
SHOW TABLES

-- describe the data 
SELECT * FROM cleaned_dataset LIMIT 10;

-- check the columns 
DESCRIBE cleaned_dataset;

-- understanding the dataset 
-- 1) check total rows 
SELECT COUNT(*) FROM cleaned_dataset;

-- 2)check churn distriubtion 
SELECT churned, COUNT(*) 
FROM cleaned_dataset
GROUP BY churned;

#login behavior 
SELECT 
login_frequency,
COUNT(*) AS users,
SUM(churned) AS churned
FROM cleaned_dataset
GROUP BY login_frequency
ORDER BY login_frequency;

#value analysis 
SELECT 
AVG(lifetime_value)
FROM cleaned_dataset;

#make clean view 
CREATE VIEW clean_data AS
SELECT 
age,
login_frequency,
lifetime_value,
churned,
CASE 
    WHEN country_India = 1 THEN 'India'
    WHEN country_USA = 1 THEN 'USA'
    ELSE 'Other'
END AS country
FROM cleaned_dataset;

#simple analysis 
SELECT 
country,
COUNT(*) AS total,
SUM(churned) AS churned
FROM clean_data
GROUP BY country;