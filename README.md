# MetaCTF-CyberGames-2021<br>
[Link to Stats](https://compete.metactf.com/60/view_team?tid=8440)<br>
<br>
## Web Exploitation<br>
### WAS my flag? Part I (Solved after tournament ended)<br>
We are given a link that leads us to the following webpage<br>
![image](https://user-images.githubusercontent.com/51941044/145773006-59251ef0-9afc-45c5-92b4-39e1c2df8dfa.png)<br>
In the sources tab of the browser, you can find a file named flagco.wasm<br>
![image](https://user-images.githubusercontent.com/51941044/145773212-43b68656-baa9-49c4-a4e7-8fb8f7208917.png)<br>
Turns out this is a reverse engineering challenge involving a WASM binary file<br>
I put a breakpoint after the beginning of the checkFlag function at 0x0044e<br>
![image](https://user-images.githubusercontent.com/51941044/145773660-645924c1-a594-402e-93ed-e5869bcb8003.png)<br>
Stepping through the execution 1 line at a time, we eventually reach a function call for $func201 at 0x00471<br>
After repeatedly running this program with various inputs, I determined that the function returned the length of the string inputted into the flag generator. You can see the value of 26 being returned from the function and later on is checked. Now we know that the flag is 26 letters in length!<br>
![image](https://user-images.githubusercontent.com/51941044/145774321-ee305ac0-d476-4fcd-b54d-10bddea95ac4.png)<br>
I then watched the stack for values that would be equivalent to the decimal representation of the input strings and the flag. Likely values would roughly be in the range of 32-125.<br>
There would then be two function calls where the input string would be tested for a match with the flag.<br>
The function called at 0x004c1 would test if the first 8 characters matched MetaCTF{ in the first pass<br>
The function would then be called again to test the remaining characters in the flag. I would then use a fake input of length 26, and then iteratively build the flag from the first to last character. To speed this up, I used breakpoints at 0x17bc and 0x17e1 inside of the function testing for character equivalence.<br>
![image](https://user-images.githubusercontent.com/51941044/145775689-588f70f3-56b3-41f6-a353-d8137893dfec.png)<br>
From above you can see that where I paused it would compare the decimal representation of the input and flag. In this case they are both s (115, as shown on the stack). So by skipping to the next breakpoint I could quickly retrieve the value and then restart the process when the remaining filler input failed.<br><br>
Once every character was leaked, we were greeted with a success message and the flag MetaCTF{sauc3_expr3s51on5}<br>
![image](https://user-images.githubusercontent.com/51941044/145776304-552ea830-9018-4aa5-bb4b-19da2bfb5eaa.png)
