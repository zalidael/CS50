{"filter":false,"title":"application1.py","tooltip":"/pset7/finance/application1.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":97,"column":20},"end":{"row":98,"column":0},"action":"remove","lines":["",""],"id":832}],[{"start":{"row":104,"column":0},"end":{"row":105,"column":21},"action":"remove","lines":["    ","    # return to index"],"id":833}],[{"start":{"row":179,"column":0},"end":{"row":180,"column":81},"action":"remove","lines":["    ","        # insert the new user into users, storing the hash of the user's password"],"id":834}],[{"start":{"row":188,"column":0},"end":{"row":188,"column":43},"action":"remove","lines":["        # remember which user has logged in"],"id":835}],[{"start":{"row":187,"column":8},"end":{"row":188,"column":0},"action":"remove","lines":["",""],"id":836}],[{"start":{"row":190,"column":0},"end":{"row":190,"column":36},"action":"remove","lines":["        # redirect user to home page"],"id":837}],[{"start":{"row":189,"column":4},"end":{"row":190,"column":0},"action":"remove","lines":["",""],"id":838}],[{"start":{"row":164,"column":0},"end":{"row":164,"column":26},"action":"remove","lines":["    return apology(\"TODO\")"],"id":839}],[{"start":{"row":164,"column":0},"end":{"row":173,"column":44},"action":"insert","lines":["    if request.method == \"POST\":","        rows = lookup(request.form.get(\"symbol\"))","        ","        if not rows:","            return apology(\"Invalid Symbol\")","            ","        return render_template(\"quoted.html\", stock=rows)","    ","    else:","        return render_template(\"quote.html\")"],"id":840}],[{"start":{"row":163,"column":26},"end":{"row":163,"column":27},"action":"insert","lines":["\\"],"id":841}],[{"start":{"row":163,"column":26},"end":{"row":163,"column":27},"action":"remove","lines":["\\"],"id":842}],[{"start":{"row":163,"column":26},"end":{"row":164,"column":0},"action":"insert","lines":["",""],"id":843},{"start":{"row":164,"column":0},"end":{"row":164,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":171,"column":32},"end":{"row":171,"column":38},"action":"remove","lines":["quoted"],"id":844},{"start":{"row":171,"column":32},"end":{"row":171,"column":33},"action":"insert","lines":["q"]}],[{"start":{"row":171,"column":33},"end":{"row":171,"column":34},"action":"insert","lines":["u"],"id":845}],[{"start":{"row":171,"column":34},"end":{"row":171,"column":35},"action":"insert","lines":["o"],"id":846}],[{"start":{"row":171,"column":35},"end":{"row":171,"column":36},"action":"insert","lines":["t"],"id":847}],[{"start":{"row":171,"column":36},"end":{"row":171,"column":37},"action":"insert","lines":["e"],"id":848}],[{"start":{"row":171,"column":37},"end":{"row":171,"column":38},"action":"insert","lines":["f"],"id":849}],[{"start":{"row":171,"column":38},"end":{"row":171,"column":39},"action":"insert","lines":["o"],"id":850}],[{"start":{"row":171,"column":39},"end":{"row":171,"column":40},"action":"insert","lines":["u"],"id":851}],[{"start":{"row":171,"column":40},"end":{"row":171,"column":41},"action":"insert","lines":["n"],"id":852}],[{"start":{"row":171,"column":41},"end":{"row":171,"column":42},"action":"insert","lines":["d"],"id":853}],[{"start":{"row":187,"column":39},"end":{"row":187,"column":40},"action":"insert","lines":[" "],"id":854}],[{"start":{"row":187,"column":39},"end":{"row":187,"column":40},"action":"remove","lines":[" "],"id":855}],[{"start":{"row":187,"column":39},"end":{"row":187,"column":40},"action":"insert","lines":["1"],"id":856}],[{"start":{"row":187,"column":64},"end":{"row":187,"column":79},"action":"remove","lines":["confirmpassword"],"id":857},{"start":{"row":187,"column":64},"end":{"row":187,"column":65},"action":"insert","lines":["p"]}],[{"start":{"row":187,"column":65},"end":{"row":187,"column":66},"action":"insert","lines":["a"],"id":858}],[{"start":{"row":187,"column":66},"end":{"row":187,"column":67},"action":"insert","lines":["s"],"id":859}],[{"start":{"row":187,"column":67},"end":{"row":187,"column":68},"action":"insert","lines":["s"],"id":860}],[{"start":{"row":187,"column":68},"end":{"row":187,"column":69},"action":"insert","lines":["w"],"id":861}],[{"start":{"row":187,"column":69},"end":{"row":187,"column":70},"action":"insert","lines":["o"],"id":862}],[{"start":{"row":187,"column":70},"end":{"row":187,"column":71},"action":"insert","lines":["r"],"id":863}],[{"start":{"row":187,"column":71},"end":{"row":187,"column":72},"action":"insert","lines":["d"],"id":864}],[{"start":{"row":187,"column":72},"end":{"row":187,"column":73},"action":"insert","lines":["2"],"id":865}],[{"start":{"row":185,"column":35},"end":{"row":185,"column":40},"action":"remove","lines":["prove"],"id":866},{"start":{"row":185,"column":35},"end":{"row":185,"column":36},"action":"insert","lines":["p"]}],[{"start":{"row":185,"column":36},"end":{"row":185,"column":37},"action":"insert","lines":["r"],"id":867}],[{"start":{"row":185,"column":37},"end":{"row":185,"column":38},"action":"insert","lines":["o"],"id":868}],[{"start":{"row":185,"column":38},"end":{"row":185,"column":39},"action":"insert","lines":["v"],"id":869}],[{"start":{"row":185,"column":39},"end":{"row":185,"column":40},"action":"insert","lines":["i"],"id":870}],[{"start":{"row":185,"column":40},"end":{"row":185,"column":41},"action":"insert","lines":["d"],"id":871}],[{"start":{"row":185,"column":41},"end":{"row":185,"column":42},"action":"insert","lines":["e"],"id":872}],[{"start":{"row":184,"column":43},"end":{"row":184,"column":44},"action":"insert","lines":["1"],"id":873}],[{"start":{"row":193,"column":80},"end":{"row":193,"column":81},"action":"insert","lines":["1"],"id":874}],[{"start":{"row":202,"column":4},"end":{"row":202,"column":5},"action":"insert","lines":["/"],"id":888}],[{"start":{"row":202,"column":5},"end":{"row":202,"column":6},"action":"insert","lines":["*"],"id":889}],[{"start":{"row":203,"column":49},"end":{"row":203,"column":50},"action":"insert","lines":["*"],"id":890}],[{"start":{"row":203,"column":50},"end":{"row":203,"column":51},"action":"insert","lines":["/"],"id":891}],[{"start":{"row":203,"column":50},"end":{"row":203,"column":51},"action":"remove","lines":["/"],"id":892}],[{"start":{"row":203,"column":49},"end":{"row":203,"column":50},"action":"remove","lines":["*"],"id":893}],[{"start":{"row":203,"column":48},"end":{"row":203,"column":49},"action":"remove","lines":[" "],"id":894}],[{"start":{"row":203,"column":48},"end":{"row":203,"column":49},"action":"insert","lines":["*"],"id":895}],[{"start":{"row":203,"column":49},"end":{"row":203,"column":50},"action":"insert","lines":["~"],"id":896}],[{"start":{"row":203,"column":49},"end":{"row":203,"column":50},"action":"remove","lines":["~"],"id":897}],[{"start":{"row":203,"column":49},"end":{"row":203,"column":50},"action":"insert","lines":["|"],"id":898}],[{"start":{"row":203,"column":49},"end":{"row":203,"column":50},"action":"remove","lines":["|"],"id":899}],[{"start":{"row":203,"column":49},"end":{"row":203,"column":50},"action":"insert","lines":["\\"],"id":900}],[{"start":{"row":203,"column":49},"end":{"row":203,"column":50},"action":"remove","lines":["\\"],"id":901}],[{"start":{"row":203,"column":48},"end":{"row":203,"column":49},"action":"remove","lines":["*"],"id":902}],[{"start":{"row":203,"column":47},"end":{"row":203,"column":48},"action":"remove","lines":[" "],"id":903}],[{"start":{"row":202,"column":5},"end":{"row":202,"column":6},"action":"remove","lines":["*"],"id":904}],[{"start":{"row":202,"column":4},"end":{"row":202,"column":5},"action":"remove","lines":["/"],"id":905}],[{"start":{"row":202,"column":4},"end":{"row":202,"column":5},"action":"insert","lines":[" "],"id":906}],[{"start":{"row":202,"column":5},"end":{"row":202,"column":6},"action":"insert","lines":["/"],"id":907}],[{"start":{"row":202,"column":6},"end":{"row":202,"column":7},"action":"insert","lines":["/"],"id":908}],[{"start":{"row":202,"column":7},"end":{"row":202,"column":8},"action":"insert","lines":[" "],"id":909}],[{"start":{"row":203,"column":4},"end":{"row":203,"column":8},"action":"remove","lines":["    "],"id":910}],[{"start":{"row":203,"column":4},"end":{"row":203,"column":8},"action":"insert","lines":["    "],"id":911}],[{"start":{"row":203,"column":8},"end":{"row":203,"column":9},"action":"insert","lines":["/"],"id":912}],[{"start":{"row":203,"column":9},"end":{"row":203,"column":10},"action":"insert","lines":["/"],"id":913}],[{"start":{"row":203,"column":10},"end":{"row":203,"column":11},"action":"insert","lines":[" "],"id":914}],[{"start":{"row":203,"column":10},"end":{"row":203,"column":11},"action":"remove","lines":[" "],"id":915}],[{"start":{"row":203,"column":9},"end":{"row":203,"column":10},"action":"remove","lines":["/"],"id":916}],[{"start":{"row":203,"column":8},"end":{"row":203,"column":9},"action":"remove","lines":["/"],"id":917}],[{"start":{"row":202,"column":7},"end":{"row":202,"column":8},"action":"remove","lines":[" "],"id":918}],[{"start":{"row":202,"column":6},"end":{"row":202,"column":7},"action":"remove","lines":["/"],"id":919}],[{"start":{"row":202,"column":5},"end":{"row":202,"column":6},"action":"remove","lines":["/"],"id":920}],[{"start":{"row":202,"column":5},"end":{"row":202,"column":6},"action":"insert","lines":["/"],"id":921}],[{"start":{"row":202,"column":6},"end":{"row":202,"column":7},"action":"insert","lines":["*"],"id":922}],[{"start":{"row":202,"column":7},"end":{"row":202,"column":8},"action":"insert","lines":[" "],"id":923}],[{"start":{"row":202,"column":7},"end":{"row":202,"column":8},"action":"remove","lines":[" "],"id":924}],[{"start":{"row":202,"column":6},"end":{"row":202,"column":7},"action":"remove","lines":["*"],"id":925}],[{"start":{"row":202,"column":5},"end":{"row":202,"column":6},"action":"remove","lines":["/"],"id":926}],[{"start":{"row":202,"column":5},"end":{"row":202,"column":6},"action":"insert","lines":["#"],"id":927}],[{"start":{"row":202,"column":6},"end":{"row":202,"column":7},"action":"insert","lines":[" "],"id":928}],[{"start":{"row":203,"column":8},"end":{"row":203,"column":9},"action":"insert","lines":["#"],"id":929}],[{"start":{"row":203,"column":9},"end":{"row":203,"column":10},"action":"insert","lines":[" "],"id":930}],[{"start":{"row":202,"column":6},"end":{"row":202,"column":7},"action":"remove","lines":[" "],"id":931}],[{"start":{"row":202,"column":5},"end":{"row":202,"column":6},"action":"remove","lines":["#"],"id":932}],[{"start":{"row":203,"column":9},"end":{"row":203,"column":10},"action":"remove","lines":[" "],"id":933}],[{"start":{"row":203,"column":8},"end":{"row":203,"column":9},"action":"remove","lines":["#"],"id":934}],[{"start":{"row":203,"column":4},"end":{"row":203,"column":8},"action":"remove","lines":["    "],"id":935}],[{"start":{"row":203,"column":0},"end":{"row":203,"column":4},"action":"remove","lines":["    "],"id":936}],[{"start":{"row":202,"column":10},"end":{"row":203,"column":0},"action":"remove","lines":["",""],"id":937}],[{"start":{"row":202,"column":10},"end":{"row":203,"column":0},"action":"insert","lines":["",""],"id":938},{"start":{"row":203,"column":0},"end":{"row":203,"column":9},"action":"insert","lines":["         "]}],[{"start":{"row":202,"column":4},"end":{"row":202,"column":5},"action":"remove","lines":[" "],"id":940}],[{"start":{"row":203,"column":8},"end":{"row":203,"column":9},"action":"remove","lines":[" "],"id":941}],[{"start":{"row":203,"column":4},"end":{"row":203,"column":8},"action":"remove","lines":["    "],"id":942}],[{"start":{"row":203,"column":0},"end":{"row":203,"column":4},"action":"remove","lines":["    "],"id":943}],[{"start":{"row":202,"column":9},"end":{"row":203,"column":0},"action":"remove","lines":["",""],"id":944}],[{"start":{"row":202,"column":9},"end":{"row":203,"column":0},"action":"insert","lines":["",""],"id":945},{"start":{"row":203,"column":0},"end":{"row":203,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":100,"column":27},"end":{"row":100,"column":36},"action":"remove","lines":["portfolio"],"id":946},{"start":{"row":100,"column":27},"end":{"row":100,"column":32},"action":"insert","lines":["entry"]}]]},"ace":{"folds":[],"scrolltop":1394,"scrollleft":0,"selection":{"start":{"row":96,"column":54},"end":{"row":96,"column":54},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":86,"state":"start","mode":"ace/mode/python"}},"timestamp":1495028673721,"hash":"7e656e8f77530fba0b73bc256494cd9c5632d27c"}