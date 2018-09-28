# Contributing guide

## Basic definitions 
As with all projects, its important we define some key tersm in order to create a more effective and cohesive communication language.
**Tightly Bound Development:** All parts of a project that requires specific and well communicated knowledge of the code's architecture. This generally refers to more complicated and layered parts of a code base.
**Loosely Bound Development:** Areas of a project which are highly isolated. Changes in these parts are unlikely to create problems in other parts of the code base.
**Language Spec:** The direct design specifications of a language. This is a theoretical component of develpment. The language spec should be written into documents and explicitly sepcify the desired behviour of a language based on certain situations. The language spec is essentially the rules a language should follow.
**Language Grammar:** The semantic rules for a language. The grammar is the defined set of conventions and symbols used to actually write code in a given language. An example of something that would be defined in the grammar is: 
```python
# The following are to be considered termination statements
(';',               TERM_CODE),
('\n',              TERM_COMMENT),
('}',               TERM_SCOPE),
```
**SemVer:** The versioning standard most commonly found in ope source projects. [SemVer](https://semver.org/)
**REPL:** Read-Evaluate-Print-Loop. This refers to an interactive shell used to communicate with a program. An example of a REPL is command prompt.

## Devlopment Branches
There are two main branches of development for LDD. LDD Core and LDD Standard Library. The core regards to any development which actually implements the language. It includes the development of the Lexer, Parser, Evaluator and REPL. This is where the spec and grammar of the language are implemented and behaviour is defined. This can be though of as tightly bound development and can constitute changes to all MAJOR.MINOR.PATCH-label changes to the SemVer tag. The standard library branch is strictly for spec independant development. This is where all the low lying fruit is (aka. the easy stuff). The standard library is  the collection of code which can be called by default (things like 'print',  'read_file' and 'random_number' should be implemented here. The standard library can be written in platform native code (Python) or in LDD. For more info read 'Development Strategy' below.

## Making changes and adding features
Each devlopment branch has slightly different rules for contributing. 'ldd_core' has much more sensitive requirments than 'ldd_stdlib' as the core is much more complex and reactive to changes. This being said their respective rules are as follows:
### ldd_core
1. All changes must be made on a separate sub branch
2. Every update must go through a pull request
3. This branch must only be merged with the master if all new features are complete and fully implemented
4. Releases made from this branch should have the appropriate SemVer version as well as an appended label with the branch name. eg; v1.3.11-ldd_core-a1.2 (where the'a' means alpha and the 1.2 is the MINOR.PATCH version of that branch)
5. No changes are to be made to the stdlib on this branch. If changes are necessary they must be pulled from the 'ldd_stdlib' branch.
### ldd_stdlib
1. Changes can occur directly on this branch. No pull request necessary
2. This branch should never be merged directly to master. It may only be merged with ldd_core.
3. Releases must not be made from this branch
4. No changes are to be made to the core functionality on this branch. Furthermore, no changes should be made to the spec or grammar either.
