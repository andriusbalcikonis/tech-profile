# MSSQL answers

| #   | Answer                                                                                                                |
| :-- | :-------------------------------------------------------------------------------------------------------------------- |
| 1   | Keeping track of changes in structure                                                                                 |
| 2   | No, it may take different index                                                                                       |
| 3   | Xml schema should be set                                                                                              |
| 4   | SQL Server Express supports a maximum size of 4 GB per database, which excludes all the log files.                    |
| 5   | yes                                                                                                                   |
| 6   | No                                                                                                                    |
| 7   | varchar is stored in row, must be under 8KB. varchar(max) must be under 2GB (pinter outside of row)                   |
| 8   | varchar(max)                                                                                                          |
| 9   | BCP or BulkCopy is a tool used to copy huge amounts of data from tables and views                                     |
| 10  | Global temp table can be seen in different connections while it exists                                                |
| 11  | Log shipping                                                                                                          |
| 12  | Yes                                                                                                                   |
| 13  | B                                                                                                                     |
| 14  | After many changes                                                                                                    |
| 15  | Truncate resets the identity                                                                                          |
| 16  | Primary - clustered, unique - nonclustered                                                                            |
| 17  | Primary - 0, Unique - 1                                                                                               |
| 18  | Index rows                                                                                                            |
| 19  | Performance                                                                                                           |
| 20  | inner join                                                                                                            |
| 21  | Cross join                                                                                                            |
| 22  | Yes                                                                                                                   |
| 23  | Collation                                                                                                             |
| 24  | LinkedServers                                                                                                         |
| 25  | No, only after                                                                                                        |
| 26  | Instead of and after                                                                                                  |
| 27  | No                                                                                                                    |
| 28  | Set minus operation - cxompares two sets and removes duplicating ones                                                 |
| 29  | No                                                                                                                    |
| 30  | do smth ERROR_MESSAGE();                                                                                              |
| 31  | Uncheck checkbox in mamagement studio                                                                                 |
| 32  | union - takes unique, union all - all.                                                                                |
| 33  | You can't reference a view in a foreign key                                                                           |
| 34  | No                                                                                                                    |
| 35  | Virtual table                                                                                                         |
| 36  | Stored select                                                                                                         |
| 37  | Yes                                                                                                                   |
| 38  | Yes                                                                                                                   |
| 39  | Constraints                                                                                                           |
| 40  | Triggers                                                                                                              |
| 41  | Jobs                                                                                                                  |
| 42  | Activity Monitor                                                                                                      |
| 43  | Yes                                                                                                                   |
| 44  | Data pages                                                                                                            |
| 45  | Seek                                                                                                                  |
| 46  | Second one                                                                                                            |
| 47  | No                                                                                                                    |
| 48  | Yes                                                                                                                   |
| 49  | No                                                                                                                    |
| 50  | Index join                                                                                                            |
| 51  | Yes                                                                                                                   |
| 52  | Dirty read                                                                                                            |
| 53  | No                                                                                                                    |
| 54  | Yes                                                                                                                   |
| 55  | First is BLOB                                                                                                         |
| 56  | @name                                                                                                                 |
| 57  | @@variable                                                                                                            |
| 58  | No                                                                                                                    |
| 59  | Yes                                                                                                                   |
| 60  | No                                                                                                                    |
| 61  | ROW_NUMBER() OVER()                                                                                                   |
| 62  | Nested loop, hash join and merge join                                                                                 |
| 63  | Recursive selects                                                                                                     |
| 64  | Truncate                                                                                                              |
| 65  | WITH SCHEMABINDING                                                                                                    |
| 66  | Yes                                                                                                                   |
| 67  | No                                                                                                                    |
| 68  | FILLFACTOR option while creating                                                                                      |
| 69  | 70-90                                                                                                                 |
| 70  | Recreation of indexes                                                                                                 |
| 71  | FILLFACTOR usage not only in leaf level                                                                               |
| 72  | No                                                                                                                    |
| 73  | Free Text index                                                                                                       |
| 74  | Yes                                                                                                                   |
| 75  | Because query optimiser uses it                                                                                       |
| 76  | Trace file                                                                                                            |
| 77  | Tmp table creation                                                                                                    |
| 78  | Not using an index                                                                                                    |
| 79  | 1                                                                                                                     |
| 80  | More rows per page                                                                                                    |
| 81  | No                                                                                                                    |
| 82  | Publisher, distributor, subscriber                                                                                    |
| 83  | Publicator and distributor                                                                                            |
| 84  | Yes                                                                                                                   |
| 85  | Publication                                                                                                           |
| 86  | Subscription                                                                                                          |
| 87  | Push and pull                                                                                                         |
| 88  | On distributor                                                                                                        |
| 89  | On subscriber                                                                                                         |
| 90  | Snapshot, transactional, merge                                                                                        |
| 91  | Snapshot and transactional                                                                                            |
| 92  | Merge                                                                                                                 |
| 93  | Takes snapshot and checks, if it needs to be transmitted                                                              |
| 94  | Service Broker                                                                                                        |
| 95  | Add column in replication                                                                                             |
| 96  | Yes                                                                                                                   |
| 97  | Alt F1                                                                                                                |
| 98  | When doing import of lots of tables, classifiers, etc. Then it is wise to get all data without them and recreate.     |
| 99  | Filtered index - create index ... where a is not null                                                                 |
| 100 | Drop and create with recompile                                                                                        |
| 101 | Synonim                                                                                                               |
| 102 | Yes, no.                                                                                                              |
| 103 | No                                                                                                                    |
| 104 | function, change all calling places                                                                                   |
| 105 | Order                                                                                                                 |
| 106 | select a.b.value() from xmlvar.nodes() a(b)                                                                           |
| 107 | Checks condition on every row join                                                                                    |
| 108 | It will not recongnize it, until its cache is refreshed                                                               |
| 109 | It is false even after NOT opperation                                                                                 |
| 110 | set rowcount x                                                                                                        |
| 111 | No                                                                                                                    |
| 112 | No, one window - one connection - one transaction                                                                     |
| 113 | compatible with .net zero date, can be smaller without miliseconds                                                    |
| 114 | Smaller, can be sure that no bad data will be stored                                                                  |
| 115 | Filtered indexes                                                                                                      |
| 116 | They are included in the row, except if it exceeds 8K                                                                 |
| 117 | DB reports menu and dynamic management views                                                                          |
| 118 | Caches for the same queries                                                                                           |
| 119 | 1                                                                                                                     |
| 120 | top, subselect and row_number. 2005 and more                                                                          |
| 121 | Merge replication with several sources                                                                                |
| 122 | One read will read too little rows, this is important for index structures                                            |
| 123 | 1. When you need to have id before saving in db 2. Merge replication                                                  |
| 124 | ResolveUrl returns a path relative to the site root                                                                   |
| 125 | Need to have statements "set quated identifiers on/off"                                                               |
| 126 | @xml.modify('insert...                                                                                                |
| 127 | SCOPE IDENTITY                                                                                                        |
| 128 | use escape keyword                                                                                                    |
| 129 | Cannot be done for several rows                                                                                       |
| 130 | Serializable blocks modifications. Snapshot does not, but keeps two copies of selected data.                          |
| 131 | Serializable and Snapshot                                                                                             |
| 132 | Repeatable Read                                                                                                       |
| 133 | 1. Select will block while other transactions are modifying. 2. New transactions will block until select is performed |
| 134 | Dirty reads                                                                                                           |
| 135 | Read Commited                                                                                                         |
| 136 | Read Uncommited                                                                                                       |
| 137 | In transaction scope constructor                                                                                      |
