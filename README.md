# Ex03 Time Table
# Date : 05-10-2023

## AIM
To write a html webpage page to display your slot timetable.

## ALGORITHM
### STEP 1
Create a Django-admin Interface.

### STEP 2
Create a static folder and inert HTML code.

### STEP 3
Create a simple table using ```<table>``` tag in html.

### STEP 4
Add header row using ```<th>``` tag.

### STEP 5
Add your timetable using ```<td>``` tag.

### STEP 6
Execute the program using runserver command.

## CODE
```
<!DOCTYPE html>
<html>
    <head>
        <title>Timetable</title>
    </head>
    <body>
      <center>
        <img src="Screenshot 2023-10-05 152818.png" height="100" width="540">
        </center>
<table align="center" width="540" cellspacing="2" cellpadding="4" border="5" bgcolor="cyan">
<caption><b>SLOT TIME TABLE -   Karpagakirthika V(212221220025)</b></caption>
<tr align="center">
<th bgcolor="green">Day/Time</th>
<th bgcolor="green">8-10</th>
<th bgcolor="green">10-12</th>
<th bgcolor="green">12-1</th>
<th bgcolor="green">1-3</th>
<th bgcolor="green">3-5</th>
</tr>

<tr align="center">
<th bgcolor="yellow">Monday</th>
<th bgcolor="cyan"> FREE SLOT </th>
<th bgcolor="cyan"> FREE SLOT </th>
<th bgcolor="cyan" rowspan="6" align="center">LUNCH BREAK</th>
<th bgcolor="cyan">Employment enhancement skills</th>
<th bgcolor="cyan">Cryptography and network security</th>
</tr>

<tr align="center">
<th bgcolor="yellow">Tuesday</th>
<th bgcolor="cyan">FWAD</th>
<th bgcolor="cyan">CD</th>
<th bgcolor="cyan">mini project</th>
<th bgcolor="cyan">FREE SLOT</th>
</tr>

<tr align="center">
<th bgcolor="yellow">Wednesday</th>
<th bgcolor="cyan">CD</th>
<th bgcolor="cyan">FREE SLOT</th>
<th bgcolor="cyan">Game programming</th>
<th bgcolor="cyan">FREE SLOT</th>
</tr>

<tr align="center">
<th bgcolor="yellow">Thrusday</th>
<th bgcolor="cyan">GCC</th>
<th bgcolor="cyan">Game programming</th>
<th bgcolor="cyan">FREE SLOT</th>
<th bgcolor="cyan">FWAD</th>
</tr>

<tr align="center">
<th bgcolor="yellow">Friday</th>
<th bgcolor="cyan">FREE SLOT</th>
<th bgcolor="cyan">FREE SLOT</th>
<th bgcolor="cyan">FREE SLOT</th>
<th bgcolor="cyan">FREE SLOT</th>
</tr>

<tr align="center">
  <th bgcolor="yellow">Saturday</th>
  <th bgcolor="cyan">FREE SLOT</th>
  <th bgcolor="cyan">Cryptography and network security</th>
  <th bgcolor="cyan">GCC</th>
  <th bgcolor="cyan">FWAD</th>
  </tr>
</table>

<br>
<table align="center" cellspacing="2" cellpadding="4" border="2">
<tr align="center">
<th>S. No.</th>
<th>Subject Code</th>
<th>Subject Name</th>
</tr>

<tr>
<td align="center">1.</td>
<td align="center">19AI414</td>
<td>Fundamentals of Web Application Development (FWAD)</td>
</tr>

<tr>
<td align="center">2.</td>
<td align="center">19CS409</td>
<td>Compiler Design(CD)</td>
</tr>

<tr>
<td align="center">3.</td>
<td align="center">19EY705</td>
<td>Employment enhancement skills </td>
</tr>

<tr>
<td align="center">4.</td>
<td align="center">19CS412</td>
<td> Cryptography and network security </td>
</tr>

<tr>
<td align="center">5.</td>
<td align="center">19AI513</td>
<td>Game programming</td>
</tr>

<tr>
<td align="center">6.</td>
<td align="center">19IT406</td>
<td>Grid and Cloud Computing</td>
</tr>

<tr>
<td align="center">6.</td>
<td align="center">19IT701</td>
<td>Mini project</td>
</tr>
</table>
</body>
</html>
```
## OUTPUT

![Alt text](<Screenshot 2023-10-05 155241.png>)


## RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
