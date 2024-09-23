SELECT s1.Name AS name
FROM Friends f
JOIN Students s1 ON f.ID = s1.ID
JOIN Students s2 ON f.Friend_ID = s2.ID
JOIN Packages p1 ON s1.ID = p1.ID
JOIN Packages p2 ON s2.ID = p2.ID
WHERE p2.Salary > p1.Salary
ORDER BY p2.Salary DESC;