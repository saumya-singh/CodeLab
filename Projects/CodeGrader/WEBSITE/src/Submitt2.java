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
@WebServlet("/Submitt2")
public class Submitt2 extends HttpServlet {
	static final String DB_URL="jdbc:mysql://localhost/userlogin";
	static final String USER="root";
			static final String PASS ="1234";
	protected void doPost(HttpServletRequest req, HttpServletResponse resp)
			throws ServletException, IOException {
		resp.setContentType("text/html");
		PrintWriter out=resp.getWriter();
		HttpSession session = req.getSession();
		String n1=req.getParameter("questionid");
		String emailid = (String) session.getAttribute("emailid");
		String file_name = (String) session.getAttribute("file_name");
		
try
	{
		Class.forName("com.mysql.jdbc.Driver");
		Connection conn=DriverManager.getConnection(DB_URL,USER,PASS);
		PreparedStatement ps=conn.prepareStatement("insert into submission (question_id,user_id,file_name) values(?,?,?)");
		ps.setString(1, "3");
		ps.setString(2, emailid);
		ps.setString(3, file_name);
	
	
	 
	int i=ps.executeUpdate();
	
		if(i>0)
		{
			resp.sendRedirect("result4.html");	
		}
	
	}catch(Exception e2){System.out.println(e2);}
	out.close();
	}	
}
