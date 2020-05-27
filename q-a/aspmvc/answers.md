# ASP.Net MVC answers

| #   | Answer                                                                                                                                                      |
| :-- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Async actions                                                                                                                                               |
| 2   | Not useful for single request execution time. Useful for highly loaded server, because threads are freed up on long operations, while waiting for response. |
| 3   | Some kind of attribute (which may be added to action method statically)                                                                                     |
| 4   | IModelBinder                                                                                                                                                |
| 5   | Url.Action                                                                                                                                                  |
| 6   | http                                                                                                                                                        |
| 7   | Html.Action                                                                                                                                                 |
| 8   | Html Helpers                                                                                                                                                |
| 9   | Render view, Http status, Json data, Custom action result.                                                                                                  |
| 10  | Outputs a string                                                                                                                                            |
| 11  | Routing data, qs parameter, form parameter.                                                                                                                 |
| 12  | Yes                                                                                                                                                         |
| 13  | Routing data, qs parameter, form parameter.                                                                                                                 |
| 14  | Call RedirectToAction method, or simple Redirect method.                                                                                                    |
| 15  | Both                                                                                                                                                        |
| 16  | Web config                                                                                                                                                  |
| 17  | if ModelState.IsValid                                                                                                                                       |
| 18  | Collection of data annotation validation errors.                                                                                                            |
| 19  | Validation html helpers display errors from ModelState.                                                                                                     |
| 20  | Inputs have data attributes. Jquery lib takes care.                                                                                                         |
| 21  | @                                                                                                                                                           |
| 22  | @@                                                                                                                                                          |
| 23  | @()                                                                                                                                                         |
| 24  | between text tags                                                                                                                                           |
| 25  | Html helper Html.Raw                                                                                                                                        |
| 26  | @model                                                                                                                                                      |
| 27  | @using                                                                                                                                                      |
| 28  | Render outputs to response. Partial returns string.                                                                                                         |
| 29  | if (IsSectionDefined("a")) { } else { default content }                                                                                                     |
| 30  | @section {}                                                                                                                                                 |
| 31  | Before any view processing begins.                                                                                                                          |
| 32  | Subfolders override parent                                                                                                                                  |
| 33  | Web config                                                                                                                                                  |
| 34  | Before and after action execution.                                                                                                                          |
| 35  | Action method, controller, global.                                                                                                                          |
| 36  | Exceptions, Authorization, Caching                                                                                                                          |
| 37  | Renderaction or Action html helpers.                                                                                                                        |
| 38  | RenderAction outputs directly to response, Action just returns string.                                                                                      |
| 39  | both                                                                                                                                                        |
| 40  | Separate                                                                                                                                                    |
| 41  | Yes                                                                                                                                                         |
| 42  | Implement IClientSideValidation, jquery Validate and unobtrusive adapter.                                                                                   |
| 43  | Remote attribute with specified action and controller for server side validation.                                                                           |
| 44  | Abstraction of all IoC frameworks.                                                                                                                          |
| 45  | Implement custom IDependencyResolver and set it on startup.                                                                                                 |
| 46  | Yes                                                                                                                                                         |
| 47  | Code generating                                                                                                                                             |
