USE `KitchenKorner`;

INSERT INTO Users (User_ID, Username, Email, Full_Name)
VALUES (1, 'janelovesfood', 'jane.smith@kitchenkorner.com', 'Jane Smith'),
       (2, 'aliray', 'alison.ray@kitchenkorner.com', 'Alison Ray'),
       (3, 'sarahfoodie', 'sarah.anderson@kitchenkorner.com', 'Sarah Anderson');

INSERT INTO Filters (Filter_ID) VALUES (55),
                                       (56);

INSERT INTO Posts (Post_ID, User_ID, Filter_ID) VALUES (1000, 1, 55),
                                                       (1001, 1, 56),
                                                       (1002, 3, 55);

INSERT INTO Ingredients (Amount, Ingredient_ID, Price, Store, Ingredients.Ingredient_Name)
VALUES (1, 0625, 6.99, 'Star Market', 'Avocado'),
       (2, 0635, 5.99, 'Star Market', 'Bread'),
       (1, 0645, 7.99, 'Star Market', 'Eggs'),
       (1, 0655, 6.99, 'Stop and Shop', 'Milk');

INSERT INTO Recipes (Instructions, Image, Meal_Type, Recipe_ID,
                     Recipe_Name, Post_ID, Cuisine, Expected_Time, Expected_Difficulty)
VALUES ('Slice 1 avocado into pieces. Make egg over easy. Put avocado slices on bread. Put egg on avocado slices.',
        'https://example.com/images/image1.jpeg', 'Breakfast', 1000, 'Avocado Toast', 1000, '', 0.1, 2),
    ('Cook pasta. Cook Chicken. Pour alfredo.', 'https://example.com/images/image2.jpeg', 'Dinner', 1001, 'Chicken Alfredo', 1001, '', 0.5, 4);

INSERT INTO IngredientDetails (Recipe_ID, Ingredient_ID) VALUES (1000, 0625),
                                                                (1000, 0635),
                                                                (1000, 0645);

INSERT INTO Comments (Text, User_ID, Comment_ID, Post_ID)
VALUES ('Love!', 2, 8000, 1000),
       ('Yum!', 3, 8001, 1000),
       ('Thanks!', 1, 8002, 1000);

INSERT INTO Ratings (Rating_ID, Actual_Difficulty, Actual_Time, Taste, Post_ID, User_ID)
VALUES (2000, 3, 0.2, 8, 1000, 2),
       (2001, 2, 0.2, 9, 1000, 3);

INSERT INTO Follows (Followee_ID, Follower_ID) VALUES (3, 2),
                                                      (3, 1),
                                                      (2, 1),
                                                      (1, 2),
                                                      (1, 3);

INSERT INTO Feeds (Following_ID, Post_ID, User_ID) VALUES (1, 1000, 1),
                                                          (2, 1001, 3);

INSERT INTO Cookbook (Cookbook_ID, Recipe_ID, User_ID, Modified_Datetime)
VALUES (700, 1000, 1, current_timestamp),
       (701, 1001, 1, current_timestamp);

INSERT INTO External_Messages (Message_ID, Post_ID, User_ID, Text)
VALUES (10000, 1000, 2, 'Check this out!'),
       (10001, 1001, 2, 'Lets try this');

INSERT INTO Tags (Post_ID, User_ID) VALUES (1000, 2),
                                          (1001, 2);

INSERT INTO Recipe_Cookbook (Recipe_ID, Cookbook_ID)
VALUES (1000, 700),
       (1001, 700);

INSERT INTO Direct_Messages (User_ID, Text, Post_ID) VALUES (1, 'You would love this', 1000),
                                                            (2, 'Going to the grocery store rn!', 1001);

INSERT INTO Keywords_In (Filter_ID, Keyword_One) VALUES (55, 'Pasta'),
                                                        (56, 'Dinner');

INSERT INTO Keywords_Out (Filter_ID, Keyword_One) VALUES (55, 'Dairy'),
                                                         (56, 'Nut');