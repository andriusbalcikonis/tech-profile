# MSSQL questions

| #   | Question                                                                                                                                                                                       |
| :-- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | What super useful feature about DB projects does VS2012+ has?                                                                                                                                  |
| 2   | If you do repeated select without order, can you expect same result order every time?                                                                                                          |
| 3   | What should be done to xml column so that it could have index?                                                                                                                                 |
| 4   | What is the Maximum Size per Database for SQL Server Express?                                                                                                                                  |
| 5   | Is It Possible to have non-Clustered Index on Separate Drive From Original Table Location?                                                                                                     |
| 6   | Is It Possible to have Clustered Index on Separate Drive From Original Table Location?                                                                                                         |
| 7   | What is the difference between varchar(N) and varchar (MAX)? (size and place)                                                                                                                  |
| 8   | Which one large text type is recommended - varchar(max) or text?                                                                                                                               |
| 9   | What is BCP? When is it Used?                                                                                                                                                                  |
| 10  | Global temp table vs local temp table. Both are dropped when connection A is dropped. What is the difference?                                                                                  |
| 11  | The process of automating the backup of database and transaction log files on a production SQL server and then restoring them onto a standby server. - How is it called?                       |
| 12  | Can procedures be called recursively?                                                                                                                                                          |
| 13  | Connection pools - what kind of app uses it? - A. Web app (ASP.NET) - B. Any .Net app (ADO.NET)                                                                                                |
| 14  | When UPDATE_STATISTICS command is recomended?                                                                                                                                                  |
| 15  | What interesting feature does truncate command have (related to ids)                                                                                                                           |
| 16  | Primary key vs unique key - what kind of index do they create?                                                                                                                                 |
| 17  | Primary key vs unique key - how many null records does they allow?                                                                                                                             |
| 18  | What are the leaf nodes of non-clustered index?                                                                                                                                                |
| 19  | What problems will you face, if you want search by full text search and then sort by some other column?                                                                                        |
| 20  | A join that displays only the rows that have a match in both joined tables                                                                                                                     |
| 21  | Join that does not have a WHERE clause produces the Cartesian product of the tables involved in the join - how is it called?                                                                   |
| 22  | Can functions be used in joins like tables?                                                                                                                                                    |
| 23  | A set of rules that determine how data is sorted and compared. How is it called?                                                                                                               |
| 24  | What MS SQL feature allows to join tables from different servers?                                                                                                                              |
| 25  | DDL Triggers - can there be instead of type of DDL trigger?                                                                                                                                    |
| 26  | What are two types of DML Triggers?                                                                                                                                                            |
| 27  | if you do select @a = a from table... and no row is selected, will @a be set to null?                                                                                                          |
| 28  | What does EXEPT statement does in selects?                                                                                                                                                     |
| 29  | If you have a<> 1 in where condition, will nulls be taken?                                                                                                                                     |
| 30  | Waht is the syntax in BEGIN TRY END TRY BEGIN CATCH ... END CATCH                                                                                                                              |
| 31  | In management studio, if you want to change column type in designer and it blocks this action saying, that rows need to be recreated. Is there a way to workaround this?                       |
| 32  | What is the difference between union and union all?                                                                                                                                            |
| 33  | Can I have a foreign key referencing a column in a view in SQL Server?                                                                                                                         |
| 34  | View is created, then table column type is changed. Will view column type change automatically?                                                                                                |
| 35  | What view is logically to his caller?                                                                                                                                                          |
| 36  | What view is physically?                                                                                                                                                                       |
| 37  | Can views have indexes?                                                                                                                                                                        |
| 38  | Does view indexes have more restrictions, than normal indexes?                                                                                                                                 |
| 39  | What can you create for column if you want some checks?                                                                                                                                        |
| 40  | What can you create for table if you want to have before/after "handlers" for insert/update/delete actions?                                                                                    |
| 41  | What can you create if you want some scheduled tasks on sql server?                                                                                                                            |
| 42  | What tool should be used to watch and kill processes?                                                                                                                                          |
| 43  | Can stored procedure return more than one select?                                                                                                                                              |
| 44  | What are leaf levels of clustered index?                                                                                                                                                       |
| 45  | Which is faster - index seek, or index scan?                                                                                                                                                   |
| 46  | Which is better in where condition: a=isnull(@a, a) or @a is null or a = @a?                                                                                                                   |
| 47  | Is index used in "where is null..."                                                                                                                                                            |
| 48  | Is index used in "WHERE .A. AND .B."?                                                                                                                                                          |
| 49  | Is index used in "WHERE .A. OR .B."                                                                                                                                                            |
| 50  | If both indexes are used in "WHERE .A. AND .B.", if they are created separately, how it is done                                                                                                |
| 51  | Is hash join expensive, compared to other joins?                                                                                                                                               |
| 52  | What does SELECT (nolock) mean?                                                                                                                                                                |
| 53  | Does SELECT without nolock cause table to lock?                                                                                                                                                |
| 54  | Is there table data type?                                                                                                                                                                      |
| 55  | What is the difference between nVarcharMax and nVarChar?                                                                                                                                       |
| 56  | How local variables are marked                                                                                                                                                                 |
| 57  | How global variables are marked?                                                                                                                                                               |
| 58  | Does Like '%..' use index?                                                                                                                                                                     |
| 59  | Does Like '..%' use index?                                                                                                                                                                     |
| 60  | Does negatives (!=, NOT IN) use index?                                                                                                                                                         |
| 61  | How to add rownumber column?                                                                                                                                                                   |
| 62  | What are three types of joins?                                                                                                                                                                 |
| 63  | What nice feature does construct "With tmpTable (...) AS {SELECT}" support?                                                                                                                    |
| 64  | What is better alternative to delete, if all table is deleted?                                                                                                                                 |
| 65  | How view should be created to support view indexes?                                                                                                                                            |
| 66  | Can execution plans be logged in profiler?                                                                                                                                                     |
| 67  | Is Convert and Cast any different?                                                                                                                                                             |
| 68  | How to set some free space in index pages to avoid index fragmentation?                                                                                                                        |
| 69  | What are usual FILLFACTOR values?                                                                                                                                                              |
| 70  | What needs to be done to avoid index fragmentation besides initial fillfactor setting?                                                                                                         |
| 71  | What does index xreate directive pad_index mean?                                                                                                                                               |
| 72  | If >50% of rows are selected, will it use index?                                                                                                                                               |
| 73  | If ntext field needs index, what should be done?                                                                                                                                               |
| 74  | Can free text index search for similar words?                                                                                                                                                  |
| 75  | Why statistics should be renewed regularly?                                                                                                                                                    |
| 76  | What usually can be passed for tuning advisor?                                                                                                                                                 |
| 77  | What bad effect has stream aggregate execution plan step?                                                                                                                                      |
| 78  | What bad effect has "sort" or "filter" execution plan step?                                                                                                                                    |
| 79  | How many read operations does it take to read one page?                                                                                                                                        |
| 80  | Why it is possible that nonclustered index works faster than clustered?                                                                                                                        |
| 81  | Can secondary xml index be created without creating primary xml index?                                                                                                                         |
| 82  | What are three main services in replication?                                                                                                                                                   |
| 83  | What two of three main replication services can be on same machine?                                                                                                                            |
| 84  | Can stored procedure be an replication article?                                                                                                                                                |
| 85  | How set of articles is called in replication?                                                                                                                                                  |
| 86  | How request to replicate a publication is called in replication?                                                                                                                               |
| 87  | What are two types of subscriptions?                                                                                                                                                           |
| 88  | Where "push" type subscription agent runs?                                                                                                                                                     |
| 89  | Where "pull" type subscription agent runs?                                                                                                                                                     |
| 90  | What 3 types of replication there are?                                                                                                                                                         |
| 91  | What two types of repliaction use push subscription?                                                                                                                                           |
| 92  | What type of repliaction use pull subscription?                                                                                                                                                |
| 93  | What is the first action, which transactional replication takes on initialization?                                                                                                             |
| 94  | What is msmq analog service in ms sql?                                                                                                                                                         |
| 95  | For huge replicated tables, when need to add column, how not to cause reinitialization?                                                                                                        |
| 96  | Is it possible, that sometimes better way to update replicated table rows is to stop repliaction and reinitialize it afterwards?                                                               |
| 97  | In query analyser, what command selects main info about table?                                                                                                                                 |
| 98  | When foreign keys become to have disadvantages?                                                                                                                                                |
| 99  | If query always selects the same subset of table (lets say not null) what is the way to make smaller index, than default. What syntax (roughly) should be used?                                |
| 100 | If you alter the procedure, and it throws error, that there were problems finding query plan, what needs to be done?                                                                           |
| 101 | When multiple usages of different DB are needed, what is the construct to give a name for all calls to this DB?                                                                                |
| 102 | Can column be altered from int to decimal? Will it delete and recreate all rows?                                                                                                               |
| 103 | If where condition filters smthing, will row_number have gaps?                                                                                                                                 |
| 104 | What makes a little bit more trouble - to add param for procedure or function? Why?                                                                                                            |
| 105 | In which construct - where, group, having, order, - can you use given name for calculated "column"?                                                                                            |
| 106 | If we have declare'd xmlvar xml, what is the syntax to select relational data from it?                                                                                                         |
| 107 | What does cross apply do?                                                                                                                                                                      |
| 108 | If you have just added new object to DB, what small inconvenience can be expected in management studio?                                                                                        |
| 109 | What is the super strange behaviour when comparing null value?                                                                                                                                 |
| 110 | When writing scripts, which command in the begginning would control, that only limited number of rows would be updated?                                                                        |
| 111 | If you write script: begin tran, XXX, rollback - and stop execution at XXX - will transaction be reverted?                                                                                     |
| 112 | If transaction is in progress in one management studios window - can it be rolled back in other? Why?                                                                                          |
| 113 | Why column type datetime2 is useful? Give two reasons)                                                                                                                                         |
| 114 | Why date and time column types are useful? Give two reasons.                                                                                                                                   |
| 115 | What single best feature related to indexes is in MS SQL 2008?                                                                                                                                 |
| 116 | Why are nvarchar(max) and varbinary(max) better than blob?                                                                                                                                     |
| 117 | If I want to get some stats about how indexes are used, what indexes sql server wanted to have, - what are two ways to do it?                                                                  |
| 118 | If ORM generates queries dynamically, what SQL server does to execution plans?                                                                                                                 |
| 119 | If you write order by x, from which number columns are indexed?                                                                                                                                |
| 120 | If you need to skip some rows and take some rows, how to do it in sql? What version of sql server would allow that?                                                                            |
| 121 | In what situation it is needed to have ids like this - 50000000001 400000000002...?                                                                                                            |
| 122 | What is the biggest disadvantage of Guid's big space?                                                                                                                                          |
| 123 | When does Guid is very useful?                                                                                                                                                                 |
| 124 | Of two similar methods - ResolveClientUrl and ResolveUrl - which one returns path relative to site root? Which one relative to current page?                                                   |
| 125 | If you see error msg "unable to generate query plan", what can be wrong with your stored procedure?                                                                                            |
| 126 | There is xml type variable @xml - what is the syntax to insert tag?                                                                                                                            |
| 127 | If IDENTITY gives not what you need inside the trigger, what alternative could be used?                                                                                                        |
| 128 | What to do, if there are '[' symbols in like statement, and it behaves stangely?                                                                                                               |
| 129 | What is the main restriction, if you want to do xml.modify?                                                                                                                                    |
| 130 | Isolation levels - What is the difference of Serializable and Snapshot isolation levels?                                                                                                       |
| 131 | Isolation levels - We have two same selects in the same transaction. What is the isolation level, that makes sure rows read in first select will be unchanged (and new ones may not be added)? |
| 132 | Isolation levels - We have two same selects in the same transaction. What is the isolation level, that makes sure rows read in first select will be unchanged (but new ones may be added)?     |
| 133 | Isolation levels - What are the bad consequences of isolation level Read Commited?                                                                                                             |
| 134 | Isolation levels - What are the bad consequences of Read Uncommited isolation level?                                                                                                           |
| 135 | Isolation levels - What is the default isolation level?                                                                                                                                        |
| 136 | Isolation levels - What isolation level is (nolock) shortcut to?                                                                                                                               |
| 137 | Isolation levels - How to set isolation level from .net?                                                                                                                                       |
