DROP TABLE IF EXISTS bm_boards;
CREATE TABLE bm_boards (
Id INTEGER PRIMARY KEY AUTOINCREMENT,
SetId INTEGER,
ExampleNumber INTEGER,
DistID STRING,
BoardName STRING,
BidStr STRING,
CommentEast TEXT,
CommentLead TEXT,
CommentWest TEXT,
CommentNorth TEXT,
CommentPlay TEXT,
CommentSouth TEXT,
CommentPostMortem TEXT,
DistNorth STRING,
DistEast STRING,
DistSouth STRING,
DistWest STRING,
Vuln STRING,
DistributionPlayStr STRING,
FinalBid STRING,
LeaderToEachTrick STRING,
SuggestedLeadCard STRING,
SuggestedTricks INTEGER,
TeacherTags STRING,
WinnerOfTrick STRING,
CreatedAt DATETIME,
UpdatedAt DATETIME
);

DROP TABLE IF EXISTS bm_structure;
CREATE TABLE bm_structure (
Id INTEGER PRIMARY KEY AUTOINCREMENT,
LectionId INTEGER,
DistListID STRING,
Year INTEGER,
LectionNumber INTEGER,
Name STRING,
PostText TEXT,
PreText TEXT,
CreatedAt DATETIME,
UpdatedAt DATETIME
);
DROP TABLE IF EXISTS source_lessons;
CREATE TABLE source_lessons (
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Year INTEGER,
LectionNumber INTEGER,
Name STRING,
Type STRING,
Include INTEGER,
FullText TEXT,
StartText TEXT,
EndText TEXT,
Literature TEXT,
CreatedAt DATETIME,
UpdatedAt DATETIME,
CHECK (Include IN (0, 1))
);
DROP TABLE IF EXISTS result_lesson;
CREATE TABLE result_lesson (
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Number INTEGER,
Year INTEGER,
Content TEXT,
CreatedAt DATETIME,
UpdatedAt DATETIME,
);