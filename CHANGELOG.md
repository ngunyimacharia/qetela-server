# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]

### Added
- Goals model, seeds, queries and tests
- Goal allocations model, seeds, queries and tests
- Kpis model, seeds, queries and tests
- Kpi updates model, seeds, queries and tests
- Chats model, seeds, queries and tests
- Messages model, seeds, queries and tests

### Changed
- Organisation seeder to only seed one organisation
- Seed command now takes argument for app to be seeded

### Fixed
- Changed name of organisation seeder from organisastions to organisations

## 0.0.2 - 2019-03-02

### Added
 - Team model, seeds, queries, mutations and tests
 - Level model, seeds, queries, mutations and tests
 - Position model, seeds, queries, mutations and tests
 - Account queries, mutations and tests complete
 - UserPosition model, seeder and test created
 - JWT Authentication added


## 0.0.1 - 2019-02-18

### Added
 - Organisation app created and added to admin
 - GraphQL integrated
 - GraphQL Queries and mutations for organisation CRUD implemented
 - MongoDB integrated
 - Seeder command created and implemented for organisation model
 - Added requirements.txt
 - Coverage integrated to show test coverage
 - Jenkins integrated

## 0.0.0 - 2019-02-12

### Added
- CHANGELOG.md added to project
- .gitignore file to ignore unecessary files
- Initial migration files generated
- Accounts app created and added
- README.md initialized
- License added

[Unreleased]: https://github.com/ngunyimacharia/qetela-server/compare/v0.0.2...HEAD
[0.0.2]: https://github.com/ngunyimacharia/qetela-server/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/ngunyimacharia/qetela-server/compare/v0.0.0...v0.0.1
