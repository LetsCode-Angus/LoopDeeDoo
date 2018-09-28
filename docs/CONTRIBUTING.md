# Contributing guide
***
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

## Development Branches
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

## Reporting bugs and suggesting features
To report bugs (that you are not capable of personally fixing) you can use the github issues feature for this repo. Simply navigate to the home page of this repo and select the 'issues' tab. You will then be presented with a number of pre-configured issue templates. These inlude feature requests and bug reports. These templates have a number of suggested details which would be useful to be inlcluded (they are not mandatory though).

## Documentation
When collaborating on a project, communication of ideas is essential. This inlcudes explaining how features work. The two develpment bracnhes, again, have differing needs for documentation.
### ldd_core
The core should have at least one paragraph of high level documentation per module. Comments in code should be limited except for complicated areas which require small explanations for easier interpretation. If a module handles particularly critical functionalilty, it should have a much more in-depth explanation.
### ldd_stdlib
Every 'module' in the stdlib should have a docstring desribing its functionalilty. Comments should not be necessary in code as the docstring and clean coding techniques should be sufficient to explain inner logic.

## Language Spec and Grammar
The language spec and grammar should be defined in the `root/docs/spec/` folder and should be recorded in markdown format. The spec for the ldd_core should define intended language behaviour. The grammar only applies to the ldd_core and should describe the actully notation used to write code. It should list reserved keywords and their meaning. The spec for the stdlib should inlcude explanations for all of the functions found inside and demonstrate examples of expected outputs.

## Semantic Versioning
Semantic versioning is the most common versioning scheme in use today. It can be described in a few simple rules:
1. Each version should take the form MAJOR.MINOR.PATCH-label
    - MAJOR: The major version. This should only be incremented if the version is not backwards compatible with previous verions. Eg; adding a new keyword.
    - MINOR: The minor version. This should be incremented for new features and backwards compatible updates. Eg; adding some new stdlib functions.
    - PATCH: The patch number. This should be incremented for backwards compatible bug fixes. Eg; fixing a typo in an error message.
    - Label: An optional parameter to specify more info. Eg; v0.1.16-alpha.1
2. The major version should be incremented by a maximum of 1 at a time
3. Major version v0 is reserved for inital development. Any version after v0 is considered stable.

In order to keep track of changes made between versions we should use the github project boards. Here we can record notes on any changes made in order to ensure accurate versioning.

## Style guide
In larger scale projects style guides and coding conventions can be useful, however at this early stage in develpment, a style guide may be unecessary.

## Development strategy
The development strategy is the intended goals for the project alongside any additional notes involving methods of development. The current strategy is relatively simple.
1. Finish the key functionalitly of ldd_core.Lexer, ldd_core.Parser, ldd_core.Evaluator
2. Develop a standard library in parallel using a simple plug and play format
   - Ideally the standard library can just be a collection of python files which have functions in them.

All features and ideas should be recorded in the Roadmap project board.
