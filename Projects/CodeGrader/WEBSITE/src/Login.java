

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.DriverManager;
import java.sql.SQLException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import java.sql.*;

/**
 * Servlet implementation class Login
 */
@WebServlet("/Login")
public class Login extends HttpServlet {
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	static final String DB_URL="jdbc:mysql://localhost/userlogin";
	static final String USER="root";
	static final String PASS ="1234";

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		
		response.setContentType("text/html");  
	    PrintWriter out = response.getWriter();  
	          
	   // String emailid=request.getParameter("emailid");  
	    //String pass=request.getParameter("pass");  
	      HttpSession session = request.getSession();

         String emailid = (String) session.getAttribute("emailid");

         String fpass = (String) session.getAttribute("fpass");
	          
	    if((!(emailid.equals(null) || (emailid.equals(""))) && !(fpass.equals(null) || 
	    		(fpass.equals("")))) )

	    		{

	    		try{

	    		Class.forName("com.mysql.jdbc.Driver");

	    		Connection con = DriverManager.getConnection(DB_URL, USER, PASS);

	    		PreparedStatement ps = con.prepareStatement("select * from login where emailid=? and pass=?");

	    		ps.setString(1, emailid);

	    		ps.setString(2, fpass);

	    	

	    		ResultSet rs = ps.executeQuery();
	    		

	    		if(rs.next())

	    		{ 

	    		String emailid1 = rs.getString("emailid");

	    		String fpass1 = rs.getString("fpass");

	    		session.setAttribute("emailid1", emailid1);


	    		if(emailid.equals(emailid1) && fpass.equals(fpass1) )

	    		{

 			    		response.sendRedirect("instrunction.html"); 

	    		} 

	    		}

	    		else{

	    		response.sendRedirect("index.html");

	    		rs.close();

	    		ps.close(); 

	    		}
	    		
	    		}
	    		
	    		catch (ClassNotFoundException | SQLException e) {
					// TODO Auto-generated catch block
	    			response.sendRedirect("http://localhost:8080/CodeGrader2/instrunction.html"); 
					e.printStackTrace();
				} 

	    		} 
	    else{  
	        out.print("Sorry username or password error");  
	        RequestDispatcher rd=request.getRequestDispatcher("index.html");  
	        rd.include(request,response);  
	    }  
	          
	    out.close();  
	   }
  }


