<html><head> 
<script> 
<!-- 
<% 
String clock = request.getParameter( "clock" ); 
if( clock == null ) clock = "120"; 
%> 
var timeout = <%=clock%>; 
function timer() 
{ 
if( --timeout > 0 ) 
{ 
document.forma.clock.value = timeout; 
window.setTimeout( "timer()", 60000 ); 
} 
else 
{ 
document.forma.clock.value = "Time over"; 
///disable submit-button etc 
} 
} 
//--> 
</script> 
<body> 
<form action="<%=request.getRequestURL()%>" name="forma"> 
 <input type="text" name="clock" value="<%=clock%>" style="border:0px solid white;"> 
... 
</form> 
<script> 
<!-- 
timer(); 
//--> 
</script> 
</body></html>