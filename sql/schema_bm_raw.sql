DROP TABLE IF EXISTS bm_board;
CREATE TABLE bm_board (
    StructureRowId INTEGER,
    ExampleNumber INTEGER,
    HasChanges INTEGER DEFAULT 1 CHECK (HasChanges IN (0,1)),
    ToUpload INTEGER DEFAULT 0 CHECK (ToUpload IN (0,1)),
    DistID STRING,
    BoardName STRING,
    BidStr STRING,
    CommentEast TEXT,
    CommentWest TEXT,
    CommentNorth TEXT,
    CommentSouth TEXT,
    CommentLead TEXT,
    CommentBidding TEXT,
    CommentBoard TEXT,
    CommentPlay TEXT,
    CommentPostMortem TEXT,
    UnusedEndText TEXT,
    DistAsText TEXT,
    DistNorth STRING,
    DistEast STRING,
    DistSouth STRING,
    DistWest STRING,
    GeneratedHands STRING,
    Vuln STRING,
    DistributionPlayStr STRING,
    FinalBid STRING,
    LeaderToEachTrick STRING,
    SuggestedLeadCard STRING,
    SuggestedTricks INTEGER,
    TeacherTags STRING,
    WinnerOfTrick STRING,
    CreatedAt DATETIME  DEFAULT (datetime('now','localtime')),
    UpdatedAt DATETIME DEFAULT (datetime('now','localtime')),
    UNIQUE(StructureRowId, ExampleNumber)
);
DROP TABLE IF EXISTS bm_structure;
CREATE TABLE bm_structure (
    LessonId INTEGER,
    HasChanges INTEGER DEFAULT 1,
    DistListID STRING,
    Year INTEGER,
    LessonNumber INTEGER,
    Name STRING,
    PostText TEXT,
    PreText TEXT,
    UnusedText TEXT,
    CreatedAt DATETIME  DEFAULT (datetime('now','localtime')),
    UpdatedAt DATETIME  DEFAULT (datetime('now','localtime')),
    UNIQUE(LessonId)
);
DROP TABLE IF EXISTS bm_set;
CREATE TABLE bm_set (Id INTEGER PRIMARY KEY AUTOINCREMENT);