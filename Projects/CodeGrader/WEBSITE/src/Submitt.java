import java.io.File;
import java.io.IOException;



import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;


/**
 * Servlet implementation class Register
 */
@WebServlet("/Submitt")
public class Submitt extends HttpServlet {
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
		
		System.out.print(emailid);
		
try

	{
		Class.forName("com.mysql.jdbc.Driver");
		Connection conn=DriverManager.getConnection(DB_URL,USER,PASS);
		//String query = "insert into submission (question_id,user_id,file_name) values('1',"+emailid+",'')";
		//PreparedStatement ps=conn.prepareStatement(query, Statement.RETURN_GENERATED_KEYS);
		String ps="insert into submission (question_id,user_id,file_name) values(?,?,?)";
		PreparedStatement ps2=conn.prepareStatement(ps);
		PreparedStatement ps1=conn.prepareStatement(ps, Statement.RETURN_GENERATED_KEYS);
	      ps2.setString(1, "1");
		  ps2.setString(2,emailid);
		  ps2.setString(3,file_name);
	 
	      ps2.executeUpdate(); 
	 
	      ps1.executeUpdate();
	boolean returnLastInsertId = true ;
	
	    int auto_id=0;
		if(returnLastInsertId)
		{
			ResultSet rs = ps1.getGeneratedKeys();
			rs.next();
			auto_id = rs.getInt(1);
			//String id= ""+auto_id;
			new File("C:\\Users\\munen\\workspace\\Grader\\WebContent\\"+auto_id+"").mkdirs();
			
			//req.setAttribute("auto_id", auto_id);
			//RequestDispatcher rd=req.getRequestDispatcher("http://localhost:8080/CodeGrader2/Submitt");
			//rd.forward(req, resp);
			
			if(auto_id >0)
			{
				
				resp.sendRedirect("result2.html");
			}
		}
		   
	}

	catch(Exception e2){
		System.out.println(e2);
		}
	out.close();
	}	
}
