import java.io.IOException;



import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.Statement;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;


/**
 * Servlet implementation class Register
 */
@WebServlet("/Register")
public class Register extends HttpServlet {
	static final String DB_URL="jdbc:mysql://localhost/userlogin";
	static final String USER="root";
			static final String PASS ="1234";
	protected void doPost(HttpServletRequest req, HttpServletResponse resp)
			throws ServletException, IOException {
		
		resp.setContentType("text/html");
		PrintWriter out=resp.getWriter();
		String n1=req.getParameter("firstname");
		String n2=req.getParameter("lastname");
		String emailid=req.getParameter("emailid");
		String fpass=req.getParameter("fpass");
		String n5=req.getParameter("mpass");
		String n6=req.getParameter("gender");
		String n7=req.getParameter("qualification");
		
		HttpSession session = req.getSession();
		session.setAttribute("emailid", emailid);
		session.setAttribute("fpass", fpass);
		
try
	{
		Class.forName("com.mysql.jdbc.Driver");
		Connection conn=DriverManager.getConnection(DB_URL,USER,PASS);
		PreparedStatement ps=conn.prepareStatement("insert into login values(?,?,?,?,?,?,?)");
	    ps.setString(1,n1);
	    ps.setString(2, n2);
	    ps.setString(3, emailid);
	    ps.setString(4, fpass);
	    ps.setString(5, n5);
	    ps.setString(6, n6);
	    ps.setString(7, n7);
	 
	    int i=ps.executeUpdate();
	
		if(i>0)
		{
			resp.sendRedirect("http://localhost:8080/CodeGrader2/signin.html");	
		}
	
	     }catch(Exception e2){System.out.println(e2);}
	out.close();
	}	
}
