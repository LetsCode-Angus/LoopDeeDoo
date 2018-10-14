# LoopDeeDoo
The central development repo for the LoopDeeDoo language.
***
LoopDeeDoo aims to be the dumbest, most ridiculous proramming language on the scene. The entire language centers around its looping mechanic which works by calling `loop dee doo ("some string of characters")`. The loop runs for every letter in the provided string. This mechanic, whilst stupid, has some unintended and almost smart side effects. If we wanted to loop over every character in a srtring in C#, we'd have to write:
```C#
for(int i = 0; i < myString.ToCharArray().Length(); i++){
        //Do something
}
```
In ldd:
```C
loop dee doo(myString)
    (: Do something
END
```

An example program that reads an input and writes it to a file may look like the following:
```js
(: The entry point for the program
:main_
  StartProgram()
END

function StartProgram returns int::()
  loop dee doo('a' * int.MAX)
    wtf, ("Please type an input: ", false)
    string INPUT = full shwacks()
    if(INPUT == "EXIT")
      _jmpScope;
    fwtf, (INPUT, "text.txt")
  END
 return 0;
 END
 ```
