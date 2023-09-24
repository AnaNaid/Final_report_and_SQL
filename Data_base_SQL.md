# Работа с базой данных в Яндекс Самокат

SELECT cour.login, 
	COUNT (orde."inDelivery" = true) 
FROM "Couriers" AS cour 
LEFT OUTER JOIN "Orders" AS orde ON cour.id = orde."courierId" 
GROUP BY cour.login;



SELECT track, 
	CASE 
		WHEN finished = true THEN '2' 
		WHEN cancelled= true THEN '-1' 
		WHEN "inDelivery" = true THEN '1' 
		ELSE '0' 
	END 
	FROM "Orders";
	
	
	
	
