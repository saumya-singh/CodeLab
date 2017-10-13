

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class ResultServlet
 */
@WebServlet("/ResultServlet")
public class ResultServlet extends HttpServlet {
	static final String DB_URL="jdbc:mysql://localhost/userlogin";
	static final String USER="root";
			static final String PASS ="1234";
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub


		
		response.setContentType("text/html");
		PrintWriter out=response.getWriter();
		try{
			out.print("<html><body>");
			 
			 
			Class.forName("com.mysql.jdbc.Driver");
			Connection conn=DriverManager.getConnection(DB_URL,USER,PASS);
			Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("select * from submission");
           
            out.println("<h1>Result</h1>");
            out.println("<table border=1 ><tr><th>submission_id </th><th>time_of_submission</th><th>question_id</th><th>status</th><th>result</th><th>user_id</th><th>filename</th></tr>");
            while(rs.next())
            {
            	int n1=rs.getInt(1);
            	String n2=rs.getString(2);
            	int n3=rs.getInt(3);
            	String n4=rs.getString(4);
            	String n5=rs.getString(5);
            	String n6=rs.getString(6);
            	String n7=rs.getString(7);


            	out.println("<tr><td>"+n1+"</td><td>"+n2+"</td><td>"+n3+"</td><td>"+n4+"</td><td>"+n5+"</td><td>"+n6+"</td><td>"+n7+"</td></tr>");
            }
             out.print("</body></html>");
		}
		catch(Exception e){
			e.printStackTrace();
		out.println("1234");	
		}
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
	}

}
