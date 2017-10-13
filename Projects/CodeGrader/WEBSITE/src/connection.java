import java.sql.Connection;
import java.sql.DriverManager;


public class connection {
	private connection(){}
	public static Connection con;
	static{
		try{
			Class.forName(dbinitialize.Driver);
			con=DriverManager.getConnection(dbinitialize.con_String,dbinitialize.Username,dbinitialize.Password);
	  }
	  catch(Exception e)
	  {
		  System.out.println(e);
	  }
}

public static Connection connect()
{
	return con;	
}
}
