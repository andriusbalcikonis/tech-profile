# Entity Framework questions

| #   | Question                                                                                                                                                                 |
| :-- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | How to write left joins in EF?                                                                                                                                           |
| 2   | Why class functions System.Entity.DBFunctions are useful?                                                                                                                |
| 3   | Why EF7 will be faster?                                                                                                                                                  |
| 4   | What is the most important change in EF7?                                                                                                                                |
| 5   | What is the syntax if you want to include first and second level navigation properties and first level is a collection.                                                  |
| 6   | Dapper, Massive and PetaPoco - what are the advantages of each?                                                                                                          |
| 7   | Name three micro ORM products                                                                                                                                            |
| 8   | What is the feature, shared by both Micro ORMs and ORMs?                                                                                                                 |
| 9   | What are two main advantages of using one of micro ORMs?                                                                                                                 |
| 10  | What is a good practice regarding null checks?                                                                                                                           |
| 11  | What is a best practice regarding the lazy loading?                                                                                                                      |
| 12  | Is Code First suitable for serious big production projects?                                                                                                              |
| 13  | Is there a way to generate code first classes from existing db?                                                                                                          |
| 14  | How can you add t4 template for code generation in EF?                                                                                                                   |
| 15  | Can you apply where conditions on include method in EFv6? In nHybernate?                                                                                                 |
| 16  | What two classes are "main" in code first (to use POCO classes in ORM)?                                                                                                  |
| 17  | In EF, can model and db table differ?                                                                                                                                    |
| 18  | In EF, can model be generated before DB table?                                                                                                                           |
| 19  | EFCF - when you change something in model, what does EFCF do by default?                                                                                                 |
| 20  | EFCF - when you change something in model and exception is thrown, where can you set one of IDatabaseInitializer implementations (usually recreate on changes strategy)? |
| 21  | If you change context class itself in EFCF, what does it do on the next run to DB?                                                                                       |
| 22  | What if no int property (to be used as an key) is provided in model, what will EFCF do?                                                                                  |
| 23  | EFCF - what class must have, if you want to have hierarchy? Does EFCF expect you to use some conventional naming?                                                        |
| 24  | How is group of products for very simple object - relation mapping, called?                                                                                              |
| 25  | Can EF work with oracle?                                                                                                                                                 |
| 26  | If comparison with ignored casing is needed, how to atchieve it in EF?                                                                                                   |
| 27  | What are two main EF objects, that represent session with DB? (both are alternatives)                                                                                    |
| 28  | How DbSet Find method works                                                                                                                                              |
| 29  | In ObjectContext if you want to delete or modify item, how do you mark context about the change?                                                                         |
| 30  | If stored procedure for geting, modifying or deleting is attached to entity, how do you call it - explicitly or automatically together with savechanges call?            |
| 31  | When procedure is called, what is mapped to entity properties?                                                                                                           |
| 32  | What are two types of loading, that can be used?                                                                                                                         |
| 33  | How vertical splitting is done (when two db tables are mapped to one entity)                                                                                             |
| 34  | How horiontal splitting is done (two tables are represented in one entity)?                                                                                              |
| 35  | How do you configure lazy loading?                                                                                                                                       |
| 36  | If lazy loading is turned off, and you want second entity to be not null, what can you do?                                                                               |
| 37  | If you need exctract address fields to separate entity, what is the first step?                                                                                          |
