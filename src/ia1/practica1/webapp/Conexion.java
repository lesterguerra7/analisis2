package ia1.practica1.webapp;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.LinkedList;

public class Conexion {
	Connection conn = null;
	
	public Connection Conectar(){		 
        try {
            String dbURL = "jdbc:sqlserver://localhost:1433;DatabaseName=Practica1_IA1";
            String user = "sa";
            String pass = "1234";
            try {
				Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
			} catch (ClassNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
            conn = DriverManager.getConnection(dbURL, user, pass);
            return conn;
 
        } catch (SQLException ex) {
            ex.printStackTrace();
            return null;
        }
	}
    
    public void Desconectar(){
    	try {
            if (conn != null && !conn.isClosed()) {
                conn.close();
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }
    
    public LinkedList<Pregunta> Consultar(String Pregunta){
    	Pregunta = Pregunta.replace("'", "");
    	Statement stmt;
    	LinkedList<Pregunta> Preguntas = new LinkedList<Pregunta>();
		try {
			stmt = conn.createStatement();
			ResultSet rs;
	        rs = stmt.executeQuery("select TOP 1 P.Pregunta, P.Respuesta from practica1_IA1.dbo.PREGUNTA P, FREETEXTTABLE(practica1_IA1.dbo.PREGUNTA, pregunta, '\"" + Pregunta + "\"') C Where P.idPregunta = C.[KEY] Order  By C.Rank desc");
	        while ( rs.next() ) {
	        	String strPregunta = rs.getString("Pregunta");
	        	String strRespuesta = rs.getString("Respuesta");
	        	Preguntas.add(new Pregunta(strPregunta, strRespuesta));
	        }
	        return Preguntas;
		} catch (SQLException e) {
			e.printStackTrace();
			return null;
		}
        
    }

}