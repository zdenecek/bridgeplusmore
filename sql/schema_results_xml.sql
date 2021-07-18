DROP TABLE IF EXISTS result_lesson;
CREATE TABLE result_lesson (
Id INTEGER PRIMARY KEY AUTOINCREMENT,
LessonNumber INTEGER,
Year INTEGER,
LessonName INTEGER,
SourceContent TEXT,
ResultXml TEXT,
UpdatedAt DATETIME DEFAULT (datetime('now','localtime')),
Unique(LessonNumber, Year)
);