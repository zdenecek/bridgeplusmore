DROP TABLE IF EXISTS bm_board;
CREATE TABLE bm_board (
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
    LessonId INTEGER,
    DistListID STRING,
    Year INTEGER,
    LessonNumber INTEGER,
    Name STRING,
    PostText TEXT,
    PreText TEXT,
    CreatedAt DATETIME,
    UpdatedAt DATETIME
);
DROP TABLE IF EXISTS bm_set;
CREATE TABLE bm_set (Id INTEGER PRIMARY KEY AUTOINCREMENT);