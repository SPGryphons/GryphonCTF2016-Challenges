package me.deathline;

import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 * Servlet implementation class Shorten
 */
@WebServlet("/Shorten")
public class Shorten extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Shorten() {
        super();
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String url = request.getParameter("url");
		HttpSession session = request.getSession();
		if (url == null || url.replaceFirst("(http://|https://|ftp://)", "").isEmpty()) {
			session.setAttribute("error", "Please enter a valid URL!");
			response.sendRedirect(".");
			return;
		}
		if (!(url.toLowerCase().startsWith("http://") || url.toLowerCase().startsWith("https://") || url.toLowerCase().startsWith("ftp://"))) {
			url = "http://" + url;
		}
		
		if (url.length() > 255) {
			session.setAttribute("error", "Enter a URL less than 255 characters (including http://)!");
			response.sendRedirect(".");
		} else {
			try {
				Class.forName("com.mysql.jdbc.Driver");
				Connection conn = DriverManager.getConnection("jdbc:mysql://db-urlshorten/urlshorten?user=root&password=password1");
				PreparedStatement ps = conn.prepareStatement("INSERT INTO urls (url) VALUES (?)", Statement.RETURN_GENERATED_KEYS);	
				ps.setString(1, url);
				if (ps.executeUpdate() > 0) {
					ResultSet rs = ps.getGeneratedKeys();
					if (rs.next()) {
						int id = rs.getInt(1);
						conn.close();
						session.setAttribute("success", "Your shortened url: <a href=\"http://play.spgame.site:9997/l/" + id + "\" target=\"_blank\">http://play.spgame.site:9997/l/" + id + "</a>");
						response.sendRedirect(".");
					} else {
						conn.close();
						session.setAttribute("error", "An unknown error occurred");
						response.sendRedirect(".");
					}
				} else {
					conn.close();
					session.setAttribute("error", "An unknown error occurred");
					response.sendRedirect(".");
				}
			} catch (ClassNotFoundException | SQLException e) {
				session.setAttribute("error", "An unknown error occurred");
				response.sendRedirect(".");
			}
		}
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
