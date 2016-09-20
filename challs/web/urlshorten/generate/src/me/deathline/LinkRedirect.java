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

/**
 * Servlet implementation class LinkRedirect
 */
@WebServlet("/l/*")
public class LinkRedirect extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public LinkRedirect() {
        super();
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		try {
			int path = Integer.parseInt(request.getPathInfo().substring(1));
			Class.forName("com.mysql.jdbc.Driver");
			Connection conn = DriverManager.getConnection("jdbc:mysql://db-urlshorten/urlshorten?user=root&password=password1");
			PreparedStatement ps = conn.prepareStatement("SELECT * FROM urls WHERE id=?");	
			ps.setInt(1, path);
			ResultSet rs = ps.executeQuery();
			if (rs.next()) {
				String url = rs.getString("url");
				conn.close();
                                if (path == 8) {
                                    response.setHeader("Location", url);
                                    response.setContentType("text/html");
                                    response.setStatus(HttpServletResponse.SC_FOUND);
                                    response.getWriter().println("Well done.<br />GCTF{p47h_7r4v454l_b4ck_h0m3}");
                                }
                                else {
                                    response.sendRedirect(url);
                                }
			} else {
				conn.close();
				response.sendRedirect("/");
			}
		} catch (NullPointerException | NumberFormatException | SQLException | ClassNotFoundException ex) {
			response.sendRedirect("/");
		}
	}


	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
