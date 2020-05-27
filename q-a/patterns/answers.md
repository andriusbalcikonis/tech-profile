# Patterns answers

| #   | Answer                                                                                                                                                       |
| :-- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Have a existing class hierarchy. Append them all with accept(Visitor) method. Now everything can be extended implementing visitors as needed.                |
| 2   | Memento                                                                                                                                                      |
| 3   | Mediator                                                                                                                                                     |
| 4   | State                                                                                                                                                        |
| 5   | Template method                                                                                                                                              |
| 6   | Abstract factory - concrete factory creates needed objects. BBuilder - Builder provides sets of methods. Director may call them in any combination           |
| 7   | Get it through Dependency Injection framework.                                                                                                               |
| 8   | Creating one of implementations by random                                                                                                                    |
| 9   | Observer                                                                                                                                                     |
| 10  | Strategy                                                                                                                                                     |
| 11  | 1                                                                                                                                                            |
| 12  | Log actions to xml file. Accept the same syntax in script runner.                                                                                            |
| 13  | Cannot extract interface                                                                                                                                     |
| 14  | For Dependency Injection pattern                                                                                                                             |
| 15  | For libraries, when you need to resolve only factory, and it makes all other implementations                                                                 |
| 16  | Private constructor                                                                                                                                          |
| 17  | Facade                                                                                                                                                       |
| 18  | Decorator                                                                                                                                                    |
| 19  | Can be virtual                                                                                                                                               |
| 20  | Factory abstract class, which creates all needed library objects                                                                                             |
| 21  | Builder                                                                                                                                                      |
| 22  | Director calls builder's methods to produce product.                                                                                                         |
| 23  | When factory method returns one of abstract class concrete implementations depending on runtime conditions                                                   |
| 24  | Load only when smth is needed for the first time.                                                                                                            |
| 25  | Global dictionary of singletons.                                                                                                                             |
| 26  | Connection pool                                                                                                                                              |
| 27  | Have prototype instance. Create objects by copying it.                                                                                                       |
| 28  | Adapter implements IA, but recalls IB implementation object.                                                                                                 |
| 29  | Object hierarchy (parent and children props)                                                                                                                 |
| 30  | Large numbers of object instances                                                                                                                            |
| 31  | Sharing as many properties as possible                                                                                                                       |
| 32  | Policy injection                                                                                                                                             |
| 33  | Many processors handle the operation. They each decide what to do with it - handle, or pass control to next processor (each processor has reference to next) |
| 34  | Undo                                                                                                                                                         |
| 35  | Queuing and logging                                                                                                                                          |
| 36  | Object for each UI command.                                                                                                                                  |
| 37  | Text in custom language as an input, parsing and executing it.                                                                                               |
| 38  | When method cannot do what its name promises it can do                                                                                                       |
| 39  | For performance. Example: user rights cached for whole session.                                                                                              |
| 40  | No                                                                                                                                                           |
| 41  | Point from which arrived, Currently Shortest Path                                                                                                            |
| 42  | Checked point with minimum path.                                                                                                                             |
| 43  | Sorted list                                                                                                                                                  |
| 44  | Yes, sort it if element was not found.                                                                                                                       |
| 45  | Recursively sort two parts of list and merge-join them.                                                                                                      |
| 46  | Tests cannot intercept static method calls to dependent parts of the system to fake them.                                                                    |
| 47  | Global state cannot be controlled by the tests                                                                                                               |
| 48  | Hard to create mocks. Factory pattern is better in those scenarios.                                                                                          |
| 49  | Restricts ability to pass faked dependencies in unit tests. Use dependency resolving instead.                                                                |
