# CREATE TABLE book
# (book_id int,
# book_title text,
# book_author text,
# publisher_id int)
#
# SELECT * FROM book
# INSERT INTO book VALUES
# (1,'Руслан и Людмила', 'Пушкин', 100),
# (2,'Мцыри', 'Лермонтов', 100),
# (3,'Война и мир', 'Толстой', 100),
# (4,'Братья Карамазовы', 'Достоевский', 200),
# (5, 'Палата №6','Чехов', 300),
# (6,'Гроза', 'Островский', 200),
# (7,'Лолита', 'Набоков', 600),
# (8,'Детство', 'Горький', 300),
# (9,'Мертвые души', 'Гоголь', 100),
# (10,'Медный всадник', 'Пушкин', 100),
# (11,'Доктор Живаго', 'Пастернак', 700),
# (12,'Мойдодыр', 'Чуковский', 200),
# (13,'Герой нашего времени', 'Лермонтов', 600),
# (14,'Калина красная', 'Шукшин', 800),
# (15,'Чемодан', 'Довлатов', 800)
#
# SELECT book_title, book_author FROM book WHERE publisher_id = 100
# SELECT book_title, book_author, book_id FROM book WHERE publisher_id = 300
# SELECT book_id, book_title, book_author, publisher_id FROM book WHERE book_author = 'Пушкин'
# SELECT book_id, book_title, book_author, publisher_id FROM book WHERE book_title LIKE 'П%'