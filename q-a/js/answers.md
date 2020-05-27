# Javascript answers

| #   | Answer                                                                                                                                                               |
| :-- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Neither. Leave empty, style with css and use unobtrusive javascript techniques (like jquery event) to attach handler                                                 |
| 2   | If body uses something (like onclick handlers), this needs to be declared in the head                                                                                |
| 3   | Packaging web apps. NuGet analogy.                                                                                                                                   |
| 4   | Minifying, linting, compiling web app code. Like MS Build or in some way VS compilator.                                                                              |
| 5   | Generating (scaffholding) sample web app                                                                                                                             |
| 6   | No                                                                                                                                                                   |
| 7   | Yes                                                                                                                                                                  |
| 8   | onbeforeunload handler can only set message                                                                                                                          |
| 9   | Make GetHandler function and use closures                                                                                                                            |
| 10  | Does not do type converting                                                                                                                                          |
| 11  | undefined                                                                                                                                                            |
| 12  | Type error                                                                                                                                                           |
| 13  | Member A is appended                                                                                                                                                 |
| 14  | If val does not exist                                                                                                                                                |
| 15  | Never                                                                                                                                                                |
| 16  | Yes                                                                                                                                                                  |
| 17  | typeof o.A                                                                                                                                                           |
| 18  | o.hasOwnProperty('A')                                                                                                                                                |
| 19  | delete o.A                                                                                                                                                           |
| 20  | No                                                                                                                                                                   |
| 21  | delete o.A                                                                                                                                                           |
| 22  | Functions can be called                                                                                                                                              |
| 23  | No error - others will be ignored                                                                                                                                    |
| 24  | No error - undefined will be assigned for missing ones                                                                                                               |
| 25  | When its is called o.Func()                                                                                                                                          |
| 26  | Function scope                                                                                                                                                       |
| 27  | Never                                                                                                                                                                |
| 28  | No prototype link is hidden                                                                                                                                          |
| 29  | o                                                                                                                                                                    |
| 30  | global object                                                                                                                                                        |
| 31  | var o = new A();                                                                                                                                                     |
| 32  | this.newProp inside constructor function                                                                                                                             |
| 33  | ConstructorFuncName.prototype.newFunc = function() {...} outside constructor func                                                                                    |
| 34  | 1. When you need to specify what is "this" inside function 2. When you have array of args                                                                            |
| 35  | obj.meth.apply(thisObj, [array of args])                                                                                                                             |
| 36  | try catch throw                                                                                                                                                      |
| 37  | Maker func, which returns object with functions. Private var is inside maker func.                                                                                   |
| 38  | var o = makerFunction();                                                                                                                                             |
| 39  | Inherits prototypically new obj from A.prototype and executes A                                                                                                      |
| 41  | Make empty constructor function F, set F.prototype = o, return new F();                                                                                              |
| 42  | In hierarchy objects have same prototypical links.                                                                                                                   |
| 43  | Without                                                                                                                                                              |
| 44  | With                                                                                                                                                                 |
| 45  | Members of function                                                                                                                                                  |
| 46  | Members of returned "that" object                                                                                                                                    |
| 47  | Yes                                                                                                                                                                  |
| 48  | for in may change order                                                                                                                                              |
| 49  | Property does not exist                                                                                                                                              |
| 50  | Property exists and its value is empty object                                                                                                                        |
| 51  | Number value is not a number (i.e. parse unsuccessfull)                                                                                                              |
| 52  | Yes                                                                                                                                                                  |
| 53  | string and function. string should be avoided                                                                                                                        |
| 54  | Useless operator, that should be avoided                                                                                                                             |
| 55  | jslint.com                                                                                                                                                           |
| 56  | JSON.parse from json parser lib                                                                                                                                      |
| 57  | Douglas Crockford's minifier                                                                                                                                         |
| 58  | console.log(); write empty object & func                                                                                                                             |
| 59  | F-ion, which should be used as construction f-ion, property. f.prototype = A. If object b is constructed (b = new f()), b will have prototypical inheritance from A. |
| 60  | this[obj] === undefined                                                                                                                                              |
| 61  | Because it (like http redirect) does not put current url into history                                                                                                |
| 62  | var obj = {}; obj[“key”] = value;                                                                                                                                    |
| 63  | if (window['objName'])                                                                                                                                               |
| 64  | if (elem.createTextRange !== undefined && typeof (elem.createTextRange) === "function")                                                                              |
| 65  | If display none, IE8 and maybe lower ones will return nonsense value with this call                                                                                  |
| 66  | Delete won't remove the element from the array it will only set the element as undefined.                                                                            |
| 67  | window.open( params                                                                                                                                                  |
| 68  | Window.open returned - handle.document.title                                                                                                                         |
| 69  | Window.open returned - handle.document.write()                                                                                                                       |
| 70  | Window.open returned - handle.document dynamic head section maniputalion - add style element.                                                                        |
| 71  | JQuery create standalone element, set html, take text.                                                                                                               |
| 72  | There is no timezone info in a Date object.                                                                                                                          |
| 73  | document.querySelector and document.querySelectorAll                                                                                                                 |
| 74  | Javascript behaviour to move all declarations (but not initializations) to the top of the scope                                                                      |
| 75  | console.dir                                                                                                                                                          |
| 76  | In global functions (they are methods of window object)                                                                                                              |
| 77  | When calling object method (object was created with new and method was defined by constructor func.prototype.method =...)                                            |
| 78  | You can call function and pass the value as "this" as a first parameter                                                                                              |
| 79  | Apply expects array, call expects comma separated values                                                                                                             |
| 80  | Javascript compiler ES6 -> Javascript                                                                                                                                |
| 81  | Applies this to be what was passed (for later, when function is executed)                                                                                            |
| 82  | Stricter javascript syntax mode, introduced in ES5                                                                                                                   |
| 83  | Runs through properties                                                                                                                                              |
| 84  | if hasOwnProperty                                                                                                                                                    |
| 85  | Array                                                                                                                                                                |
| 86  | Function to handle each item                                                                                                                                         |
| 87  | Cannot be broken                                                                                                                                                     |
