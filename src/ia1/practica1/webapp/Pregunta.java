package ia1.practica1.webapp;

public class Pregunta {
	private String Pregunta;
	private String Respuesta;
	public Pregunta(String Pregunta, String Respuesta) {
		this.Pregunta = Pregunta;
		this.Respuesta = Respuesta;
	}
	public String getPregunta() {
		return Pregunta;
	}
	public void setPregunta(String pregunta) {
		Pregunta = pregunta;
	}
	public String getRespuesta() {
		return Respuesta;
	}
	public void setRespuesta(String respuesta) {
		Respuesta = respuesta;
	}
	
	//Otro comentario
}
