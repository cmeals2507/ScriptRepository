======================
DATABASE SCHEMA DESIGN
======================

Purpose
-------
* 

Tables
------
* Composers
* Demographics
* Ensembles
* Seasons
* Works

Composers
---------
* [ ] Composer ID - PK - first name, last name, alias
* [ ] First name
* [ ] Last name / family name
* [ ] Suffix
* [ ] Pseudonym / pen name / alias
* [x] Living status
* [ ] Year died
* [x] Demographic code - FK
* [ ] Pronouns
* [ ] City
* [ ] State
* [ ] Country
* [ ] Website

Demographics
------------
* [x] Code - PK - [1, 2, 3, 4, 5, 6]
* [ ] Gender identity - [male, female, intersex, non-binary, transgender, etc.]
* [ ] Racial identity - [white, black, asian, etc.]


Ensembles
----------
* [ ] Ensemble ID - PK - ensemble name
* [x] Ensemble name
* [x] LAO group
* [ ] City
* [ ] State
* [ ] Operating budget

Artistic Admin
--------------
* [ ] Admin ID - PK - season, ensemble, conductor, artistic director, composer in residence
* [ ] Season - FK
* [ ] Ensemble - FK
* [ ] Conductor
* [ ] Artistic director
* [ ] Composer in residence
* [ ] Conductor code - FK (demographic code)
* [ ] Artistic director code - FK (demographic code)
* [ ] Composer in residence code - FK (demographic code)


Programs
--------
* [ ] Program ID - PK - season, ensemble, work, date of performance
* [ ] Season
* [x] Ensemble - FK
* [x] Work - FK
* [x] Composer - FK
* [x] Arranger - FK
* [ ] Date of performance

Works
-----
* [ ] Work ID - PK - title, composer, (arranger)
* [x] Title
* [x] Composer ID - FK
* [x] Arranger - FK (composer ID)
* [ ] Ensemble size - [chamber, string, symphonic]
* [ ] Duration
* [ ] Instrumentation
* [ ] Year composed
* [ ] Year premiered
* [ ] Ensemble premiered - FK (ensemble ID)