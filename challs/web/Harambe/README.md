# Harambe
This challenge imitates the developer's nature of commenting code for future use as a vulnerability to servers.

## Question Text
Harambe is love. Harambe is life

http://play.spgame.site:9998

## Setup Guide
Deploy using any form of PHP web application.

## Solution
1. Uncomment the html code in the webpage
2. Add the following lines to the form and fill in the data form.
```html
 				<div style="margin-bottom:5px">
					Name: <input type="text" name="name"/>
				</div>
				<div style="margin-bottom:5px">
					Comment:<br/>
					<textarea rows="4" cols="50" name="comment"></textarea>
				</div> 
```
3. Disable Javascript to prevent text validation
4. Send and get your flag!