# C# & OOP questions

| #   | Question                                                                                                                                                                                 |
| :-- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | What is a huge risk with async methods in asp.net apps or windows apps?                                                                                                                  |
| 2   | What is interesting feature about async methods return types?                                                                                                                            |
| 3   | If method A is asynch and returns Task[resulttype], how should you call and await it?                                                                                                    |
| 4   | Does making a wrapper async method (which returns Task[result]) means a new Thread will be created?                                                                                      |
| 5   | Why is it dangerous to use Task.Run in ASP.Net?                                                                                                                                          |
| 6   | If you need some long CPU bound function to be asynch (in other words awaitable), how do you do it.                                                                                      |
| 7   | Can ?. operator of c# v6 be used for event calls?                                                                                                                                        |
| 8   | What new operator is added to c# v6?                                                                                                                                                     |
| 9   | What new feature regarding lambdas is added to c# v6?                                                                                                                                    |
| 10  | What new feature regarding strings is added to c# v6?                                                                                                                                    |
| 11  | What is new c# v6 feature regarding static classes?                                                                                                                                      |
| 12  | What visual studio version has .net 4.6?                                                                                                                                                 |
| 13  | When c# v6 will be shipped (with which visual studio version)?                                                                                                                           |
| 14  | C# v6 has auto properties without setters. Where its value can be set?                                                                                                                   |
| 15  | What does "checked" keyword do?                                                                                                                                                          |
| 16  | Is there any context to store data separated for threads but static in the thread?                                                                                                       |
| 17  | c# keyword "params" - what is it for?                                                                                                                                                    |
| 18  | When searching for dependant dlls, where does .net framework searches it?                                                                                                                |
| 19  | What does asynch mechod usually return?                                                                                                                                                  |
| 20  | Asynch and await - what two nice things these keywords allow to be used?                                                                                                                 |
| 21  | What new c# feature regarding params is introduced in c# v4                                                                                                                              |
| 22  | DataAnnotations - what is DataType attribute (for example DataType=EmailAddress) for - display or validation?                                                                            |
| 23  | Lazy class - what does it do?                                                                                                                                                            |
| 24  | Is list[t] thread safe?                                                                                                                                                                  |
| 25  | How is ThreadAbortException different from all the others?                                                                                                                               |
| 26  | When is good idea to use struct instead of class?                                                                                                                                        |
| 27  | What is the class representing lambdas?                                                                                                                                                  |
| 28  | Are regions considered: A. Good practice B. Bad practice C. Opinions differ                                                                                                              |
| 29  | To write linq dynamically, what class static methods should be used?                                                                                                                     |
| 30  | Is lambda compilation an (relatively) expensive task?                                                                                                                                    |
| 31  | What is OOP feature for implementation hiding?                                                                                                                                           |
| 32  | What is OOP feature for reducing code duplication?                                                                                                                                       |
| 33  | What do you need for polymorphism to work?                                                                                                                                               |
| 34  | Does Linq support Joining two tables and grouping?                                                                                                                                       |
| 35  | How to make method, which expects lambda expression as parameter?                                                                                                                        |
| 36  | Are lambda expressions compiled the same as anonymous functions?                                                                                                                         |
| 37  | Why were .Net Expression trees created?                                                                                                                                                  |
| 38  | When dynamic programming is useful?                                                                                                                                                      |
| 39  | LinqToEvents (Rx Framework) - what are you quering with linq in this technology?                                                                                                         |
| 40  | What is VisualStudio 2010 improvement of code snippets?                                                                                                                                  |
| 41  | What new alternative to breakpoint was introduced in VS2010?                                                                                                                             |
| 42  | What class .Net 4.0 offers instead of Thread as higher abstraction?                                                                                                                      |
| 43  | What do you need to use, if you want to extend sealed class with new methods?                                                                                                            |
| 44  | How do you create extension method?                                                                                                                                                      |
| 45  | What one attribute must be added to class to support serialization?                                                                                                                      |
| 46  | What are two most common serialization formats?                                                                                                                                          |
| 47  | Which attribute must be used, if serialized object hierarchy uses "polymorphism"?                                                                                                        |
| 48  | How reference to context in which function was created is called?                                                                                                                        |
| 49  | What interface must object implement, so that it could be used in using() sentence?                                                                                                      |
| 50  | When does Finalize method is called of IFinalizable objects?                                                                                                                             |
| 51  | Is it recommended to use IFinalizable objects?                                                                                                                                           |
| 52  | What is the difference between const ant readonly?                                                                                                                                       |
| 53  | When prop is overriden, how implementation function is selected?                                                                                                                         |
| 54  | When prop hides other property, how implementation method is selected?                                                                                                                   |
| 55  | Can property, which hides other prop, have other type?                                                                                                                                   |
| 56  | Method hiding is almost never useful. Still, when could it be usefull?                                                                                                                   |
| 57  | B. var d = M;                                                                                                                                                                            |
| 58  | Can delegate have more than one method attached?                                                                                                                                         |
| 59  | If delegate has more than a one method attached, and methods have return value, which one is used?                                                                                       |
| 60  | We have a method, that accepts delegate as a parameter. What is alternative way to do the same (with only a few differences)?                                                            |
| 61  | What is the difference between event and delegate?                                                                                                                                       |
| 62  | Can ?? be used with reference types?                                                                                                                                                     |
| 63  | What four serialization frameworks are supported in .Net?                                                                                                                                |
| 64  | If preserving reference links and loops is needed, what is the way to do it with DataContractSerializer?                                                                                 |
| 65  | If preserving reference links and loops is needed, what is the way to do it with NetDataContractSerializer?                                                                              |
| 66  | If object graph contains inherited classes, what is the way to do serialization with DataContractSerializer?                                                                             |
| 67  | If object graph contains inherited classes, what is the way to do serialization with NetDataContractSerializer?                                                                          |
| 68  | In DataContract serialization, what does DataMemberAttr.EmitDefaultValue mean?                                                                                                           |
| 69  | In DataContract serialization (and probably others) - will deserializer call constructor and field initializers?                                                                         |
| 70  | In DataContract serialization, how can you add custom serialization, deserailization logic?                                                                                              |
| 71  | Can you extract comments through reflection?                                                                                                                                             |
| 72  | How can you extract comments at runtime?                                                                                                                                                 |
| 73  | B. All used classes in object graph?                                                                                                                                                     |
| 74  | Object.GetHashCode when it can be used?                                                                                                                                                  |
| 75  | Solution contains projet A, referencing project B the normal way. We want to change rererencing strategy, so that A would only reference dll of B. What two changes must be made.        |
| 76  | Math.round - will it round .5 A. upwards B. downwards C. sometimes upwards sometimes downwards?                                                                                          |
| 77  | What real number type needs to be used when operating with money (or in other scenarios, when calculations must be exact and expected)? A. double B. decimal                             |
| 78  | Do you know any Exception type, which is treated differently by .net in general and asp.net?                                                                                             |
| 79  | Why combination of overloading function with same number of params (A(int) A(object)) and inheritance is not good idea?                                                                  |
| 80  | How can you implement the casting - var a = (A)b; ?                                                                                                                                      |
| 81  | Name one important difference betweeen structs and classes, besides the facts, that structs are stored in stack, does not have to be garbage collected and does not support inheritance? |
| 82  | Name one example, when ref keyword may be useful?                                                                                                                                        |
| 83  | If you run app, it calls method in other dll, but dll does not exist, when exception will be thrown?                                                                                     |
| 84  | When dll is added to project as file ref, how can you check what version is expected - props window, xml file, or both?                                                                  |
| 85  | When project file reference property SpecificVersion is important - compilation time, runtime, or both?                                                                                  |
| 86  | What places are searched for needed dlls in runtime?                                                                                                                                     |
| 87  | Is specific dll version important at runtime?                                                                                                                                            |
| 88  | Is specific dll version important at compilation time?                                                                                                                                   |
| 89  | If extension method is called with null, will it throw null ref exception?                                                                                                               |
| 90  | If you create List passing enumerable, will it ask for each item immediately? Is it too expensive to be called on every request?                                                         |
| 91  | How to create delegate from string, specifying functions name?                                                                                                                           |
| 92  | How to create lambda value which returns void?                                                                                                                                           |
| 93  | If you have static field, in which context is data saved?                                                                                                                                |
| 94  | Can you use initializers for a list - initializing properties and list items at the same time?                                                                                           |
| 95  | IEnumerable[Interface] a = new List[Realization]();                                                                                                                                      |
| 96  | In generics, what do restictions mean: A: where T: class. B: where T : new()                                                                                                             |
| 97  | Will the finally block be executed if an exception has not occurred? Not caught? Caught?                                                                                                 |
| 98  | Is String a Reference Type or Value Type in .NET?                                                                                                                                        |
| 99  | How to instruct the garbage collector to collect unreferenced data?                                                                                                                      |
| 100 | What is the default Math.Round behaviour? Can you change that?                                                                                                                           |
| 101 | What does this extension method do?                                                                                                                                                      |
| 102 | which is right: throw ex; or throw; ?                                                                                                                                                    |
| 103 | If object implements IDisposible, how should you create it? Why?                                                                                                                         |
| 104 | Give an example of namepsace alias?                                                                                                                                                      |
| 105 | Which class is used for lambdas of specific delegate type T?                                                                                                                             |
| 106 | What is the biggest difference between readonly and const?                                                                                                                               |
| 107 | Will double or float value 0.1 (or 0.5) be stored without any loss of data? Why                                                                                                          |
| 108 | What .net class library method could be used to join strings with separator?                                                                                                             |
| 109 | Can object access private member of other object of the same class?                                                                                                                      |
| 110 | What is one diference between static readonly field and constant?                                                                                                                        |
| 111 | Can you create object without default constructor being called?                                                                                                                          |
| 112 | Will -= operator crash, if no handler is attached to event?                                                                                                                              |
| 113 | What is the only way to write function, which return anonymous type?                                                                                                                     |
| 114 | What immutable type is new in .Net 4?                                                                                                                                                    |
| 115 | Enum does not mean Enumerator. What is Enum?                                                                                                                                             |
| 116 | Enum does not mean Enumerator. What is Enumerator?                                                                                                                                       |
| 117 | Data Annotations - is there a way to show messages from resources?                                                                                                                       |
