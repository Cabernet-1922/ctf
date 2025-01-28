# QuestionAIR [200 points] (27 solves)
First, we want to fill the same information given in the form, but you can't fill it in the interface since there are some restrictions.
We need burpsuite in this challenge.
```
name=Firebird&age=50&gender=ALL&interest[]=Apple&interest[]=Orange&email=firebird@cse.ust.hk&dob=Yesterday&comment=I%20love%20Firebird&hidden=No%20One%20Plays&submit=Submit
```
Keep in mind that `comment` also need to be filled, since it is commented in the form.
Also, represent the space as `%20`.