# Produce Queries
GET_ALL_PRODUCE_QUERY = "SELECT produce_id AS id, produce_name AS name, description, price, season FROM Produce;"
GET_PRODUCE_BY_ID_QUERY = "SELECT produce_id AS id, produce_name AS name, description, price, season FROM Produce WHERE produce_id = %s;"
INSERT_PRODUCE_QUERY = "INSERT INTO Produce (produce_name, description, price, season) VALUES (%s, %s, %s, %s);"

# Farming Practices Queries
GET_ALL_FARMING_PRACTICES_QUERY = "SELECT practice_id AS id, practice_name, description FROM FarmingPractices;"

# Community Events Queries
GET_ALL_COMMUNITY_EVENTS_QUERY = "SELECT event_id AS id, event_name, event_date, description FROM CommunityEvents;"
