<%@page import="java.util.LinkedList"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1" import="ia1.practica1.webapp.*, java.util.LinkedList, javax.servlet.*"%>
<%
	Conexion conexion = new Conexion();
	conexion.Conectar();
	String strParametro = request.getParameter("strMensaje");
	//String strParametro = "nanomateria";
	LinkedList<Pregunta> pregunta = conexion.Consultar(strParametro);
	conexion.Desconectar();
	if(pregunta.size() > 0){
		out.write("{\"Pregunta\":\"" + pregunta.get(0).getPregunta() + "\", \"Respuesta\":\"" + pregunta.get(0).getRespuesta() + "\"}");	
	} else {
		out.write("{\"Pregunta\":\"\", \"Respuesta\":\"No entiendo la pregunta\"}");
	}
	
%>