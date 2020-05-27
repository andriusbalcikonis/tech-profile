# C# & OOP answers

| #   | Answer                                                                                                                                                                             |
| :-- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | UI (or request) thread deadlock if task.Result is used instead of awaiting.                                                                                                        |
| 2   | You write return 1, but method return type is Task[int].                                                                                                                           |
| 3   | var t = A(); var result = await t;                                                                                                                                                 |
| 4   | No, it means, that compiler will rearange everything, if this method will be called in paralell with other avaitable methods                                                       |
| 5   | Thread starvation is possible, because running asynchroniously takes new threads from thread pool                                                                                  |
| 6   | Call it in Task.Run                                                                                                                                                                |
| 7   | Yes                                                                                                                                                                                |
| 8   | ?. which returns null if left side is null                                                                                                                                         |
| 9   | Lambda expressions for class methods instead of its body                                                                                                                           |
| 10  | Placeholders instead of string format                                                                                                                                              |
| 11  | Include them with "using" and call methods without specifying class.                                                                                                               |
| 12  | 2015                                                                                                                                                                               |
| 13  | 2015                                                                                                                                                                               |
| 14  | Constructor, initializers (like fields)                                                                                                                                            |
| 15  | Throws Exception if expression value is too big and would save it with an overflow.                                                                                                |
| 16  | ThreadStatic attribute for static members                                                                                                                                          |
| 17  | Unspecified number of parameters at the end of function                                                                                                                            |
| 18  | 1. GAC (for strongly named) 2. Web.conf specified locations 3. Running directory (i.e. bin)                                                                                        |
| 19  | Task[Type]                                                                                                                                                                         |
| 20  | Code readability and asynchronous programming                                                                                                                                      |
| 21  | Optional params                                                                                                                                                                    |
| 22  | Display                                                                                                                                                                            |
| 23  | Calls constructor only on property request, not in constructor call stack                                                                                                          |
| 24  | No                                                                                                                                                                                 |
| 25  | It is automatically rethrown in catch clause.                                                                                                                                      |
| 26  | The general rule to follow is that structs should be small, simple (one-level) collections of related properties, that are immutable once created; for anything else, use a class. |
| 27  | LambdaExpression                                                                                                                                                                   |
| 28  | C                                                                                                                                                                                  |
| 29  | Expression                                                                                                                                                                         |
| 30  | yes, 26K compilations - 7secs                                                                                                                                                      |
| 31  | Private fields                                                                                                                                                                     |
| 32  | Inheritance                                                                                                                                                                        |
| 33  | Interface, abstract or virtual method and implementation.                                                                                                                          |
| 34  | Yes                                                                                                                                                                                |
| 35  | Use Linq Where as an Example.                                                                                                                                                      |
| 36  | No, they are more advanced                                                                                                                                                         |
| 37  | To support LinqToSql Sql generation                                                                                                                                                |
| 38  | Instead of reflection, Xml, json access                                                                                                                                            |
| 39  | Events for which handler should be attached                                                                                                                                        |
| 40  | Code blocks in toolbox                                                                                                                                                             |
| 41  | Tracepoint                                                                                                                                                                         |
| 42  | Task                                                                                                                                                                               |
| 43  | Extension method                                                                                                                                                                   |
| 44  | Static class, this in front of params                                                                                                                                              |
| 45  | Serializable                                                                                                                                                                       |
| 46  | Binary and Xml                                                                                                                                                                     |
| 47  | XmlInclude                                                                                                                                                                         |
| 48  | Closure                                                                                                                                                                            |
| 49  | IDisposable                                                                                                                                                                        |
| 50  | When garbage collectror destroys object                                                                                                                                            |
| 51  | No                                                                                                                                                                                 |
| 52  | Const is static & type level. Readonly is class level and runtime field, that cannot be changed later.                                                                             |
| 53  | By object type                                                                                                                                                                     |
| 54  | By reference type                                                                                                                                                                  |
| 55  | Yes                                                                                                                                                                                |
| 56  | In class hierarchies, where objects should behave by their classification (references)                                                                                             |
| 57  | No difference                                                                                                                                                                      |
| 58  | Yes                                                                                                                                                                                |
| 59  | Last one                                                                                                                                                                           |
| 60  | Accept Interface with one method                                                                                                                                                   |
| 61  | Inside class events are delegates. Outside - can be accessed only by += -=                                                                                                         |
| 62  | Yes                                                                                                                                                                                |
| 63  | Binary, Xml, DataContract, custom                                                                                                                                                  |
| 64  | Constructor overload with setting                                                                                                                                                  |
| 65  | Automatically                                                                                                                                                                      |
| 66  | Include all types on constructor                                                                                                                                                   |
| 67  | Automatically                                                                                                                                                                      |
| 68  | Do not include, if value is default                                                                                                                                                |
| 69  | No                                                                                                                                                                                 |
| 70  | Add OnSerializing (or similar) attribute to method.                                                                                                                                |
| 71  | No                                                                                                                                                                                 |
| 72  | Special 3rd party libs for working with assemblies                                                                                                                                 |
| 73  | B                                                                                                                                                                                  |
| 74  | For strings and when number of items is not extremely huge                                                                                                                         |
| 75  | 1. B output path. 2. A reference to dll.                                                                                                                                           |
| 76  | C                                                                                                                                                                                  |
| 77  | B                                                                                                                                                                                  |
| 78  | ThradAbortException                                                                                                                                                                |
| 79  | inheritance hides overloads                                                                                                                                                        |
| 80  | write operator                                                                                                                                                                     |
| 81  | structs passed by value, not by reference                                                                                                                                          |
| 82  | For value types                                                                                                                                                                    |
| 83  | When method, that calls the dlls method is called                                                                                                                                  |
| 84  | xm file only                                                                                                                                                                       |
| 85  | compilation time                                                                                                                                                                   |
| 86  | GAC, local bin, additional places, if configured                                                                                                                                   |
| 87  | No for normal assemblies, yes for strongly named ones.                                                                                                                             |
| 88  | Only if file ref specific version attribute is true                                                                                                                                |
| 89  | No                                                                                                                                                                                 |
| 90  | Yes. Not too expensive                                                                                                                                                             |
| 91  | Delegate.CreateDelegate                                                                                                                                                            |
| 92  | () => {}                                                                                                                                                                           |
| 93  | Application, but if class is generic - then separate for each type                                                                                                                 |
| 94  | No                                                                                                                                                                                 |
| 95  | Yes                                                                                                                                                                                |
| 96  | A - reference type; B - parametreless constructor                                                                                                                                  |
| 97  | Yes it will execute                                                                                                                                                                |
| 98  | String is a Reference Type object.                                                                                                                                                 |
| 99  | We may call the garbage collector to collect unreferenced data by executing theSystem.GC.Collect() method.                                                                         |
| 100 | closest even (2, 4, ...) number, overloads                                                                                                                                         |
| 101 | usefull "IsIn" functionality                                                                                                                                                       |
| 102 | easy - throw;                                                                                                                                                                      |
| 103 | using(var n = new Obj())... Dispose will be called even if exception is thrown                                                                                                     |
| 104 | using win = System.Windows.Forms;                                                                                                                                                  |
| 105 | Expression[T]                                                                                                                                                                      |
| 106 | Const is static, readonly may be dynamically determined, but is frozen when ctror finishes its work                                                                                |
| 107 | 0.1 will loose, 0.5 not, because it is stored in binary format 01010.0101010                                                                                                       |
| 108 | String.Join(                                                                                                                                                                       |
| 109 | Yes                                                                                                                                                                                |
| 110 | Static field is available only at run time, const even at compile time                                                                                                             |
| 111 | Yes: FormatterServices.GetUninitializedObject                                                                                                                                      |
| 112 | No                                                                                                                                                                                 |
| 113 | Accept generic param                                                                                                                                                               |
| 114 | BigInteger                                                                                                                                                                         |
| 115 | Custom data type                                                                                                                                                                   |
| 116 | Class implementing IEnumerable                                                                                                                                                     |
| 117 | Yes                                                                                                                                                                                |
