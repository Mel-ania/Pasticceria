# Pasticceria - Ai 4 cioccolati

The content is in italian, everything else is in english.

This is a simple website for a bakery that wants its own showcase open to everyone.

## Languages

- Backend: Python (v3.7) - Flask;
- Frontend: HTML, JavaScript (JQuery), CSS;
- Database: Firebase (NoSQL).
 
## Website

The available areas at the moment are: home, contact, sign-in/out and backoffice.

- The **home page** is an exhibition showcase with a list of all the cakes available for sale. For each cake, you also see the quantity available and its price. The price varies depending on the day the cake was prepared. Users may not know how long a cake has been on sale, but the price will drop as the days go by. The first day is worth the full price, the second day is worth 80% of the price and the third day is worth 20% of the price. When a cake has expired, it will no longer appear. Passing over a cake’s box, an overlayer appears following the cursor. The overlayer contains the list of ingredients with their quantities and units of measure.
- The **contact page** only contains the address, the telephone number of the bakery and the email of the owners.
- The **sign-in/out page** is a normal sign-in/out page where emails and passwords are required to log in. There is no registration page, only the owners can access the website's backoffice.
- The **backoffice page** allows you to view all the cakes as in the home page. By clicking on a cake's box you can change the number of cakes available according to those sold. When availability drops to zero, the cake will be deleted from the database. Once you choose the new availability you will have to confirm the update. From this page you can reach another **page to add a new cake**. To add a new cake, you have to specify the name, the availability of cakes of that kind, the price and the ingredients. The day of the cake's preparation is automatically added. For each ingredient, you must specify the name, quantity and unit of measurement. The number of ingredients is dynamic and you can add them at will.

### Sample video

Here is a video to show how the web app works and its responsive adaptation to different screen sizes and resolutions.

https://user-images.githubusercontent.com/64848167/117580706-88005300-b0f9-11eb-99ba-8180bf52dead.mp4
