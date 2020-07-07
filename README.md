# Andrius Balčikonis

I am a software developer based in Vilnius, Lithuania. I am working in software development since 2005.

This is a summary of technologies and practices I am familiar with and my technical notes.

## Roles

Tech lead (2016-2020):

- Performing daily code reviews
- Tech discussions with architects and other teams
- Documenting the architecture
- Holding career meetings & job interviews
- Introducing and supporting new team memebers

Devops (2016-2020):

- CI/CD setup
- Performance testing and tuning
- Preparing deployment plans, performing deployments
- Setting up new environments in cooperation with ops.

Senior developer (2014-2020):

- Building systems from scratch
- Rewriting systems
- Refactoring major parts

Scrum master / technical project manager (2014-2020):

- Setting and documenting the development process (git process, jira workflow, sprint goals, measurements, retro notes)
- Arranging and holding scrum meetings (weekly/bi-weekly sprint planning calls - review, demo, planning, retrospective, backlog grooming sessions, daily devs discussions & daily scrum)
- Plan preparation with service owners and product owners (goals, schedule, versions, tickets)
- Performing feature demonstrations, other presentations
- Making sure there is always clear work and priorities for everyone in the team

Developer (2005-2014):

- Doing development tasks
- Participating in system design discussions with team

System analyst (2005-2007):

- Discussing & collecting requirements with clients
- Documenting requirements

## Technologies

| Category             | Level | Technology           | POC (templates / experiments)  | Notes                                              |
| :------------------- | :---- | :------------------- | :----------------------------- | :------------------------------------------------- |
| **FRONTEND**         |       |                      |                                |                                                    |
| Styling              | `**`  | HTML+CSS/SASS        |                                | [Q&A: html&css](q-a/html-css)                      |
|                      | `**`  | Bootstrap            | [bootstrap](poc/bootstrap)     |                                                    |
| Languages            | `**`  | Javascript           |                                | [Q&A: js](q-a/js)                                  |
|                      | `***` | Javascript (ES6)     | (in many POCs)                 | [Q&A: es6](q-a/es6)                                |
|                      | `**`  | Typescript           |                                | [Q&A: typescript](q-a/typescript)                  |
| App frameworks       | `***` | React + Flux/Redux   | [fullstack-1](poc/fullstack/1) |                                                    |
|                      | `*`   | Vue+Vuex `P1`        |                                |                                                    |
| Libraries            | `**`  | jQuery               |                                |                                                    |
|                      | `*`   | RxJS                 |                                |                                                    |
| Tools                | `**`  | Webpack              | [fullstack-1](poc/fullstack/1) |                                                    |
|                      | `**`  | ESLint               |                                |                                                    |
|                      | `**`  | Bower + Grunt/Gulp   |                                |                                                    |
|                      | `**`  | NPM                  |                                |                                                    |
|                      | `*`   | Yarn                 |                                |                                                    |
| Site generators      | `*`   | NextJS               | [nextjs](poc/nextjs)           |                                                    |
| **BACKEND (PYTHON)** |       |                      |                                |                                                    |
| Langauge             | `***` | Python               | (in many POCs)                 | Python: [Notes](notes/python.md) [Q&A](q-a/python) |
| App frameworks       | `***` | Bottle               |                                |                                                    |
|                      | `**`  | Flask                | [fullstack-1](poc/fullstack/1) |                                                    |
|                      | `*`   | Django               |                                |                                                    |
| ORMs & migration     | `**`  | SqlAlchemy           | [fullstack-1](poc/fullstack/1) |                                                    |
|                      | `*`   | Alembic `P2`         |                                |                                                    |
|                      | `*`   | DjangoORM            |                                |                                                    |
| REST API             | `*`   | FlaskRest            |                                |                                                    |
|                      | `*`   | Schematics `P2`      |                                |                                                    |
|                      | `*`   | DjangoREST           |                                |                                                    |
| GraphQL API          | `*`   | Graphene             |                                |                                                    |
| Async tasks          | `*`   | Celery + RabbitMQ    | [fullstack-1](poc/fullstack/1) |                                                    |
| Queue                | `*`   | pika + RabbitMQ      | [fullstack-1](poc/fullstack/1) |                                                    |
| Web server setup     | `**`  | nginx + uwsgi        | [uwsgi-nginx](poc/uwsgi-nginx) | [Q&A: rev-proxy](q-a/rev-proxy)                    |
| **BACKEND (.NET)**   |       |                      |                                |                                                    |
| .Net                 | `**`  | .Net                 |                                | [Q&A: .net](q-a/dotnet)                            |
|                      | `**`  | C#                   |                                | [Q&A: c#](q-a/csharp)                              |
|                      | `**`  | ASP.Net WebForms     |                                | [Q&A: asp.net wf](q-a/wf)                          |
|                      | `**`  | ASP.Net MVC          |                                | [Q&A: asp.net mvc](q-a/aspmvc)                     |
|                      | `**`  | Entity Framework ORM |                                | [Q&A: ef](q-a/ef)                                  |
|                      | `*`   | Xml                  |                                | [Q&A: xml](q-a/xml)                                |
|                      | `*`   | WCF                  |                                | [Q&A: wcf](q-a/wcf)                                |
|                      | `*`   | IIS                  |                                | [Q&A: iis](q-a/iis)                                |
|                      | `*`   | Active directory     |                                | [Q&A: activedir](q-a/activedir)                    |
|                      | `*`   | .Net Core On Linux   |                                | [Notes: netcore](notes/netcore.md)                 |
| **DATABASES**        |       |                      |                                |                                                    |
| Relational           | `*`   | PostgreSQL           | [3dbs](poc/3dbs)               |                                                    |
|                      | `*`   | MySQL                |                                |                                                    |
|                      | `**`  | MS SQL Server        |                                | [Q&A: mssql](q-a/mssql)                            |
| NoSQL                | `**`  | Redis                | [3dbs](poc/3dbs)               |                                                    |
|                      | `*`   | MongoDB              | [3dbs](poc/3dbs)               |                                                    |
|                      | `*`   | Other noSQL DBs      |                                | [Q&A: nosql](q-a/nosql)                            |
| Search engines       | `*`   | Elastic search       |                                |                                                    |
| **OTHER DEV**        |       |                      |                                |                                                    |
| Version control      | `**`  | Git                  |                                | [Notes: git](notes/git.md)                         |
| Selenium tests       | `**`  | Robot framework      | [robots](poc/robots)           |                                                    |
| Authentication       | `**`  | OAuth, JWT           |                                |                                                    |
| Regexp               | `**`  | Regexp               |                                | [Q&A: regexp](q-a/regexp)                          |
| **DEVOPS**           |       |                      |                                |                                                    |
| Tools                | `**`  | Docker               | (in many POCs)                 | [Notes: docker](notes/docker.md)                   |
|                      | `**`  | Docker-compose       | (in many POCs)                 | [Notes: docker](notes/docker.md)                   |
|                      | `*`   | Helm `P2`            |                                |                                                    |
|                      | `**`  | Kubernetes           |                                | [Notes: kubectl](notes/kubectl.md)                 |
|                      | `**`  | Bash                 |                                | [Notes: bash](notes/bash.md)                       |
| CI/CD systems        | `***` | GitLab CI            |                                |                                                    |
|                      | `**`  | Jenkins              |                                |                                                    |
|                      | `*`   | Travis CI            |                                |                                                    |
| Monitoring           | `**`  | NewRelic             |                                |                                                    |
|                      | `**`  | Graylog              |                                |                                                    |
|                      | `*`   | Sentry               |                                |                                                    |
|                      | `*`   | Graphana & influxdb  | [grafana](poc/grafana)         |                                                    |
|                      | `*`   | Google analytics     |                                |                                                    |
| Perofmance testing   | `**`  | Locust               | [perf-tests](poc/perf-tests)   |                                                    |
| Operations           | `**`  | Operations           |                                | [Q&A: ops](q-a/ops)                                |

Notation:

- `***` I know it well, no additional studying would be needed (studied in detail / used in real projects recently)
- `**` Some studying/refreshing may be needed (studied it / used in real projects a while ago)
- `*` Studying would be needed (I know _why_ and _when_ it should be used, but not much about the details of _how_)
- `PN` TODO to study more with prio N

## Best practices

| Category         | Level | Practice (tools used)                                        | POC (templates / experiments)      | Notes                                  |
| :--------------- | :---- | :----------------------------------------------------------- | :--------------------------------- | :------------------------------------- |
| **ENVS & CI/CD** |       |                                                              |                                    |                                        |
| Local env        | `***` | One-liner startup (`docker-compose`, `make`)                 | (in many POCs)                     |                                        |
|                  | `***` | Makefiles to manage package installs (`make`)                |                                    |                                        |
|                  | `**`  | Prod-like dev env (`docker`)                                 |                                    |                                        |
|                  | `**`  | Convenient way to reload (`webpack hot-reload`)              |                                    |                                        |
|                  | `**`  | Convenient way to debug (IDE in-line debugger, source-maps)  | [pdb-in-docker](poc/pdb-in-docker) |                                        |
| CI & local env   | `***` | Unit tests ( `jest`, `pytest` )                              |                                    |                                        |
|                  | `***` | Enforced code style - linters (`eslint`, `flake8` )          | [fullstack-1](poc/fullstack/1)     |                                        |
|                  | `***` | Enforced code style - formatters (`prettier`, `black`)       |                                    |                                        |
|                  | `**`  | Code complexity checks `flake8` with param `max-complexity`  | [fullstack-1](poc/fullstack/1)     |                                        |
|                  | `***` | Test coverage (`pytest-cov` with param `fail_under`)         |                                    |                                        |
|                  | `***` | Static security checks (`npm audit`, `snyk`, `bandit`)       |                                    |                                        |
| CI               | `***` | CI runs not only on commit, but also nightly                 |                                    |                                        |
|                  | `*`   | Dynamic security tests (`OWASP ZAP`)                         |                                    |                                        |
|                  | `***` | Integration tests (`robot-framework with selenium2`)         | [robots](poc/robots)               |                                        |
|                  | `***` | Prealpha environment for smoke testing before alpha          |                                    |                                        |
|                  | `?`   | Automated memory leak checks                                 | [memory-leaks](poc/mem-leaks)      |                                        |
|                  | `?`   | Ensuring clean error log during integration tests            |                                    |                                        |
|                  | `?`   | Performance measurements during integration tests            |                                    |                                        |
| CD               | `***` | Keep track of deployed envs automatically (`GitLab CI` envs) |                                    |                                        |
|                  | `*`   | Pre-deploy dependency checks                                 |                                    |                                        |
|                  | `***` | After-deploy version checks                                  |                                    |                                        |
|                  | `**`  | Auto-scaling (`kubernetes`)                                  |                                    |                                        |
|                  | `**`  | Rolling updates and avoided downtime (`kubernetes`)          |                                    |                                        |
|                  | `**`  | Liveness, readyness checks and auto-recovery (`kubernetes`)  |                                    |                                        |
| Monitoring       | `*`   | User usage metrics (`google-analytics`)                      |                                    |                                        |
|                  | `***` | Server performance & alerts (`new relic`)                    |                                    |                                        |
|                  | `**`  | Aggregated logs (`graylog`)                                  |                                    |                                        |
|                  | `*`   | Custom metrics (`grafana`)                                   | [grafana](poc/grafana)             |                                        |
|                  | `*`   | Incident tracker (`sentry`)                                  |                                    |                                        |
|                  | `?`   | Health/smoke tests with selenium in production               |                                    |                                        |
| **APP DESIGN**   |       |                                                              |                                    |                                        |
| Any web app      | `***` | General best practices of web                                |                                    | [Q&A: web](q-a/web)                    |
|                  | `***` | Extensive logging                                            |                                    | [Notes: logging](notes/logging.md)     |
|                  | `***` | Special endpoints (version, liveness & readyness)            |                                    | [Notes: endpoints](notes/endpoints.md) |
|                  | `***` | Stateless web app - external session and cache (`redis`)     |                                    |                                        |
|                  | `***` | Framework / abstract class to enforce dev consistancy        |                                    |                                        |
|                  | `***` | Mechanism to handle localizations properly                   |                                    | [Notes: intl](notes/intl.md)           |
|                  | `**`  | (If needed) Consistant way to access various contexts        |                                    | [Notes: contexts](notes/contexts.md)   |
|                  | `**`  | (If needed) Feature switches (possibly for some users only)  |                                    |                                        |
| Single page apps | `*`   | Collect frontend logs to server                              |                                    |                                        |
|                  | `**`  | Keep permission & workflow logic in one place (backend)      |                                    |                                        |
| API              | `**`  | Documentation + callable client (`OpenAPI (swagger)`)        | [swagger](poc/swagger)             |                                        |
|                  | `**`  | Strong input validation and clear messages                   |                                    |                                        |
| Library dev      | `**`  | Semantic versioning                                          |                                    |                                        |
|                  | `*`   | Strong typing lang/features (Python3 type hints + `mypy`)    |                                    |                                        |
|                  | `**`  | Change log / release notes                                   |                                    |                                        |
|                  | `**`  | Upgrade example / instructions for breaking changes          |                                    |                                        |
| DB design        | `*`   | Schema control even if no-sql does not enforce it            |                                    |                                        |
|                  | `*`   | Change scripts should go with migrations + rollback script   |                                    |                                        |
|                  | `*`   | Immutability (`event-sourcing`) or at least full audit       | [fullstack-1](poc/fullstack/1)     |                                        |
|                  | `*`   | Full audit (`temporal tables`) if not immutability           |                                    |                                        |
| User experience  | `**`  | Avoid heavily used sessions                                  |                                    |                                        |
|                  | `*`   | (If session used heavily) Session expiration handling        |                                    |                                        |
|                  | `**`  | Everything / many things should be accessible via url        |                                    |                                        |
|                  | `**`  | Consistant form validation mechanism                         |                                    |                                        |
|                  | `**`  | Consistant ajax loader mechanism                             |                                    |                                        |
| Design patterns  | `*`   | Design patterns                                              |                                    | [Q&A: patterns](q-a/patterns)          |
| Security         | `*`   | Best practices in security                                   |                                    | [Q&A: security](q-a/security)          |
| **DEV PROCESS**  |       |                                                              |                                    |                                        |
| Project-kickoff  | `***` | Define git-process                                           |                                    |                                        |
|                  | `***` | Task workflow (states)                                       |                                    |                                        |
|                  | `***` | Define definition of done                                    |                                    | [Notes: dod](notes/dod.md)             |
| Daily dev        | `***` | Commenting task merge request to the ticket (`GitLab` MRs)   |                                    |                                        |
|                  | `***` | Peer review is performed before merging (`GitLab` MRs)       |                                    | [Notes: reviews](notes/reviews.md)     |
|                  | `***` | Daily group review for knowledge sharing                     |                                    | [Notes: reviews](notes/reviews.md)     |
|                  | `**`  | Daily scrum                                                  |                                    |                                        |
|                  | `**`  | Continous delivery to alpha                                  |                                    |                                        |
|                  | `**`  | Marking external dependencies - in ticket and/or in code     |                                    |                                        |
|                  | `*`   | Tests for new functionality and for new bugs found           |                                    |                                        |
| Once in sprint   | `***` | Sprint review (overview, demo, feedback)                     |                                    |                                        |
|                  | `***` | Sprint planning (goals, schedule, versions, tickets)         |                                    |                                        |
|                  | `**`  | Backlog grooming and estimating                              |                                    |                                        |
|                  | `***` | Retrospective                                                |                                    | [Notes: retro](notes/retro.md)         |
| Before releases  | `***` | Arrange deployment freeze and regression testing in alpha    |                                    |                                        |
|                  | `***` | Collect approvals (CAB)                                      |                                    |                                        |
|                  | `***` | Release notes                                                |                                    | [Notes: docs](notes/docs.md)           |
|                  | `***` | (When needed) Deployment plan and it's approvals             |                                    |                                        |
|                  | `***` | (When needed) Technical documentation updates                |                                    |                                        |
|                  | `**`  | (When needed) Performance testing in beta                    | [perf-tests](poc/perf-tests)       |                                        |
|                  | `***` | (When needed) Security audit                                 |                                    |                                        |
|                  | `**`  | Other agile best practices                                   |                                    | [Q&A: agile](q-a/agile)                |
| Documentation    | `**`  | Technical documentation                                      |                                    | [Notes: docs](notes/docs.md)           |
|                  | `*`   | UML                                                          |                                    | [Q&A: uml](q-a/uml)                    |

Notation:

- `***` I have used it and would use in next projects
- `**` I have not used it, but willing to try in next projects
- `*` I have not used it and also have doubts if it is for every situation
- `?` Just an untested idea
